# memory.md — Rastreador de ofertas en Amazon

Memoria del agente que revisa cada 4 horas cupones, códigos y bajadas de precio en Amazon.com (y en dos grupos de Telegram) para 4 productos.
El agente la lee al empezar cada ejecución y la edita al final si aprendió algo nuevo.
Alejo puede corregirlo editando este archivo a mano o diciéndoselo a Claude.

## Decisiones (de Alejo)
- 2026-11-17: Productos y precios de referencia:
  1. Etiquetas Rongta R22, 2"×1.18" (50×30 mm), 260 etiquetas — ref. B0F5VG2KQG, $9.99. Vale cualquier marca compatible del mismo tamaño.
  2. Soplador de aire inalámbrico eléctrico para teclado — ref. B0995W447Y (Koonie), $29.99. Vale cualquier marca similar (no latas de aire comprimido).
  3. Colgate Sensitive Enamel Health, 3 × 6 oz — B0795S9XRB, $14.88. Exactamente ese producto; otro paquete solo si el precio por onza es menor.
  4. Dove Beauty Bar Cool Moisture Cucumber & Green Tea, 6 × 3.75 oz — B0016FWFDI, $15.49. Mismo aroma; otro paquete solo si el precio por barra es menor.
- 2026-11-17: Solo leer páginas: nunca comprar, agregar al carrito, aplicar códigos en el checkout, iniciar sesión ni escribir/reaccionar en Telegram.
- 2026-11-17: Avisar solo ofertas nuevas o cuyo precio final bajó más que lo ya avisado. Sin ofertas nuevas = una línea, sin ruido.
- 2026-11-19: El estado de ofertas avisadas vive en GitHub (`rastreador-ofertas/data/estado.json`), ya no en Google Drive.

## Correcciones (de Alejo)
(ninguna todavía)

## Aprendizajes del agente
- 2026-11-19: La corrida de las 6:08 a. m. (Bogotá) no tuvo Claude in Chrome disponible (Chrome cerrado o extensión inactiva). Si pasa, reportarlo en una línea y no intentar otra vía de navegación.
