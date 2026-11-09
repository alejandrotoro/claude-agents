# claude-agents

Memoria de los agentes programados de Claude. Un solo repo para todos los agentes: **una carpeta por agente**.

```
claude-agents/
├── README.md
└── <nombre-del-agente>/
    └── memory.md      # decisiones, correcciones y aprendizajes del agente
```

## Convenciones

- Cada agente lee su `memory.md` al empezar cada ejecución y lo edita al terminar si aprendió algo nuevo (un commit por cambio, con mensaje descriptivo).
- Lo que diga `memory.md` en **Decisiones** y **Correcciones** manda sobre el prompt del agente.
- Las correcciones del usuario llegan respondiendo al correo del agente; el agente las pasa a su `memory.md`.
- Un agente solo escribe dentro de su propia carpeta.
- También puedes editar `memory.md` a mano: el agente lo respeta desde la siguiente ejecución.

## Agentes

| Carpeta | Qué hace | Horario |
|---|---|---|
| `locales-manizales/` | Busca locales en arriendo en Manizales para el segundo punto de dieta. y envía un correo con los nuevos | Diario, 8:40 AM (Bogotá) |
