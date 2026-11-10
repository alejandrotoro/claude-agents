# claude-agents

Memoria y datos de los agentes programados de Claude. Un solo repo para todos los agentes: **una carpeta por agente**.

```
claude-agents/
├── README.md
└── <nombre-del-agente>/
    ├── memory.md      # decisiones, correcciones y aprendizajes del agente
    └── data/
        ├── manifest.json   # lista de archivos diarios
        ├── dias/<fecha>.json  # lo nuevo y lo que cambió cada día
        ├── indice.json     # índice para no repetir anuncios
        └── estado.json     # favoritos/descartes que marca Alejo en la página (el agente no lo modifica)
```

## Convenciones

- Cada agente lee su `memory.md` al empezar y lo edita al terminar si aprendió algo nuevo (un commit por cambio).
- Lo que diga `memory.md` en **Decisiones** y **Correcciones** manda sobre el prompt del agente.
- Las correcciones llegan respondiendo al correo del agente, con notas en la página o editando `memory.md` a mano.
- Un agente solo escribe dentro de su propia carpeta.
- Página con las tres búsquedas: https://claude.ai/artifact/PvV3LaRSGhfacviVvuWqg4

## Agentes

| Carpeta | Qué hace | Horario |
|---|---|---|
| `locales-manizales/` | Locales en arriendo (máx. 70 m²) para el segundo punto de dieta.; escribe a inmobiliarias de los locales marcados para contactar | Diario, 8:40 AM (Bogotá) |
| `apartamentos-rentas-cortas/` | Apartamentos/casas en arriendo en Manizales donde se permiten rentas cortas por plataformas | Diario, 8:47 AM (Bogotá) |
| `fincas-lotes/` | Fincas (≤ $400M) y lotes construibles (≤ $300M) en venta cerca de Manizales | Diario, 8:53 AM (Bogotá) |
