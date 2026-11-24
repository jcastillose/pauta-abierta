# Pauta Abierta

Tablero diario de propuestas freelance en comunicaciones, publicado en https://jcastillose.github.io/pauta-abierta/. Proyecto hermano de `jcastillose/aula-abierta` y `jcastillose/obra-abierta`, del que copia la estructura.

## Cómo funciona
- Una tarea programada de Claude (Cowork) corre una vez al día con el texto de `prompt-tarea-diaria.md`. Busca propuestas, escribe `cambios.json` y ejecuta `scripts/merge.py`, que produce `data.json` y `runs.json`.
- `scripts/publish.py` sube esos dos archivos por la API de GitHub usando un token guardado fuera del repositorio (`github-token-pauta.txt` en la carpeta Obra).
- `index.html` es estático y lee `data.json` al abrirse. El mapa de calor agrupa por `modalidad` (remoto, híbrido, presencial) en lugar de región.

## Reglas para trabajar en este repositorio
- El repositorio es público: no escribir el nombre, teléfono, correo, empleador actual ni referencias de la persona, ni tokens.
- La tarea diaria nunca edita `index.html`, este archivo, el prompt ni los scripts. Esos cambios se hacen aquí, a mano o con Claude Code.
- `prompt-tarea-diaria.md` es la fuente de verdad del prompt. Si se modifica, hay que copiar el texto nuevo a la tarea programada; no se sincroniza solo.
- Los valores de `sector`, `modalidad` y `tipo` están definidos en `scripts/merge.py` y en `index.html`; si se cambia uno, cambiar ambos.
- Toda la lógica determinista (ids, estados, retiros, orden, bitácora) vive en `scripts/merge.py`. No duplicarla en el prompt.

## Mantenimiento habitual
- Leer las notas recientes de `runs.json` para ver qué fuentes fallan y ajustar la sección "Fuentes" del prompt.
- Probar el script: `python3 scripts/merge.py data.json runs.json cambios.json` sobre copias.
- Publicar a mano: `python3 scripts/publish.py <ruta-token> . data.json runs.json`.
