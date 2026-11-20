# memory.md — Buscador diario de ofertas de empleo (Alejo)

Memoria del agente que cada mañana busca ofertas de empleo serias que hagan match con el perfil de Alejo y se las envía por correo.
El agente la lee al empezar cada ejecución y la edita al final si aprendió algo durable.
Alejo puede corregirlo editando este archivo, respondiendo el correo diario o diciéndoselo a Claude.

## Perfil del candidato (fuente: CV 2026 de Alejo)
- Alejandro Toro — Senior Full-Stack Engineer | Technical Lead. Manizales, Colombia (UTC-5). Inglés profesional (EF SET C2), español nativo.
- 15+ años. Stack principal: **Ruby on Rails** (experto), **React**, **Next.js**, JavaScript/TypeScript, Redux, PostgreSQL, MySQL, MongoDB, Elasticsearch, REST APIs.
- Fortalezas diferenciales: modernización de sistemas legacy y upgrades grandes (Rails 2.2 → Rails 7 sin downtime; Ember → React; mantenimiento/deprecación de una app .NET de ~25 años), liderazgo técnico de equipos, ownership end-to-end (discovery → producción), debugging complejo, testing (Cypress), rendimiento.
- Dominios: SaaS, fintech/banca digital (Amount: lending, tarjetas, Rails Engines), edtech (PanOpen), geoespacial (Ginkgo: polígonos, venues), widgets embebibles para gimnasios/yoga (Playlist), reporting/Electron (Diana AI).
- Adicional: .NET (mantenimiento), React Native, Electron, Ionic, Titanium, Sinatra.
- Ha trabajado siempre para empresas de EE. UU. de forma remota desde Colombia.

## Decisiones (de Alejo)
- 2026-11-20: Objetivo: un **segundo empleo remoto** en paralelo al actual. La búsqueda es **discreta**: el agente SOLO lee y reporta. Nunca aplica, nunca escribe a empresas ni reclutadores, nunca crea cuentas ni inicia sesión.
- 2026-11-20: Correo diario SIEMPRE a altose87@gmail.com, haya o no ofertas nuevas.
- 2026-11-20: Excluir cualquier oferta de **Playlist** y de **Ginkgo** (sus empleadores actuales).
- 2026-11-20: Ya está en proceso con **Strider** (app.onstrider.com) y con **GreenLight / Anyone AI** (proyecto Nectarine): no reportarlos como novedad salvo una oferta concreta nueva.

## Reglas de match (salvo corrección de Alejo)
### Debe cumplir (si no, se descarta)
1. **Remoto 100 %** y elegible desde **Colombia** (Colombia, LATAM, "Americas", "anywhere/worldwide", o zona horaria compatible con UTC-5). Descartar "US only", "must be authorized to work in the US/EU", "Remote (US/Canada)", híbrido u on-site (salvo híbrido opcional en Manizales).
2. **Senior o superior**: Senior, Staff, Lead, Principal, Tech Lead, Engineering Lead. Descartar junior, mid/semi-senior e internships.
3. **Stack**: Ruby on Rails en el rol, o full-stack con React/Next.js + backend. Roles solo de frontend React/Next.js senior se aceptan con fit medio.
4. **Seria**: publicada por la empresa o un reclutador identificable, con descripción real. Descartar estafas (pagar por aplicar, entrevistas por Telegram/WhatsApp con desconocidos, "cheques" o equipos que hay que comprar), ofertas cerradas, y anuncios de más de 30 días sin actividad.

### Suma puntos (fit 0–100)
- Stack (máx. 40): Rails + React/Next.js = 40; Rails solo = 34; React/Next.js + otro backend (Node/TS) = 22; otro stack con Rails como "nice to have" = 15.
- Seniority/liderazgo (máx. 15): Tech Lead/Staff = 15; Senior = 12.
- Elegibilidad (máx. 15): dice Colombia o LATAM explícitamente = 15; "anywhere"/Americas = 12; ambiguo = 5.
- Compensación (máx. 10): pago en USD con rango publicado = 10; USD sin rango = 6; COP o sin dato = 2.
- Compatibilidad con segundo empleo (máx. 10): contractor/async/horario flexible = 10; full-time empleado con horario estándar EE. UU. = 6; exige exclusividad explícita o horario fijo con muchas reuniones = 2.
- Bonus (máx. 10): modernización legacy / upgrades de Rails, fintech, edtech, geoespacial, widgets/embebibles, SaaS B2B, .NET legacy + Rails, IA aplicada a producto.
- **Alto ≥ 75**, **Medio 60–74**, < 60 no se envía.

