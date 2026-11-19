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
- 2026-11-14: La búsqueda "fincaraiz hotel venta Manizales registro nacional de turismo" y el listado /venta/edificios/lleras/manizales sacan hoteles (Millán & Asociados publica varios). Fincas-hotel rurales con RNT (La Linda, Quiebra de Vélez) se incluyen con fit "bajo"; la finca-hotel de El Remanso (AF Capital, 193689465, sin RNT, a 30 min) se dejó fuera.
- 2026-11-14: El hotel de 21 habitaciones con RNT en Av. Santander/Las Camelias (Lucia Prada: FR 10693854, Ciencuadras 3682515) está retirado en ambos portales: no incluir salvo que reaparezca activo.
- 2026-11-15: Revisados y descartados por no mencionar rentas cortas (edificios/casas "de rentas" con arriendo tradicional): edificio Milán Vista 194444637, casa El Bosque Lucia Prada 193084808, casa Las Delicias Hazul 193904697 (14 apartaestudios), apartaestudio Milán Vista 193333586. El ex-hotel de Las Camelias en Ciencuadras 3403755 (Castro Rosero) está retirado.
- 2026-11-15: La búsqueda "fincaraiz venta Manizales hostal hotel apartamentos turísticos RNT" sacó la casa del Centro 194372811 ("2 apartamentos generan renta como airbnb").
- 2026-11-16: Revisados y descartados (no mencionan rentas cortas o retirados): apartaestudios FR 193874500 Milán (retirado, arrendado largo plazo), 194046201 Av. Santander ("ideal para inversión" genérico), 194060297 Campohermoso; apto 193839367 y 193738907; 192994809 Palermo amoblado (retirado); Ciencuadras 3802149 Los Rosales (retirado). FR 192579738 Saenz, 191506309 y 191489004 dan error al abrir.
- 2026-11-17: Revisados y descartados (no mencionan rentas cortas o retirados): FR 194535348 Alta Leonora, 194274650 apartaestudio Av. Paralela, 191245473 Cable (renta tradicional), 194063285 Palermo; Metrocuadrado 19982-M6095917 apartaestudio Chipre, 21612-M6242591 Centro, 21639-M6307422 La Sultana (retirado); Ciencuadras 3821451 Los Agustinos (retirado); proyecto Torre Vita (Olize, Versalles, unidades 26-70 m², sin mención de renta corta, retirado en Ciencuadras). Nuroa da error.
- 2026-11-18: Revisados y descartados (sin mención de rentas cortas): Metrocuadrado 2147-M6654148 El Trébol 1h 59 m² $480M; FR 193440423 Milán 3h; edificios Lleras FR 193301966 La Cabaña y 193311356 Vélez; proyectos Milán 170 (CAMU, sin unidades publicadas) y Trébol 81 (LF Salazar, retirado en Ciencuadras). Las búsquedas con frases exactas ("se renta por plataformas", "apto para airbnb") solo devuelven anuncios de Airbnb.
- 2026-11-19: Revisados y descartados (sin mención de rentas cortas o retirados): FR 194055952 Av. Kevin Ángel (retirado), 192744523 La Linda 2h, 193739550 Los Cámbulos 2h; Ciencuadras 3297504 Los Cámbulos (retirado), 3915073 (ficha vacía). Edificios Vista sin señales de turismo: 191539172/192525636 Palermo, 191536758 Av. Santander, 192273610 y 192338823 Centro, 192142439 La Arboleda. Trovit loft-amoblado-manizales p1: 30 avisos, ninguno menciona renta corta.
