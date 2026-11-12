# memory.md — Agente de apartamentos para rentas cortas (COMPRA)

Memoria del agente diario que busca apartamentos (o casas) EN VENTA en Manizales donde el edificio o la casa permita alquilar por plataformas de rentas cortas (Airbnb, Booking).
El agente la lee al empezar cada ejecución y la edita al final si aprendió algo nuevo.
Alejo puede corregir el agente respondiendo al correo diario, con notas en la página o editando este archivo a mano.

## Decisiones (de Alejo)
- 2026-11-10: Objetivo: COMPRAR apartamentos (o casas) en Manizales para ponerlos en plataformas de rentas cortas. (Corrección del 2026-11-10: NO es arriendo; la primera búsqueda en arriendo se borró.)
- 2026-11-10: Requisito clave: el edificio (reglamento de propiedad horizontal) o la casa debe PERMITIR rentas cortas. Si el anuncio lo dice explícitamente ("apto Airbnb", "permite rentas cortas", "apartamento turístico", "ideal para inversión en Airbnb", "se permite alquiler por días", "con RNT") → rentas_cortas = "permitidas". Si no lo dice pero es casa independiente sin propiedad horizontal, o edificio de apartamentos turísticos/amoblados por días → "por confirmar". Si el anuncio lo prohíbe ("no se permite Airbnb", "solo vivienda familiar") → NO incluir. Apartamentos comunes en edificio que no dicen nada → NO incluir.
- 2026-11-10: Sin tope de precio ni de habitaciones por ahora: traer todo y ordenarlo.
- 2026-11-10: Un correo propio por día (separado del de locales).

## Correcciones (de Alejo)
- 2026-11-10: Los apartamentos son para COMPRA, no para arriendo.

## Aprendizajes del agente
(fuentes que funcionan o bloquean, palabras clave que sirven, edificios que permiten o prohíben rentas cortas)
- 2026-11-11: Trovit sirve para listar, pero sus fichas /detail/ están bloqueadas por robots; buscar el original en Finca Raíz. Fichas de Finca Raíz y Metrocuadrado sí se leen (teléfono siempre oculto).
- 2026-11-11: Muchos inmuebles salen duplicados con 2 inmobiliarias (Vista/Hazul, Lucia Prada/Millán): agrupar como un inmueble con varias ofertas.
- 2026-11-11: Buscar "airbnb" devuelve sobre todo anuncios de Airbnb (competencia, no venta): mejor usar listados de venta de Finca Raíz/Metrocuadrado por barrio y abrir cada ficha buscando las señales de rentas cortas.
- 2026-11-11 (venta): casi ningún anuncio de venta dice "Airbnb"; las señales reales fueron "se renta por plataformas virtuales" y edificios/hoteles en venta. Los listados Trovit apartamento-amoblado-manizales y penthouse-amoblado-manizales (páginas 1-5) traen fragmentos de descripción útiles; Ciencuadras sí muestra la ficha completa.
- 2026-11-11: Fichas de Finca Raíz con "[No disponible]" en el título están retiradas: no incluir. Edificios/hoteles se guardan con tipo_inmueble "casa" y la aclaración "EDIFICIO" en instalaciones.
- 2026-11-12: El listado de edificios en venta de Vista Inmobiliaria en Finca Raíz (/inmobiliarias/vista-inmobiliaria/174674501/venta/edificios/manizales/caldas) trae hostels y hoteles; revisarlo cada día. Las fichas de Ciencuadras de apartaestudios y edificios suelen salir "ya no está disponible": verificar siempre.
- 2026-11-12: estrenarvivienda.com/renta-corta no tiene proyectos en Manizales (solo Santa Marta, Bogotá, Armenia…). Un hostel sin "en funcionamiento" ni RNT → "por confirmar".
