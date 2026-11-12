# memory.md — Agente de fincas y lotes cerca de Manizales

Memoria del agente diario que busca fincas y lotes construibles EN VENTA cerca de Manizales.
El agente la lee al empezar cada ejecución y la edita al final si aprendió algo nuevo.
Alejo puede corregir el agente respondiendo al correo diario, con notas en la página o editando este archivo a mano.

## Decisiones (de Alejo)
- 2026-11-10: Objetivo: comprar una finca o un lote construible cerca de Manizales.
- 2026-11-10: Presupuesto: finca construida hasta $400.000.000; lote hasta $300.000.000. No incluir lo que pase de esos topes.
- 2026-11-10: Lotes: solo construibles (con uso de suelo, licencia o parcelación que permita construir vivienda). Si el anuncio no lo dice → construible = "por confirmar"; si dice que no se puede construir → NO incluir.
- 2026-11-10: Zonas: Santágueda / Palestina; Villamaría y Chinchiná (incl. veredas como La Florida, Gallinazo, Llanitos); Neira, Termales y vía al Magdalena; y en general cualquier sector a máx. ~45 min de Manizales.
- 2026-11-10: Un correo propio por día (separado del de locales).

## Correcciones (de Alejo)
(ninguna todavía)

## Aprendizajes del agente
(fuentes que funcionan o bloquean, veredas y precios de referencia, trucos de búsqueda)
- 2026-11-11: Finca Raíz, Ciencuadras y Metrocuadrado abren bien con WebFetch; Trovit sirve como listado (con precios) pero sus fichas /detail/ están bloqueadas por robots; Mitula no da URLs individuales. Los listados de Ciencuadras por sector (/venta/<municipio>/.../finca) permiten filtrar por precio rápido.
- 2026-11-11: Precios de referencia: fincas construidas en Santágueda, Neira y Villamaría casi todas > $480M (lo bajo el tope es raro); lotes en condominio Santágueda ~$250k/m² (1.050 m² a $262,5M), vía a Chinchiná ~$300k/m², La Cabaña (Manizales) ~$470k/m², Palestina–La Plata ~$110k/m².
- 2026-11-11: Inmobiliaria Lucia Prada publica decenas de lotes casi idénticos (mismo condominio, códigos distintos): agruparlos en un solo registro con varias ofertas.
- 2026-11-11: Mejor bolsa de lotes baratos: El Río / vereda Palermo (Neira) y Km 41, vía Manizales–Medellín (~40–45 min, cálido): ~$110–150k/m², lotes de 1.000–1.500 m² a $150–200M. Listados útiles en Finca Raíz: /venta/lotes/el-rio/neira, /venta/kilometro-41/manizales, /venta/lotes/la-muleta/palestina/pagina2, /venta/casas-campestres/neira/santagueda y /inmobiliarias/<inmobiliaria>/<id>/venta/lotes/<municipio>/caldas.
- 2026-11-11: El condominio de Lucia Prada "vía a Chinchiná" aparece en Finca Raíz como La Inquisición (Palestina) con IDs 19124xxxx → mismo registro chinchina-lote-840m2. Villamaría rural (Llanitos, El Pindo, Tejares) y Metrocuadrado: todo > $900M; lotes de Monserrate (Villamaría) son urbanos chicos, no aplican. Mercado Libre/Properati/OLX/Facebook no salen en el buscador; Cocampo.com abre bien.
- 2026-11-11: Si el archivo del día ya existe y es grande, escribir uno adicional dias/<hoy>-2.json (la página aplica en orden) en vez de reescribirlo. Ojo: Guzmán 194113640 (Santágueda 3.248 m²) muestra $90M pero el texto dice $900M → excluido.
- 2026-11-12: Villegas Ocampo publica muchos lotes de El Río/Km 41 con área "1 m²" (el área real está en la descripción): 1.074–1.086 m² → registro km41-lote-1074m2; 1.050 m² Km 47 → km41-lote-1050m2. Florida del Río P.H. (Palermo) tiene lotes con número propio (#49 = 1.185 m², $210M).
- 2026-11-12: El listado /venta/chinchina/caldas/pagina5 de Finca Raíz trae lotes baratos de Palestina (La Inquisición, a 2 km de Cameguadua, $220–280M). Fincas de Santágueda vistas hoy: todas $670M–$6.500M. Las fichas de Cocampo fallaron hoy (client_error).
