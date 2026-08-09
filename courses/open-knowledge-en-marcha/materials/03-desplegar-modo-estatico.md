Desplegar una librería estática son tres pasos y unos minutos. Esta lección
es deliberadamente concreta — comandos que puedes pegar — porque la promesa
de la lección anterior solo importa si el camino es de verdad así de corto.

## Paso 1 — Genera tu repositorio de contenido

Un comando, sin más dependencia que una shell:

```sh
curl -fsSL https://raw.githubusercontent.com/oegea/open-knowledge/main/scripts/init-content-repo.sh | sh -s mi-libreria
```

El script crea una carpeta `mi-libreria/` con un ejemplo completo y
funcional — un curso con una lección de texto y un examen, una noticia, una
página "acerca de", una portada — ya inicializado como repositorio git con
su primer commit hecho. Escribe además dos ficheros de documentación: un
`README.md` con las instrucciones de despliegue (esencialmente esta
lección) y la referencia de formato `AGENTS.md`, para ti y para los
asistentes de IA.

Nada del ejemplo es sagrado: existe para ser editado, copiado y borrado a
medida que lo sustituyes por tu propio material.

## Paso 2 — Publícalo en GitHub

Crea un repositorio nuevo **público** en GitHub (el contenido debe ser
legible públicamente — es lo que la instancia va a leer y, dada la
tradición, también es la gracia). Conéctalo y sube:

```sh
cd mi-libreria
git remote add origin git@github.com:<usuario>/mi-libreria.git
git push -u origin main
```

Tu contenido tiene ahora una URL raw con la forma
`https://raw.githubusercontent.com/<usuario>/mi-libreria/main` — apúntala:
es la única configuración que la aplicación necesita.

## Paso 3 — Despliega la aplicación, una sola vez

Dos caminos fáciles; ambos llevan minutos.

**Serverless (p. ej. Vercel).** Como el modo estático no guarda estado en
el servidor, una plataforma serverless funciona — que el sistema de
ficheros se borre entre invocaciones no cuesta nada cuando no hay nada que
guardar. Usa el flujo de "desplegar desde repositorio" de la plataforma
apuntando a `github.com/oegea/open-knowledge`, y define una variable de
entorno:

```
OK_CONTENT_REPO = https://raw.githubusercontent.com/<usuario>/mi-libreria/main
```

**Docker, en cualquier máquina tuya:**

```sh
git clone https://github.com/oegea/open-knowledge.git && cd open-knowledge
docker build -t open-knowledge .
docker run -d -p 3000:3000 \
  -e OK_CONTENT_REPO=https://raw.githubusercontent.com/<usuario>/mi-libreria/main \
  open-knowledge
```

Esa es toda la operación, y aquí está la parte que merece interiorizarse:
**nunca vuelves a desplegar por contenido.** Editar, commit, push — en
producción en un minuto. La aplicación solo se redespliega cuando quieres
una versión más nueva de Open Knowledge.

## Los hábitos que mantienen sana una librería estática

- **El índice es la verdad.** Un elemento debe estar listado en su
  `index.json` para existir, estén los ficheros que estén en el disco; el
  orden del índice es el orden de presentación (cursos: orden del catálogo;
  noticias: la más nueva primero).
- **Los ids son para siempre.** El progreso de los visitantes está anclado
  a los ids de curso y material en sus propios navegadores. Renombrar un id
  reinicia silenciosamente el progreso de todas las personas que leyeron
  ese curso. Elígelos una vez, consérvalos.
- **Los slugs son URLs.** Cambiar uno rompe los enlaces entrantes — el modo
  estático no tiene memoria de redirecciones. Misma regla: elige bien,
  conserva.
- **Las imágenes van en `media/`** y se referencian con rutas relativas; la
  instancia las resuelve contra tu repositorio automáticamente.
- **Valida el JSON** tras editar a mano (cualquier editor o `python3 -m
  json.tool` sirve): un fichero malformado hace desaparecer ese contenido
  del sitio hasta arreglarlo — el fallo es silencioso a propósito, nunca
  una página rota para tus lectores.