## Verificación de enlaces (OBLIGATORIA — corrección de Alejo 2026-11-20)
El primer correo traía enlaces rotos: los resultados de WebSearch y los agregadores conservan vacantes que ya cerraron. Una oferta SOLO se envía si pasa TODO esto:
1. **El enlace sale del tablero vivo de la empresa.** Para ATS (Greenhouse, Lever, Ashby, Workable, Teamtailor, careers-page), busca y abre primero la página RAÍZ del tablero (p. ej. `job-boards.greenhouse.io/nortal`, `jobs.lever.co/koombea`) y toma el enlace de la vacante SOLO si aparece en la lista actual. Si no aparece en la raíz → cerrada.
2. **WebFetch al enlace exacto que irá en el correo** (no a otra copia) con un prompt que pida: URL final después de redirecciones, título del puesto tal como aparece, si hay botón o formulario para aplicar ("Apply", "Apply for this job", "Postular"), y si aparece algún texto de cierre.
3. Se descarta como **CERRADA** si: la URL final cambió a la raíz del tablero, contiene `?error=true`, `/404` o `expired`; o el texto dice "no longer active", "no longer accepting applications", "position has been filled", "job not found", "Página no encontrada", "ya no está activa", "this job has expired", "closed"; o la página muestra solo una lista de otras vacantes; o no hay botón/formulario para aplicar.
4. **Agregadores** (Jobgether, Remote Rocketship, 4dayweek, Arc, Working Nomads, Built In, portfolio boards de VCs, etc.): no enviar su enlace si la vacante es de una empresa con tablero propio. Busca la misma vacante en el tablero de la empresa y verifica allí con los pasos 1–3. Solo si la empresa no tiene tablero propio se acepta el enlace del agregador, y únicamente si el agregador muestra fecha de publicación ≤ 14 días y botón de aplicar.
5. Si WebFetch falla o la respuesta es ambigua → NO se envía como oferta; va a una sección final "No pude verificar (revisa tú)" con máx. 3 entradas, sin contarla en el total.
6. En cada oferta enviada, escribe la línea "✅ Verificada abierta hoy: <evidencia corta, p. ej. 'botón Apply visible, aparece en jobs.lever.co/koombea'>".
Mejor 2 ofertas reales que 10 rotas.

## Fuentes (rotación)
WebFetch solo abre URLs que hayan salido en un WebSearch de esa misma corrida: primero busca, luego abre el enlace del resultado.
### Núcleo — TODOS los días
- ATS directos con `site:` (la mejor fuente: ofertas de la empresa misma):
  - `site:jobs.lever.co "Ruby on Rails" (Colombia OR LATAM OR "Latin America")`
  - `site:job-boards.greenhouse.io rails ("Latin America" OR Colombia OR LATAM)` y `site:boards.greenhouse.io rails LATAM`
  - `site:jobs.ashbyhq.com rails (LATAM OR Colombia OR Americas)`
  - `site:apply.workable.com "ruby on rails" remote LATAM`
  - `site:*.teamtailor.com "ruby on rails" LATAM`, `site:careers-page.com rails LATAM`
  - Variantes con "Next.js" y "React" + "Ruby" y con "Tech Lead"/"Staff".
