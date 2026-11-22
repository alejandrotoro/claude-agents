#!/usr/bin/env python3
"""Lector de ofertas de canales públicos de Telegram (vista web t.me/s/<canal>).

Corre en GitHub Actions cada hora:
  1. Lee los mensajes nuevos de cada canal de config.json.
  2. Extrae categoría, tienda, precio, % de descuento, código/cupón, título y enlaces.
  3. Guarda las ofertas por día (hora de Bogotá) en data/dias/AAAA-MM-DD.json y actualiza data/manifest.json.
  4. Avisa por un bot de Telegram (secreto TELEGRAM_BOT_TOKEN) las ofertas nuevas que cumplan las reglas de alerta.

Solo usa la vista pública de los canales: no inicia sesión ni escribe en ellos.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
DIAS = DATA / "dias"
TZ = ZoneInfo("America/Bogota")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
      "Accept-Language": "es-CO,es;q=0.9,en;q=0.8"}

TIENDAS = {
    "amazon": "Amazon", "exito": "Éxito", "éxito": "Éxito", "falabella": "Falabella", "eneba": "Eneba",
    "instantgaming": "Instant Gaming", "mercadolibre": "Mercado Libre", "alkosto": "Alkosto", "ktronix": "Ktronix",
    "temu": "Temu", "shein": "Shein", "walmart": "Walmart", "aliexpress": "AliExpress", "ebay": "eBay",
    "adidas": "Adidas", "nike": "Nike", "homecenter": "Homecenter", "jumbo": "Jumbo", "olimpica": "Olímpica",
    "olímpica": "Olímpica", "rappi": "Rappi", "d1": "D1", "ara": "Ara", "puma": "Puma", "samsung": "Samsung",
    "apple": "Apple", "steam": "Steam", "epicgames": "Epic Games", "xbox": "Xbox", "playstation": "PlayStation",
    "linio": "Linio", "dafiti": "Dafiti", "panamericana": "Panamericana", "colsubsidio": "Colsubsidio",
    "carulla": "Carulla", "makro": "Makro", "pricesmart": "PriceSmart", "target": "Target", "bestbuy": "Best Buy",
    "costco": "Costco", "lenovo": "Lenovo", "hp": "HP", "dell": "Dell", "xiaomi": "Xiaomi", "claro": "Claro",
    "movistar": "Movistar", "tigo": "Tigo", "didi": "DiDi", "uber": "Uber",
}
BOILER = re.compile(r"(¿viste una|envíamela|compártela|comprar\s*:|ver oferta|únete a prime|unete a prime|"
                    r"revisar condiciones|^\W*$)", re.I)
RE_CODIGO = re.compile(r"(?i:cup[oó]n|c[oó]digo|code|codigo)\s*:?\s*([A-Z0-9]{5,16})\b")
NO_CODIGOS = {"DESCUENTO", "APLICANDO", "CODIGO", "CUPON", "PRIME", "GRATIS", "OFERTA", "ENTREGA"}
RE_DESC = [re.compile(r"(\d{1,2})\s*%\s*(?:de\s+)?(?:descuento|dto|off|desc)", re.I),
           re.compile(r"(?:clip|cup[oó]n|ahorra|save)[^\n%]{0,25}?(\d{1,2})\s*%", re.I)]
RE_PRECIO = re.compile(r"(USD|US|COP|CO)?\s*\$\s*([\d][\d.,]*)", re.I)
RE_ASIN = re.compile(r"(?:/dp/|/gp/product/|/product/)([A-Z0-9]{10})(?:[/?&\"']|$)")


def log(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- parseo del texto
def parse_precio(texto: str):
    m = RE_PRECIO.search(texto)
    if not m:
        return None, None
    cur = (m.group(1) or "").upper()
    raw = m.group(2).rstrip(".,")
    moneda = "COP" if cur.startswith("CO") else "USD"
    if moneda == "COP" or re.fullmatch(r"\d{1,3}(\.\d{3})+", raw):
        moneda = "COP" if moneda == "COP" or len(raw.replace(".", "")) > 5 else moneda
        val = float(raw.replace(".", "").replace(",", ""))
    else:
        val = float(raw.replace(",", ""))
    return moneda, (int(val) if val == int(val) else round(val, 2))


def parse_descuento(texto: str):
    vals = [int(m.group(1)) for r in RE_DESC for m in r.finditer(texto)]
    vals = [v for v in vals if 5 <= v <= 99]
    return max(vals) if vals else None


def parse_codigo(texto: str):
    for m in RE_CODIGO.finditer(texto):
        c = m.group(1)
        if c in NO_CODIGOS or c.isdigit():
            continue
        return c
    return None


def parse_texto(texto: str, links: list[str]) -> dict:
    lineas = [l.strip() for l in texto.split("\n") if l.strip()]
    cab = lineas[0] if lineas else ""
    tags = re.findall(r"#([\w]+)", cab, re.UNICODE)
    cats, tienda = [], None
    for t in tags:
        k = t.lower()
        if k in TIENDAS and tienda is None:
            tienda = TIENDAS[k]
        else:
            cats.append(t.replace("_", " "))
    hosts = " ".join(links).lower()
    if tienda is None:
        if re.search(r"\bprime\b|amazon", texto, re.I) or "amazon." in hosts or "amzn." in hosts or "joylink" in hosts:
            tienda = "Amazon"
        else:
            tienda = "Otra"
    moneda, precio = parse_precio(cab) if RE_PRECIO.search(cab) else parse_precio(texto)
    codigo = parse_codigo(texto)
    descuento = parse_descuento(texto)
    if codigo:
        tipo = "codigo"
    elif re.search(r"\bclip\b", texto, re.I):
        tipo = "clip"
    elif re.search(r"cup[oó]n", texto, re.I):
        tipo = "cupon"
    else:
        tipo = None
    titulo = ""
    for l in lineas[1:]:
        if BOILER.search(l) or RE_CODIGO.search(l) or re.search(r"aplica|cup[oó]n|\bclip\b|%\s*desc", l, re.I):
            continue
        if len(re.sub(r"\W", "", l)) < 4:
            continue
        titulo = l
        break
    if not titulo:
        titulo = re.sub(r"#\w+", "", cab).strip()[:140]
    titulo = re.sub(r"\s+", " ", titulo).strip(" -–·")[:200]
    return {
        "categoria": cats[0] if cats else "Otros",
        "etiquetas": cats,
        "tienda": tienda,
        "moneda": moneda,
        "precio": precio,
        "descuento": descuento,
        "codigo": codigo,
        "tipo_cupon": tipo,
        "prime": bool(re.search(r"\bprime\b", cab, re.I)),
        "titulo": titulo,
    }


# ---------------------------------------------------------------- lectura de t.me/s
def mensaje(div, canal: str) -> dict | None:
    post = div.get("data-post") or ""
    try:
        num = int(post.split("/")[-1])
    except ValueError:
        return None
    t = div.select_one(".tgme_widget_message_date time")
    if not t or not t.get("datetime"):
        return None
    cuando = datetime.fromisoformat(t["datetime"]).astimezone(TZ)
    txt_el = div.select_one(".tgme_widget_message_text")
    if not txt_el:
        return None
    links = []
    for a in txt_el.select("a[href]"):
        h = a["href"]
        host = urlparse(h).hostname or ""
        if not host or host.endswith("t.me") or host.endswith("telegram.me"):
            continue
        links.append(h)
    for br in txt_el.find_all("br"):
        br.replace_with("\n")
    for a in txt_el.select("a[href]"):
        h = urlparse(a["href"]).hostname or ""
        if h and not h.endswith("t.me") and a.get_text().startswith("http"):
            a.replace_with(" ")
    texto = txt_el.get_text("")
    texto = re.sub(r"[ \t]+", " ", texto).strip()
    img = None
    pw = div.select_one(".tgme_widget_message_photo_wrap") or div.select_one(".tgme_widget_message_video_thumb")
    if pw and pw.get("style"):
        m = re.search(r"url\(['\"]?([^'\")]+)", pw["style"])
        if m:
            img = m.group(1)
    datos = parse_texto(texto, links)
    oferta = next((l for l in links if "facebook.com" not in l), links[0] if links else None)
    return {
        "id": f"{canal}/{num}",
        "canal": canal,
        "num": num,
        "fecha": cuando.date().isoformat(),
        "hora": cuando.strftime("%H:%M"),
        "ts": cuando.isoformat(timespec="seconds"),
        **datos,
        "link_post": f"https://t.me/{canal}/{num}",
        "link_oferta": oferta,
        "imagen": img,
        "texto": texto[:900],
    }


def leer_canal(canal: str, ultimo: int, desde: datetime, max_paginas: int = 25) -> list[dict]:
    url = f"https://t.me/s/{canal}"
    vistos, out, antes = set(), [], None
    for _ in range(max_paginas):
        r = requests.get(url, params={"before": antes} if antes else None, headers=UA, timeout=25)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        divs = soup.select("div.tgme_widget_message[data-post]")
        if not divs:
            break
        nums = []
        parar = False
        for d in divs:
            m = mensaje(d, canal)
            if not m:
                try:
                    nums.append(int(d["data-post"].split("/")[-1]))
                except Exception:
                    pass
                continue
            nums.append(m["num"])
            if m["num"] <= ultimo or datetime.fromisoformat(m["ts"]) < desde:
                parar = True
                continue
            if m["id"] not in vistos:
                vistos.add(m["id"])
                out.append(m)
        if parar or not nums:
            break
        nuevo_antes = min(nums)
        if antes is not None and nuevo_antes >= antes:
            break
        antes = nuevo_antes
        time.sleep(1.2)
    log(f"  {canal}: {len(out)} mensajes nuevos")
    return out


def resolver_amazon(o: dict, sesion: requests.Session):
    """Intenta sacar el ASIN de enlaces que llevan a Amazon (joylink, amzn.to, amazon.com)."""
    l = o.get("link_oferta") or ""
    host = urlparse(l).hostname or ""
    m = RE_ASIN.search(l)
    if not m and any(h in host for h in ("joylink.io", "amzn.to", "amzn.com", "amazon.")):
        try:
            r = sesion.get(l, headers=UA, timeout=10, allow_redirects=True)
            m = RE_ASIN.search(r.url) or RE_ASIN.search(r.text[:200000])
        except Exception:
            m = None
    if m:
        o["asin"] = m.group(1)
        o["link_amazon"] = f"https://www.amazon.com/dp/{m.group(1)}"


# ---------------------------------------------------------------- alertas por bot
def tg(token: str, metodo: str, **data):
    r = requests.post(f"https://api.telegram.org/bot{token}/{metodo}", data=data, timeout=20)
    try:
        return r.json()
    except Exception:
        return {"ok": False, "description": r.text[:200]}


def descubrir_chat(token: str):
    res = tg(token, "getUpdates", timeout=0, allowed_updates=json.dumps(["message"]))
    if not res.get("ok"):
        log("  alertas: Telegram rechazó el token:", res.get("error_code"), res.get("description"))
        return None
    me = tg(token, "getMe")
    log(f"  alertas: bot @{(me.get('result') or {}).get('username')} con {len(res.get('result', []))} mensajes pendientes")
    for u in reversed(res.get("result", [])):
        msg = u.get("message") or {}
        chat = msg.get("chat") or {}
        if chat.get("type") == "private":
            return chat.get("id")
    return None


def esc(s) -> str:
    return str(s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def precio_txt(o) -> str:
    if o.get("precio") is None:
        return ""
    if o.get("moneda") == "COP":
        return "COP$" + f"{int(o['precio']):,}".replace(",", ".")
    p = o["precio"]
    return f"US${p:g}" if isinstance(p, (int, float)) else f"US${p}"


def texto_alerta(o: dict) -> str:
    partes = [f"🏷 <b>#{esc(o['categoria'])}</b> · {esc(o['tienda'])}"]
    partes.append(f"<b>{esc(o['titulo'])}</b>")
    linea = []
    if o.get("precio") is not None:
        linea.append(f"💲 {precio_txt(o)}")
    if o.get("descuento"):
        linea.append(f"-{o['descuento']}%")
    if o.get("codigo"):
        linea.append(f"Código: <code>{esc(o['codigo'])}</code>")
    elif o.get("tipo_cupon") == "clip":
        linea.append("Cupón para marcar (clip)")
    elif o.get("tipo_cupon") == "cupon":
        linea.append("Con cupón")
    if linea:
        partes.append(" · ".join(linea))
    enl = [f'<a href="{esc(o["link_post"])}">Ver post</a>']
    if o.get("link_amazon"):
        enl.append(f'<a href="{esc(o["link_amazon"])}">Amazon</a>')
    elif o.get("link_oferta"):
        enl.append(f'<a href="{esc(o["link_oferta"])}">Abrir oferta</a>')
    partes.append(" · ".join(enl) + f"  <i>({esc(o['canal'])} {o['hora']})</i>")
    return "\n".join(partes)


def pasa_alerta(o: dict, reglas: dict) -> bool:
    if reglas.get("solo_con_cupon", True) and not (o.get("tipo_cupon") or o.get("descuento")):
        return False
    mind = int(reglas.get("min_descuento", 0) or 0)
    if mind and (o.get("descuento") or 0) < mind:
        return False
    excl = {c.lower() for c in reglas.get("categorias_excluidas", [])}
    if o["categoria"].lower() in excl or any(e.lower() in excl for e in o.get("etiquetas", [])):
        return False
    incl = {c.lower() for c in reglas.get("solo_categorias", [])}
    if incl and o["categoria"].lower() not in incl:
        return False
    txt = (o.get("titulo", "") + " " + o.get("texto", "")).lower()
    if any(p.lower() in txt for p in reglas.get("palabras_excluidas", [])):
        return False
    tiendas = {t.lower() for t in reglas.get("tiendas", [])}
    if tiendas and o["tienda"].lower() not in tiendas:
        return False
    return True


def enviar_alertas(nuevas: list[dict], estado: dict, reglas: dict):
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    if not token or not reglas.get("activas", True):
        log("  alertas: sin TELEGRAM_BOT_TOKEN o desactivadas")
        return 0
    chat = estado.get("telegram_chat_id")
    if not chat:
        chat = descubrir_chat(token)
        if not chat:
            log("  alertas: el bot aún no tiene chat. Escríbele /start al bot.")
            return 0
        estado["telegram_chat_id"] = chat
        tg(token, "sendMessage", chat_id=chat, parse_mode="HTML",
           text="✅ Listo: desde ahora te aviso aquí las ofertas con código o cupón de los canales que sigo.")
    lista = [o for o in nuevas if pasa_alerta(o, reglas)]
    lista.sort(key=lambda o: o["ts"])
    maxn = int(reglas.get("max_por_corrida", 40))
    enviadas = 0
    for o in lista[:maxn]:
        cap = texto_alerta(o)
        res = {"ok": False}
        if o.get("imagen") and reglas.get("con_foto", True):
            res = tg(token, "sendPhoto", chat_id=chat, photo=o["imagen"], caption=cap[:1020], parse_mode="HTML")
        if not res.get("ok"):
            res = tg(token, "sendMessage", chat_id=chat, text=cap, parse_mode="HTML", disable_web_page_preview="true")
        if res.get("ok"):
            enviadas += 1
        else:
            log("  alerta falló:", res.get("description"))
            if res.get("error_code") == 429:
                time.sleep(int(res.get("parameters", {}).get("retry_after", 5)) + 1)
        time.sleep(1.1)
    if len(lista) > maxn:
        tg(token, "sendMessage", chat_id=chat, parse_mode="HTML",
           text=f"…y {len(lista) - maxn} ofertas más con cupón en esta hora. Míralas en el tablero.")
    log(f"  alertas enviadas: {enviadas} de {len(lista)}")
    return enviadas


# ---------------------------------------------------------------- archivos
def leer_json(p: Path, defecto):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return defecto


def escribir_json(p: Path, obj, compacto=False):
    p.parent.mkdir(parents=True, exist_ok=True)
    if compacto and isinstance(obj, dict) and "ofertas" in obj:
        cab = {k: v for k, v in obj.items() if k != "ofertas"}
        s = json.dumps(cab, ensure_ascii=False)[:-1]
        s += (', ' if cab else '') + '"ofertas": [\n' + ",\n".join(json.dumps(o, ensure_ascii=False) for o in obj["ofertas"]) + "\n]}\n"
        p.write_text(s, encoding="utf-8")
    else:
        p.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main():
    cfg = leer_json(BASE / "config.json", {})
    canales = cfg.get("canales", ["DescuentosHome", "DescuentosTech"])
    reglas = cfg.get("alertas", {})
    estado = leer_json(DATA / "estado.json", {})
    ultimos = estado.setdefault("ultimo_id", {})
    ahora = datetime.now(TZ)
    primera_vez = not ultimos
    desde = ahora - timedelta(days=int(cfg.get("dias_backfill", 2)) if primera_vez else 4)

    nuevas, errores = [], []
    sesion = requests.Session()
    for canal in canales:
        try:
            msgs = leer_canal(canal, int(ultimos.get(canal, 0)), desde)
        except Exception as e:
            errores.append(f"{canal}: {e}")
            log("  error", canal, e)
            continue
        for m in msgs:
            resolver_amazon(m, sesion)
        if msgs:
            ultimos[canal] = max(ultimos.get(canal, 0), max(m["num"] for m in msgs))
        nuevas.extend(msgs)

    # guardar por día
    por_dia: dict[str, list] = {}
    for o in nuevas:
        por_dia.setdefault(o["fecha"], []).append(o)
    for dia, lista in por_dia.items():
        p = DIAS / f"{dia}.json"
        prev = leer_json(p, {"fecha": dia, "ofertas": []})
        idx = {o["id"]: o for o in prev.get("ofertas", [])}
        for o in lista:
            idx[o["id"]] = o
        ofertas = sorted(idx.values(), key=lambda o: o["ts"], reverse=True)
        escribir_json(p, {"fecha": dia, "total": len(ofertas),
                          "con_cupon": sum(1 for o in ofertas if o.get("tipo_cupon")), "ofertas": ofertas}, compacto=True)

    # manifest
    dias = sorted((f.stem for f in DIAS.glob("*.json")), reverse=True)
    keep = int(cfg.get("dias_guardados", 120))
    for viejo in dias[keep:]:
        (DIAS / f"{viejo}.json").unlink(missing_ok=True)
    dias = dias[:keep]
    resumen = {}
    for d in dias[:7]:
        j = leer_json(DIAS / f"{d}.json", {})
        resumen[d] = {"total": j.get("total", 0), "con_cupon": j.get("con_cupon", 0)}
    escribir_json(DATA / "manifest.json", {
        "actualizado": ahora.isoformat(timespec="seconds"),
        "hoy": ahora.date().isoformat(),
        "canales": canales,
        "dias": dias,
        "resumen": resumen,
        "errores": errores,
    })

    # alertas (en la primera corrida solo lo de las últimas 2 horas para no inundar)
    para_alertar = nuevas
    if primera_vez:
        lim = ahora - timedelta(hours=2)
        para_alertar = [o for o in nuevas if datetime.fromisoformat(o["ts"]) >= lim]
    try:
        n = enviar_alertas(para_alertar, estado, reglas)
    except Exception as e:
        n = 0
        errores.append(f"alertas: {e}")
        log("  error alertas", e)

    estado["ultima_ejecucion"] = {"fecha": ahora.isoformat(timespec="seconds"), "nuevas": len(nuevas),
                                  "alertas": n, "errores": errores}
    escribir_json(DATA / "estado.json", estado)
    log(f"Listo: {len(nuevas)} ofertas nuevas, {n} alertas, {len(errores)} errores")
    if errores and not nuevas:
        sys.exit(1)


if __name__ == "__main__":
    main()
