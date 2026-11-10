# memory.md — Agente de locales para el segundo punto de dieta.

Memoria del agente diario que busca locales en arriendo en Manizales.
El agente la lee al empezar cada ejecución y la edita al final si aprendió algo nuevo.
Alejo puede corregir el agente respondiendo al correo diario, con notas en la página o editando este archivo a mano.

## Decisiones (de Alejo)
- 2026-11-08: Objetivo: arrendar un local en Manizales para un segundo punto de dieta. (panadería de amasijos + café de mostrador).
- 2026-11-08: Zonas: toda Manizales, con prioridad en Centro (le gustó un local en Cra 22 con Calle 22, edificio Banco de Bogotá) y en el corredor Cable / Milán / Palermo / Av. Santander.
- 2026-11-08: Sin filtro de canon ni de tamaño: traer todo y ordenarlo.
- 2026-11-08: Facebook Marketplace: solo lo público que aparezca en buscadores; sin iniciar sesión.
- 2026-11-08: Enviar solo locales que no se hayan enviado antes.
- 2026-11-08: Detectar si el mismo local lo ofrecen varias inmobiliarias y comparar precios entre ellas.
- 2026-11-08: Verificar la dirección de cada local y poner un enlace a Google Maps.
- 2026-11-09: El reporte completo vive en la página (https://claude.ai/artifact/PvV3LaRSGhfacviVvuWqg4); el correo diario es corto, con botón a la página y destacados.
- 2026-11-09: Contacto con inmobiliarias: cuando Alejo marca un local como "contactar" en la página, el agente ENVÍA AUTOMÁTICAMENTE (en la corrida de las 8:40) un correo desde su Gmail a la inmobiliaria con la plantilla aprobada de abajo. WhatsApp no es automático: la página muestra un botón con el mensaje listo y Alejo lo envía.
- 2026-11-09: Número de contacto para las inmobiliarias: WhatsApp 310 597 9727, SOLO WhatsApp (no llamadas). No usar el 315 050 7179 en mensajes a inmobiliarias.
- 2026-11-09: Plantilla de correo aprobada por Alejo (no cambiarla sin que él lo pida):
  Asunto: Interés en local en arriendo – {dirección/barrio}, {m2} m²
  Cuerpo:
  Buenos días,

  Mi nombre es Alejandro Toro, de dieta., una panadería de amasijos y café en Manizales. Vi el local publicado en {portal} ({enlace}) con canon de {canon} y me interesa para un segundo punto.

  Quisiera confirmar:
  1. Si sigue disponible y desde cuándo.
  2. Canon y administración finales, y requisitos (codeudor, póliza, depósito).
  3. Si el uso de suelo permite panadería/cafetería con horno eléctrico.
  4. Disponibilidad para visitarlo esta semana.

  Quedo atento por este medio o por WhatsApp al 310 597 9727 (solo WhatsApp, por favor no llamadas).

  Gracias,
  Alejandro Toro
  dieta. · @dieta_mzls

## Correcciones (de Alejo, en respuestas al correo o notas en la página)
(ninguna todavía)

## Locales descartados por Alejo (no volver a enviar)
(se marcan desde la página en data/estado.json)

## Aprendizajes del agente
(fuentes que funcionan o bloquean, trucos de búsqueda, formatos de dirección, etc.)
- 2026-11-08: Finca Raíz es la fuente principal. Listados útiles: /arriendo/locales/cable/zona-2-sur/manizales (y /paginaN, ~109 resultados, cubre todo el corredor sur) y /arriendo/locales/palermo/zona-2-sur/manizales/paginaN. /arriendo/locales/centro/manizales NO sirve (redirige a Barranquilla). Un anuncio retirado de Finca Raíz redirige a una búsqueda nacional; en Ciencuadras dice "ya no está disponible". Metrocuadrado y Ciencuadras funcionan; Properati/MercadoLibre/OLX/Facebook no salen en buscador.
- 2026-11-08: Casi ningún anuncio publica dirección exacta (solo barrio/vía) → casi todo queda "Aproximada". Vista, Hazul y Visión & Asesoría publican el mismo local con IDs consecutivos; Vista a veces duplica su propio anuncio.
- 2026-11-08: Hazul a veces publica como "canon" el total canon + IVA 19% + administración (ej. Multicentro Estrella 186 m²: $16.454.000 vs $12.000.000 de Villegas Ocampo). Antes de marcar diferencia de precio, revisar si es IVA/admin.
- 2026-11-08: Para el Centro, Metrocuadrado es mejor que Finca Raíz (casi todo de Millán & Asociados; un retirado da 404 "no está disponible").
- 2026-11-08: El local de Milán a $5.300.000 (82–85 m²) aparece publicado por Millán & Asociados, AF Capital, Vista y Hazul; el título y la descripción a veces difieren en m² y barrio.
- 2026-11-09: Listado del Centro en Finca Raíz que SÍ funciona: /arriendo/locales/el-centro/zona-2-sur/manizales (+ /pagina2..5, ~100 anuncios; la paginación se solapa). También /arriendo/locales/versalles/zona-2-sur/manizales (2 págs.) y /arriendo/locales/manizales/caldas (~400, 20 págs.). El listado de Metrocuadrado no carga sin navegador; los anuncios de Ciencuadras/Finca Raíz que salen en el buscador suelen estar retirados → mejor ir por listados.
- 2026-11-09: Millán & Asociados publica en Metrocuadrado con IVA incluido y el mismo local aparece en Finca Raíz sin IVA (factor exacto 1,19, misma admin): no es diferencia de precio real.
- 2026-11-09: Método eficiente: WebFetch de /arriendo/locales/manizales/caldas/pagina1..20 (21 tarjetas/pág., 416 resultados, ~334 URLs únicas por solapes) pidiendo una línea por tarjeta en formato pipe; Ciencuadras por barrio (Chipre, Alta Suiza, Belén, San José, San Antonio). Excluir Villamaría (otro municipio) y URLs oficina-en-arriendo.
- 2026-11-09: Formato de datos: la base de 317 locales (al 2026-11-09) viaja con la página; cada día solo se escribe data/dias/<fecha>.json + indice.json + manifest.json. NUNCA reescribir la base completa (create_or_update_file no aguanta ~420 KB). data/locales.json ya no existe.
