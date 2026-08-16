# scripts/narrate.py — narración con ElevenLabs

Convierte los capítulos «Historia —» de un curso en materiales de tipo
`audio`: genera un mp3 por capítulo con la API de ElevenLabs y actualiza
`course.json`. El texto completo sigue mostrándose bajo el reproductor, y
las exportaciones Markdown/EPUB/PDF de Open Knowledge lo siguen incluyendo
(precedido de un aviso «consulta este material online» con su enlace).

## Requisitos

- Python 3 (solo librería estándar) y `ffmpeg` en el PATH
  (`brew install ffmpeg`).
- Una cuenta de ElevenLabs con créditos suficientes: cada carácter narrado
  consume aproximadamente un crédito (el consumo real ha sido ~0,5
  créditos/carácter con `eleven_multilingual_v2`).
- La API key en la variable de entorno `ELEVENLABS_API_KEY`. **Nunca la
  escribas en el repositorio ni en el historial de git.**

## Uso

```sh
export ELEVENLABS_API_KEY=sk_...

# 1. Ver qué se narraría y cuántos caracteres cuesta (no llama a la API)
python3 scripts/narrate.py --course <directorio-del-curso> --dry-run

# 2. Escuchar una muestra de ~30 s de una voz (≈400 créditos)
python3 scripts/narrate.py --sample <voice_id>        # -> scratch-samples/sample-<voice_id>.mp3

# 3. Narrar todos los capítulos «Historia» del curso
python3 scripts/narrate.py --course <directorio-del-curso> --voice <voice_id>

# Narrar/regenerar un solo capítulo (borra antes su mp3 si ya existe)
python3 scripts/narrate.py --course <dir> --voice <voice_id> --only mat-03-01
```

Salida: `media/audio/<directorio-del-curso>-<nn>-<slug>.mp3` y, en
`course.json`, `"type": "audio"` + `"mediaPath"` en cada capítulo (los `id`
y `markdownFile` no se tocan). Los mp3 ya existentes se saltan, así que
relanzar el script es seguro. Revisa el diff, escucha algún capítulo y haz
commit de `media/audio/` y `course.json`.

## Qué hace con el texto

- Quita marcas Markdown (negritas, cursivas, encabezados, enlaces → texto,
  imágenes → nada, código inline).
- Las líneas de separación `---` se convierten en una pausa
  (`<break time="1.2s" />`).
- Los bloques de código se leen tal cual (útil para mensajes de commit
  cortos; evita narrar capítulos con bloques largos de código).
- Trocea por párrafos en bloques de ≤ 4.000 caracteres y encadena las
  peticiones con *request stitching* (`previous_request_ids`,
  `previous_text`, `next_text`) para que la entonación no salte entre
  trozos; después concatena los mp3 con `ffmpeg -f concat -c copy`.

## Endpoints de la API que utiliza

Base: `https://api.elevenlabs.io/v1`, autenticación con la cabecera
`xi-api-key: $ELEVENLABS_API_KEY`.

| Uso | Endpoint |
| --- | --- |
| Créditos disponibles | `GET /user/subscription` → `character_count` (usados) y `character_limit` |
| Listar voces (con `voice_id`) | `GET /voices` |
| Sintetizar | `POST /text-to-speech/{voice_id}?output_format=mp3_44100_64` |

Cuerpo de la síntesis:

```json
{
  "text": "…",
  "model_id": "eleven_multilingual_v2",
  "voice_settings": { "stability": 0.5, "similarity_boost": 0.75, "style": 0.0, "use_speaker_boost": true },
  "previous_request_ids": ["…"],
  "previous_text": "…",
  "next_text": "…"
}
```

La respuesta es el audio (`audio/mpeg`) y devuelve la cabecera `request-id`,
que se reenvía en las siguientes peticiones del mismo capítulo.

Consultas rápidas desde la terminal:

```sh
curl -s -H "xi-api-key: $ELEVENLABS_API_KEY" https://api.elevenlabs.io/v1/user/subscription | jq '{character_count, character_limit}'
curl -s -H "xi-api-key: $ELEVENLABS_API_KEY" https://api.elevenlabs.io/v1/voices | jq -r '.voices[] | "\(.voice_id)  \(.name)  \(.labels.language // "")"'
```

## Parámetros fijados en el script

| Constante | Valor | Por qué |
| --- | --- | --- |
| `MODEL` | `eleven_multilingual_v2` | Castellano muy natural y estable en textos largos |
| `OUTPUT_FORMAT` | `mp3_44100_64` | Voz mono: indistinguible de 128 kbps y la mitad de peso (~5 MB por 10 min) |
| `CHUNK_LIMIT` | 4000 | Por debajo del límite por petición del modelo, con margen |

## Transcripción sincronizada — `scripts/align.py`

Open Knowledge resalta palabra a palabra el texto de un capítulo narrado si
el material declara `transcriptPath` (JSON `{ "words": [{ "text", "start",
"end" }] }`, tiempos en segundos). `align.py` lo genera a partir del mp3 ya
publicado y del mismo texto limpio que narró `narrate.py`, con el endpoint de
*forced alignment*:

```sh
export ELEVENLABS_API_KEY=sk_...
python3 scripts/align.py --course <directorio-del-curso> --dry-run   # qué se alinearía
python3 scripts/align.py --course <directorio-del-curso>             # todos los «Historia» con audio
python3 scripts/align.py --course <dir> --only mat-03-01 --force     # rehacer uno
```

Salida: `media/audio/<capítulo>.transcript.json` (≈ 90 KB por capítulo,
~2.000 palabras) y `transcriptPath` en `course.json`. Los ya alineados se
saltan salvo `--force`.

| Uso | Endpoint |
| --- | --- |
| Alinear audio + texto | `POST /forced-alignment` (multipart: `file` = mp3, `text` = texto narrado) → `words[]` con `text/start/end/loss` |

En nuestras pruebas la alineación **no descontó créditos de TTS**
(`character_count` no cambió tras cada llamada); el script imprime el
contador antes y después por si la política cambia. La pérdida (`loss`)
global de cada capítulo quedó entre 0,18 y 0,21 y ~99,5 % de las palabras
mostradas encontraron su pareja narrada.

## Voz usada en la librería

- *El oficio y la máquina* (`ingeniero-de-software-en-la-era-de-la-ia`):
  **Susana – Documentary** (`py37pY8QUQdhW5a7JwPG`), castellano
  peninsular. Reutilízala para mantener coherencia si narras otros cursos
  en español.

Documentación oficial: https://elevenlabs.io/docs/api-reference/text-to-speech
