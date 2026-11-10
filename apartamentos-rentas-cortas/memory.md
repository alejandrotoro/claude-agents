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
