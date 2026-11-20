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
- Jueves: empresas de producto con Rails que contratan LATAM — Donorbox, Recurly (Medellín), Ridepanda, GitLab, Buk, Workana B2B, y las que aparezcan en "Aprendizajes".
- Viernes: casas de software C — BairesDev (solo roles Senior/Lead de Ruby; sus avisos "evergreen" se repiten: reportar uno solo), Globant, Endava, Wizeline, Applaudo, Gorilla Logic, Jobsity, Scopic, MAS Global, Parrolabs.
- Sábado: Hacker News "Who is hiring?" del mes (buscar Rails + remote + LATAM/anywhere) y newsletters (Ruby Weekly jobs).
- Domingo: solo núcleo.

## Correcciones (de Alejo)
(vacío)

## Empresas descartadas (de Alejo)
(vacío)

## Aprendizajes del agente
- 2026-11-20: Muchas casas de software publican vacantes "de pipeline" (p. ej. Koombea: "applying does not guarantee immediate placement"). Reportarlas marcadas como "pipeline", con fit −5.
- 2026-11-20: FullStack Labs publica la misma vacante por país/ciudad (incluye Manizales): deduplicar por empresa + título, quedarse con la de Colombia.
