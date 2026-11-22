# memory.md — Agente de locales para el segundo punto de dieta.

Memoria del agente diario que busca locales en arriendo en Manizales.
El agente la lee al empezar cada ejecución y la edita al final si aprendió algo nuevo.
Alejo puede corregir el agente respondiendo al correo diario, con notas en la página o editando este archivo a mano.

## Decisiones (de Alejo)
- 2026-11-08: Objetivo: arrendar un local en Manizales para un segundo punto de dieta. (panadería de amasijos + café de mostrador).
- 2026-11-08: Zonas: toda Manizales, con prioridad en Centro (le gustó un local en Cra 22 con Calle 22, edificio Banco de Bogotá) y en el corredor Cable / Milán / Palermo / Av. Santander. (Prioridades actualizadas el 2026-11-10, ver abajo.)
- 2026-11-10: ZONAS PRIORITARIAS según el análisis de geointeligencia (mapa: https://claude.ai/artifact/6ymLUJZSsgX5htA9PSzLjd). Se sigue buscando en toda Manizales, pero estas zonas van primero en la búsqueda, en "fit" y en los destacados, en este orden:
  1. Centro / San Joaquín (comuna Cumanday): barrios Centro, El Centro, San Joaquín, Fundadores, Los Agustinos, San Antonio, 20 de Julio, Buena Esperanza.
  2. Cervantes (comuna La Fuente): Cervantes, Uribe, Prado, Santa Helena, Fundadores.
  3. San Jorge / clúster de salud (comuna La Estación): San Jorge, La Argentina, El Sol, Lleras, Versalles, Santa Helena (cerca del Hospital de Caldas, Clínica de La Presentación, Hospital Infantil, Clínica Versalles).
  4. Chipre (comuna Atardeceres): Chipre, Campohermoso (cerca de la Universidad de Manizales).
  5. La Enea (comuna Tesorito): La Enea, San Marcel.
  Un local en una de estas zonas sube un nivel de "fit" (bajo→medio, medio→alto) si cumple lo demás (primer piso, frente a calle, ≤70 m²). En destacados, di en "por" a qué zona prioritaria pertenece. El corredor Cable / Milán / Palermo / Palogrande queda a menos de 1 km del primer local: sigue entrando, pero ya no es prioritario.
- 2026-11-08: Sin filtro de canon: traer todo y ordenarlo.
- 2026-11-09: TAMAÑO MÁXIMO 70 m² (reemplaza "sin filtro de tamaño"). No registres como nuevos ni destaques locales de más de 70 m². Si el anuncio no dice m², inclúyelo con m2 null. Si ya está en la base y mide más de 70, ignóralo (no lo pongas en "vistos" ni "cambios") salvo que esté marcado en estado.json.
- 2026-11-08: Facebook Marketplace: solo lo público que aparezca en buscadores; sin iniciar sesión.
- 2026-11-08: Enviar solo locales que no se hayan enviado antes.
- 2026-11-08: Detectar si el mismo local lo ofrecen varias inmobiliarias y comparar precios entre ellas.
- 2026-11-08: Verificar la dirección de cada local y poner un enlace a Google Maps.
- 2026-11-09: El reporte completo vive en la página (https://claude.ai/artifact/PvV3LaRSGhfacviVvuWqg4); el correo diario es corto, con botón a la página y destacados.
- 2026-11-09: Contacto con inmobiliarias: cuando Alejo marca un local como "contactar" en la página, el agente ENVÍA AUTOMÁTICAMENTE (en la corrida de las 8:40) un correo desde su Gmail a la inmobiliaria con la plantilla aprobada de abajo. Lo que Alejo marca a mano manda, aunque pase de 70 m². WhatsApp no es automático: la página muestra un botón con el mensaje listo y Alejo lo envía.
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
- 2026-11-09: Método eficiente: WebFetch de /arriendo/locales/manizales/caldas/pagina1..20 (21 tarjetas/pág., 416 resultados, ~334 URLs únicas por solapes) pidiendo una línea por tarjeta en formato pipe; Ciencuadras por barrio (Chipre, Alta Suiza, Belén, San José, San Antonio). Excluir Villamaría (otro municipio) y URLs oficina-en-arriendo. Finca Raíz permite filtrar por área en la URL de búsqueda: úsalo para traer solo hasta 70 m² si funciona.
- 2026-11-09: Formato de datos: la base de 317 locales (al 2026-11-09) viaja con la página; cada día solo se escribe data/dias/<fecha>.json + indice.json + manifest.json. NUNCA reescribir la base completa (create_or_update_file no aguanta ~420 KB). data/locales.json ya no existe.
- 2026-11-10: Correos de inmobiliarias (de sus perfiles en Finca Raíz o sitio oficial): Millán & Asociados arrendamientos@millanenlinea.com · Vista mercadeo@vistainmo.com · Hazul comercial@hazulinmobiliaria.com (WA 300 814 4425) · Villegas Ocampo comercial@vopropiedadraiz.co (319 235 4151) · AF Capital/Capital Inmobiliario capitalinmobiliariomanizales@gmail.com (318 658 5089) · Lucía Prada administrador@inmobiliarialuciaprada.com (320 726 9451) · Visión & Asesoría vasesoriainmobiliaria@gmail.com · Brando y Cía: sin correo. Faltan: Jorge Giraldo & Cia, Infibank Inmobiliaria.
- 2026-11-10: Los "No indica" de Finca Raíz se identifican abriendo el anuncio ("Publicado por"); de 26 marcados "contactar", la mayoría son de MILLAN & ASOCIADOS (también Jorge Giraldo & Cia: 193369407, 194221131, 191387148; Infibank: 192326547, 194441881). Ciencuadras por barrio: ciencuadras.com/arriendo/manizales/local/<barrio>.
- 2026-11-10: Envío a inmobiliarias: en la corrida programada el control de permisos de la sesión bloqueó 2 de 3 correos (solo salió AF Capital por 194135898). Cola pendiente: los demás locales "contactar" sin entrada "enviado"/"sin_correo" en contactos.json; reintentar ≤10/día.
- 2026-11-10: En las zonas prioritarias con poca oferta (Cervantes, San Jorge, Chipre, La Enea) busca también por barrio: Ciencuadras (ciencuadras.com/arriendo/manizales/local/<barrio>) y Finca Raíz (/arriendo/locales/<barrio>/zona-2-sur/manizales); confirma la URL antes de dar por vacío un barrio.
- 2026-11-11: Gmail send_message a inmobiliarias volvió a ser bloqueado (clasificador "Real-World Transactions"); el correo a Alejo sí sale. Plan B usado: create_draft con la plantilla y registro en contactos.json con estado "error" + "draft_id". Si una entrada ya tiene draft_id para ese local/inmobiliaria, NO crear otro borrador; solo revisar si Alejo lo envió (search in:sent) y pasarla a "enviado" con thread_id.
- 2026-11-11: Ya identificados como MILLAN (Finca Raíz): 194145749, 194013088, 193690898, 194456627, 193689327, 194479954, 194058006, 193302178, 194358924, 193938737. Cola "contactar" pendiente (sin borrador): 194058006, 192326547 (Infibank), 193369407 y 191387148 (J. Giraldo), 194059768, 193665298, Palermo (6), Palogrande 194006958, Av. Santander (4), La Estrella (2), Belén 193557563, Rambla, Viveros, Vélez.
- 2026-11-11: Ciencuadras /local/centro trae muchos de Gómez Chaljubb y Brando y Cía que no salen en Finca Raíz (su dirección en el anuncio es la de la oficina, no la del local). Sacatín Viejo = Villamaría (excluir). Finca Raíz /arriendo/locales/chipre/zona-2-sur/manizales redirige a Rionegro (no sirve); /la-enea/zona-2-sur/manizales sí funciona.
- 2026-11-12: send_message bloqueado por 3.ª vez (no reintentar más de 1 vez por corrida); 10 borradores nuevos. También MILLAN: 194058010, 194007029, 194006976, 194062509, 194400178, 194006958, 193847024, 193557563, 193532462; Vista: 194470352. Cola pendiente: 192326547 y 194441881 (Infibank), 193369407 y 191387148 (J. Giraldo), 194221131, 194059768, 193665298, 193311952, 194516137, 194073873, Rambla 3402408, Viveros 3342665, Vélez 3640917.
- 2026-11-12: Finca Raíz ordena por "popularidad": los anuncios nuevos (IDs altos) aparecen dispersos; filtra por ID ≥ al máximo del índice al recorrer págs. 7–20 para ahorrar contexto. /arriendo/locales/san-jorge/zona-2-sur/manizales redirige a Girón (no sirve); /cervantes/zona-2-sur/manizales devuelve mezcla de toda la ciudad. Gómez Chaljubb en Ciencuadras no publica teléfono ni correo.
- 2026-11-14: send_message volvió a funcionar en la corrida programada (10 correos). Para los borradores pendientes usa send_message con draftId (envía el MISMO borrador, sin duplicar) y registra "enviado" con su thread_id. Quedan 15 borradores (Millán y Vista) del 11 y 12-nov: enviarlos ≤10/día.
- 2026-11-14: Sin correo público (registrados "sin_correo"): Gómez Chaljubb (Ciencuadras, solo formulario), Infibank, Jorge Giraldo & Cia, Giraldo Castaño y STAR Inmobiliaria (WA 314 801 4286, sale en la meta descripción del anuncio en Ciencuadras).
- 2026-11-14: Ciencuadras a veces muestra en la tarjeta canon + administración (La Asunción: 1.200.000 + 80.000 = 1.280.000); abre el anuncio antes de registrar un cambio de precio.
- 2026-11-15: NO filtrar por ID ≥ máximo del índice: al recorrer las 20 págs. completas salieron 17 anuncios ≤70 m² con IDs viejos que nunca entraron a la base (15 nuevos + 2 ofertas). Compara cada tarjeta por ID contra el índice (raw.githubusercontent.com del repo público sirve para bajar indice.json/contactos.json a disco y comparar con Python).
- 2026-11-15: Se enviaron 10 borradores con draftId (send_message funcionó). Quedan 5 borradores: 194400178, 194006958, 194470352 (Vista), 193847024, 193557563. Anunciantes nuevos vistos: Guzmán Grupo Inmobiliario (San Jorge), Providencia Inmobiliaria (Metrocuadrado), Inmobiliaria Manizales (C.C. Parque Caldas); sin correo buscado aún.
- 2026-11-16: Se enviaron con draftId los 5 últimos borradores (194400178, 194006958, 194470352 Vista, 193847024, 193557563): ya no queda ningún borrador ni local "contactar" pendiente. Anunciante nuevo: F&F Inmobiliaria S.A.S. (Ciencuadras, oficina Cra 23 #56-87 local 105; correo no buscado aún). Brando y Cía también publica en Campo Hermoso.
- 2026-11-16: La tarjeta del listado de Finca Raíz puede traer un canon distinto al del anuncio (194526915: tarjeta $1.800.000, anuncio $1.700.000): abre el anuncio antes de registrar un cambio de precio. Ciencuadras: las tarjetas suman canon + administración (Campo Hermoso 2.612.000 = 2.500.000 + 112.000; Los Rosales 5.376.000 = 5.338.000 + 38.000).
- 2026-11-16: Excluidos por criterio (no registrar): 194246377 Estrella 40 m² en piso 3 (Millán) y 193999285 (Villamaría).
- 2026-11-19: El indice.json del 18-nov no se había subido (faltaban sus 4 nuevos); se corrigió. Antes de clasificar, cruza también los "nuevos"/"cambios" de los últimos dias/*.json contra el índice. Archivos grandes (indice ~52 KB, contactos ~29 KB): genera el JSON en disco con Python y delega su subida a un subagente que lo copie tal cual; verifica con raw.githubusercontent.com/<commit>/... (cmp). La API REST de GitHub vía curl/gh está bloqueada en corridas programadas; solo sirve el MCP.
- 2026-11-19: Finca Raíz /arriendo/locales/chipre/zona-1-norte/manizales SÍ funciona (3 anuncios). Millán responde primero con acuse automático desde servicioalcliente@millanenlinea.com ("asignada al área comercial"). Metrocuadrado 778-M6137331 (Millán, 50 m², $2.200.000) = 194058094. Anuncios de Grupo República (Cervantes 3490218/3490219) y Castro Rosero (Centro 3150838/3058951/3059070) en Ciencuadras: retirados.
- 2026-11-20: Metrocuadrado Centro que salen en buscador y no están en el índice porque miden >70 m² (no reabrir): M6298503 (Providencia 120), M5671263 (590), M5832424 (250), M6619367 (450, 2.º piso), M6725798 (294); M5601761 da 404. Tarjetas de Finca Raíz con canon distinto al índice hoy (194526915, Ciencuadras 3525453/3945538/3946130) son los casos tarjeta≠anuncio ya conocidos: no son cambios.
- 2026-11-22: Ciencuadras listado general: solo ?page=2 trae tarjetas distintas; ?page=3..7 y /pagina-N repiten la misma página, y las tarjetas de la grilla no traen m²/precio (salen del bloque "destacados"). Para cubrir más, ir por barrio. Particular nuevo en Ciencuadras: Leidy Viviana Ríos Zuluaga (Guayacanes 3534746, probable mismo local que 194487811).