- Agregadores remotos: We Work Remotely, Remote OK, Remotive, Himalayas, Working Nomads, Jobgether, Remote Rocketship, Built In (Colombia), Wellfound (lo público).
- Boards de Ruby/Rails: jobs.gorails.com, rubyonremote.com, rubyjobs.dev.
- Colombia/LATAM: Get on Board (getonbrd.com), LinkedIn Jobs (solo lo público vía buscador), Indeed Colombia, Jooble Colombia, elempleo, Computrabajo, Torre.
### Rotación por día de la semana (además del núcleo)
- Lunes: casas de software/nearshore A — Koombea, Ideaware, FullStack Labs, Truelogic, Blue Coding, Nearsure, Nortal.
- Martes: casas de software B — Zarego, ioet, Encora, CI&T, EX Squared, Monks, Imagemaker, Rootstrap, WyeWorks, Moove It, Codeminer42.
- Miércoles: marketplaces con vetting (pago USD) — Turing, Toptal, Arc.dev, Lemon.io, Revelo, Howdy, Terminal, Andela, Proxify, Index.dev, A.Team, Gun.io (reportar como "marketplace": requieren registro/vetting).
- Jueves: empresas de producto con Rails que contratan LATAM — Donorbox, Recurly (Medellín), Ridepanda, GitLab, Buk, Workana B2B, Amplemarket, Wonolo, y las que aparezcan en "Aprendizajes".
- Viernes: casas de software C — BairesDev (solo roles Senior/Lead de Ruby; sus avisos "evergreen" se repiten: reportar uno solo), Globant, Endava, Wizeline, Applaudo, Gorilla Logic, Jobsity, Scopic, MAS Global, Parrolabs, iDelsoft, Darwoft.
- Sábado: Hacker News "Who is hiring?" del mes (buscar Rails + remote + LATAM/anywhere) y newsletters (Ruby Weekly jobs).
- Domingo: solo núcleo.

## Correcciones (de Alejo)
- 2026-11-20: "La gran mayoría de los enlaces están rotos." → regla de verificación obligatoria (sección de arriba). Comprobado en Chrome: Nearsure 4801109007 y 4728428007 (tablero de Greenhouse de Nearsure inactivo), Nortal 5204946007 (ya no está en job-boards.greenhouse.io/nortal) y Nir Yu 8184302 ("This position is no longer active") estaban cerrados.
- 2026-11-20: Enviar UN SOLO correo por corrida (el 20-nov llegaron dos).

## Empresas descartadas (de Alejo)
(vacío)

## Aprendizajes del agente
- 2026-11-20: Muchas casas de software publican vacantes "de pipeline" (p. ej. Koombea: "applying does not guarantee immediate placement"). Reportarlas marcadas como "pipeline", con fit −5.
- 2026-11-20: Greenhouse redirige las vacantes cerradas a `job-boards.greenhouse.io/<empresa>?error=true` (o muestra "La bolsa de empleo que estabas viendo ya no está activa"); Teamtailor muestra "This position is no longer active" con otras vacantes debajo.
- 2026-11-20: Nearsure parece haber dejado su tablero de Greenhouse: buscar su página de empleos actual antes de usar enlaces viejos.
- 2026-11-20: FullStack Labs publica la misma vacante por país/ciudad (incluye Manizales): deduplicar por empresa + título, quedarse con la de Colombia.
- 2026-11-20: GitHub: escribir con el conector `mcp__Github__*` (G mayúscula); `mcp__github__create_or_update_file` da 403. WebFetch rechaza raíces de tableros (jobs.lever.co/<empresa>) que no salieron en un WebSearch: buscar la raíz antes ("<empresa> careers", "careers-page.com/<empresa>").
- 2026-11-20: Koombea movió su tablero a BambooHR (koombea.bamboohr.com/careers); sus enlaces de Lever siguen visibles pero no están en su página de empleo. Get on Board mantiene indexadas vacantes cerradas ("Closed job"): verificar siempre.
- 2026-11-20: careers-page.com carga la lista de vacantes con JS (WebFetch no la ve); Zarego usa lenguaje de "talent pool".
- 2026-11-20: Tableros reales: Jobgether publica en jobs.lever.co/jobgether (usar ese enlace, no 4dayweek); Truelogic en job-boards.greenhouse.io/truelogic; Amplemarket en job-boards.greenhouse.io/amplemarket. Blue Coding (VM) y Skydropx (Getro/Arc) estaban cerradas.
