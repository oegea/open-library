Desplegar una librería estática son tres pasos y unos minutos.

**Paso 1 — Genera tu repositorio de contenido.** Un comando, sin más
dependencias que una shell:

```sh
curl -fsSL https://raw.githubusercontent.com/oegea/open-knowledge/main/scripts/init-content-repo.sh | sh -s mi-libreria
```

Obtienes un ejemplo funcional — un curso, un examen, una noticia, una página
"acerca de" — ya confirmado en un repositorio git recién creado, con un
README con estas mismas instrucciones y un `AGENTS.md` para asistentes de
IA.

**Paso 2 — Súbelo a GitHub, público:**

```sh
cd mi-libreria
git remote add origin git@github.com:<usuario>/mi-libreria.git
git push -u origin main
```

**Paso 3 — Despliega la aplicación una sola vez, apuntando a tu contenido.**
Dos caminos fáciles:

*Serverless (p. ej. Vercel).* Como el modo estático no tiene estado, el
hosting serverless funciona. Usa el flujo de Vercel de "desplegar desde
repositorio" contra `github.com/oegea/open-knowledge` y define una única
variable de entorno:

```
OK_CONTENT_REPO = https://raw.githubusercontent.com/<usuario>/mi-libreria/main
```

*Docker, en cualquier máquina:*

```sh
git clone https://github.com/oegea/open-knowledge.git && cd open-knowledge
docker build -t open-knowledge .
docker run -d -p 3000:3000 \
  -e OK_CONTENT_REPO=https://raw.githubusercontent.com/<usuario>/mi-libreria/main \
  open-knowledge
```

Esa es toda la operación. A partir de aquí nunca redespliegas por contenido:
editar, commit, push, y el sitio se actualiza en un minuto. Solo
redespliegas la aplicación para adoptar versiones nuevas de Open Knowledge.

Algunas notas prácticas:

- El repositorio de contenido **debe ser legible públicamente** — es lo que
  hace funcionar el modo, y también es la gracia.
- Las imágenes van en `media/` y se referencian con rutas relativas.
- Un elemento debe estar listado en su `index.json` para existir; el orden
  del índice es el orden de presentación.
- No cambies nunca un `id` ya publicado: el progreso local de los visitantes
  está anclado a los ids de curso y material.
