# memory.md — Agente de apartamentos para rentas cortas

Memoria del agente diario que busca apartamentos o casas en ARRIENDO en Manizales donde el edificio o la casa permita alquilar por plataformas (Airbnb, Booking).
El agente la lee al empezar cada ejecución y la edita al final si aprendió algo nuevo.
Alejo puede corregir el agente respondiendo al correo diario, con notas en la página o editando este archivo a mano.

## Decisiones (de Alejo)
- 2026-11-10: Objetivo: arrendar apartamentos (o casas) en Manizales para subarrendar por plataformas de rentas cortas.
- 2026-11-10: Requisito clave: el edificio (reglamento de propiedad horizontal) o la casa debe PERMITIR rentas cortas. Si el anuncio lo dice explícitamente ("apto Airbnb", "permite rentas cortas", "apartamento turístico", "se permite alquiler por días") → rentas_cortas = "permitidas". Si no lo dice pero es casa independiente sin propiedad horizontal, o edificio de apartamentos turísticos/amoblados por días → "por confirmar". Si el anuncio lo prohíbe ("no se permite Airbnb", "solo vivienda familiar") → NO incluir. Apartamentos comunes en edificio que no dicen nada → NO incluir.
- 2026-11-10: Sin filtro de canon ni de habitaciones: traer todo y ordenarlo.
- 2026-11-10: Un correo propio por día (separado del de locales).

## Correcciones (de Alejo)
(ninguna todavía)

## Aprendizajes del agente
(fuentes que funcionan o bloquean, palabras clave que sirven, edificios que permiten o prohíben rentas cortas)
- 2026-11-11: Casi ningún anuncio de arriendo en Manizales menciona Airbnb/rentas cortas; buscar "airbnb" devuelve sobre todo anuncios de Airbnb (competencia). Lo más útil: listados de CASAS en Finca Raíz (/arriendo/casas/manizales/caldas/5-o-mas-habitaciones y /arriendo/casas/comuna-8-palogrande/manizales) y abrir cada ficha; palabras que sirven: "hostal", "uso comercial", "residencias estudiantiles", "anexo".
- 2026-11-11: Trovit sirve para listar (casas.trovit.com.co/arriendo-casa-amoblado-manizales-manizales) pero sus fichas /detail/ están bloqueadas por robots; buscar el original en Finca Raíz. Fichas de Finca Raíz y Metrocuadrado sí se leen (teléfono siempre oculto).
- 2026-11-11: Un apartaestudio amoblado cerca al Cable (Trovit) dice "también se alquila por noches, mínimo 3": excluido por ser competencia, pero indica que hay edificios cerca al Cable que toleran estadías cortas.
