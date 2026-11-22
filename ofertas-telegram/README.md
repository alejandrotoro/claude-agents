# ofertas-telegram

Tu propio "grupo de ofertas": cada hora GitHub Actions lee la vista pública de los canales de Telegram de `config.json`
(hoy `t.me/s/DescuentosHome` y `t.me/s/DescuentosTech`), guarda cada oferta por día y te avisa por un bot de Telegram
las que traen código o cupón. El tablero (página de Claude) lee estos archivos.

## Archivos
- `scraper.py` — lector y alertas (solo lee la vista pública; no inicia sesión ni escribe en los canales).
- `config.json` — canales y reglas de alerta (`min_descuento`, `categorias_excluidas`, `solo_categorias`, `tiendas`, `palabras_excluidas`, `max_por_corrida`).
- `data/dias/AAAA-MM-DD.json` — ofertas del día (hora de Bogotá), una por línea.
- `data/manifest.json` — días disponibles y resumen; `data/estado.json` — último mensaje leído por canal y chat del bot.
- Workflow: `.github/workflows/ofertas-telegram.yml` (cada hora, minuto 7 UTC; también se puede correr a mano en *Actions → ofertas-telegram → Run workflow*).

## Activar el bot (una sola vez)
1. En Telegram abre **@BotFather** → `/newbot` → ponle nombre → copia el token.
2. En GitHub: repo `claude-agents` → *Settings → Secrets and variables → Actions → New repository secret* → nombre `TELEGRAM_BOT_TOKEN`, valor el token.
3. Abre tu bot en Telegram y escríbele `/start`. En la siguiente corrida queda enlazado y te manda "✅ Listo".

Costo: GitHub Actions gratis (repos privados tienen 2.000 min/mes; esto usa ~750).
