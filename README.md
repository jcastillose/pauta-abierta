# pauta-abierta

Tablero diario de proyectos freelance, encargos recurrentes y jornadas parciales en relaciones públicas, gestión de redes sociales, posicionamiento de marca, pauta digital, prensa y eventos, publicado en
**https://jcastillose.github.io/pauta-abierta/**

Una tarea programada busca propuestas una vez al día, verifica cada aviso abriendo su enlace y actualiza `data.json`. La página lee ese archivo cada vez que alguien la abre.

| Archivo | Qué contiene |
| --- | --- |
| `index.html` | El tablero. Estático. |
| `data.json` | Propuestas vigentes, perfil buscado y fecha de actualización. |
| `runs.json` | Bitácora de cada ejecución. |
| `prompt-tarea-diaria.md` | Instrucciones de la tarea programada. |
| `scripts/merge.py` | Fusión determinista de hallazgos, estados y retiros. |
| `scripts/publish.py` | Publicación por la API de GitHub. |
| `CLAUDE.md` | Guía para mantener el proyecto con Claude Code. |
| `robots.txt` | Pide a los buscadores no indexar el sitio. |

Áreas buscadas, por prioridad: redes sociales; marca y contenido; pauta digital; prensa y relaciones públicas; eventos.

Una propuesta se retira siete días después de cerrada o de vencido su plazo, o tras 14 días sin poder verificarla.
