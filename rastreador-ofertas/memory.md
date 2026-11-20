# memory.md — Rastreador de ofertas en Amazon

Memoria del agente que revisa una vez al día (10:55 a. m., Bogotá) cupones, códigos y bajadas de precio en Amazon.com (y en dos grupos de Telegram) para 4 productos.
El agente la lee al empezar cada ejecución y la edita al final si aprendió algo nuevo.
Alejo puede corregirlo editando este archivo a mano o diciéndoselo a Claude.

## Decisiones (de Alejo)
- 2026-11-17: Productos y precios de referencia:
  1. Etiquetas Rongta R22, 2"×1.18" (50×30 mm), 260 etiquetas — ref. B0F5VG2KQG, $9.99. Vale cualquier marca compatible del mismo tamaño.
  2. Soplador de aire inalámbrico eléctrico para teclado — ref. B0995W447Y (Koonie), $29.99. Vale cualquier marca similar (no latas de aire comprimido).
  3. Colgate Sensitive Enamel Health, 3 × 6 oz — B0795S9XRB, $14.88. Exactamente ese producto; otro paquete solo si el precio por onza es menor.
  4. Dove Beauty Bar Cool Moisture Cucumber & Green Tea, 6 × 3.75 oz — B0016FWFDI. Mismo aroma; otro paquete solo si el precio por barra es menor. (Ver la corrección del 2026-11-20: umbral de $8.)
- 2026-11-17: Solo leer páginas: nunca comprar, agregar al carrito, aplicar códigos en el checkout, iniciar sesión ni escribir/reaccionar en Telegram.
- 2026-11-17: Avisar solo ofertas nuevas o cuyo precio final bajó más que lo ya avisado.
- 2026-11-19: El estado de ofertas avisadas vive en GitHub (`rastreador-ofertas/data/estado.json`), ya no en Google Drive.
- 2026-11-19: Corre una vez al día a las 10:55 a. m. (Bogotá), ya no cada 4 horas. En Telegram revisa las últimas ~24 horas.
- 2026-11-20: SIEMPRE enviar un correo a altose87@gmail.com con el resultado, haya o no ofertas (Gmail send_message). Asunto "Rastreador de ofertas Amazon – <AAAA-MM-DD> – <N ofertas nuevas | Sin ofertas nuevas>"; arriba la línea de estado, luego ofertas nuevas, una tabla "Estado de hoy" con los 4 productos (precio de la referencia, mejor precio, cupón) y el resultado de Telegram. Esto manda sobre cualquier instrucción de "una línea sin ruido".
- 2026-11-20: Fuentes adicionales en cada corrida (además de las páginas de Amazon y los dos grupos de Telegram):
  a) Vipon (https://www.vipon.com): buscar cada producto (p. ej. "Rongta R22 labels", "cordless air duster", "Colgate Sensitive Enamel", "Dove Cool Moisture"). Es donde los vendedores publican códigos de 50–99%; sirve sobre todo para etiquetas y soplador. Solo leer: si un código exige iniciar sesión o "reclamar", reportar el enlace de Vipon para que Alejo lo reclame, sin registrarse.
  b) Slickdeals (https://slickdeals.net/newsearch.php?q=<producto>): ofertas de Colgate y Dove (cupones, Subscribe & Save, bajadas de precio).
  c) Página de cupones de Amazon (https://www.amazon.com/coupons) buscando cada producto.
  En el correo, indicar la fuente de cada oferta.
- 2026-11-20: No tiene que ser del mismo vendedor al que Alejo ya le compró: vale cualquier vendedor y cualquier origen (otro vendedor en Amazon, un código de Vipon, Slickdeals, Telegram u otra tienda en línea de EE. UU.), siempre que sea el producto según las reglas de coincidencia de arriba. Si la oferta es de una tienda distinta a Amazon, decirlo claramente en el correo.

## Correcciones (de Alejo)
- 2026-11-20: Dove Cool Moisture (6 × 3.75 oz): $12 NO es oferta. Alejo lo vio antes a ~$3.50 el paquete. Solo cuenta como oferta si el precio final (con cupón/código) del paquete de 6 es ≤ $8 (≈ $1.33 por barra). Lo de más de $8 va solo en la tabla "Estado de hoy", sin marcarlo como oferta. El aviso de $12 del 2026-11-20 no cuenta como ya avisado.

## Aprendizajes del agente
- 2026-11-19: Las corridas de las 6:08 y 10:55 a. m. no tuvieron Claude in Chrome en la sesión. Chrome con la extensión debe estar abierto a la hora de la corrida; si no, reportarlo y no intentar otra vía.
- 2026-11-20: El Koonie de referencia (B0995W447Y) está "Currently unavailable"; para el soplador comparar con equivalentes de la búsqueda "cordless air duster keyboard" (ignorar los patrocinados). "Up to 6% off if you qualify" es una oferta de tarjeta, no un cupón.
- 2026-11-20: En Telegram Web los grupos abren en el último mensaje leído (puede ser de hace semanas): pulsar el botón de bajar al final del chat antes de leer. El grupo -1001609615707 es DescuentosTech y -1002051042540 es Descuentos Home.
- 2026-11-20: Cadena de los grupos: Telegram → publicación en Facebook → JoyLink → Amazon con etiqueta de afiliado (Descuentos Home usa tag=deshome1-20). Los códigos ("Aplicando cupón: XXXXXXXX", 8 caracteres, ~50%) son de vendedores chinos pequeños; "CLIP" = cupón para marcar en la página. Para Colgate/Dove casi nunca hay códigos: buscar cupones para marcar, Subscribe & Save o bajadas de precio.
