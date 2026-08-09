En modo de contenido estático tu librería **no tiene base de datos ni
estado en el servidor**. Todo lo que sirve vive como ficheros en un
**repositorio git público**:

```
settings.json                          nombre y configuración de la librería
courses/index.json                     qué cursos existen y su orden
courses/<nombre>/course.json           un curso: metadatos, secciones, exámenes
courses/<nombre>/materials/*.md        un fichero Markdown por lección de texto
news/<nombre>.json + news/<nombre>.md  una noticia cada uno
pages/<nombre>.json + <nombre>.md      una página auxiliar cada una
media/                                 imágenes y archivos
```

A la instancia se le indica dónde vive ese repositorio — una única variable
de entorno, `OK_CONTENT_REPO`, apuntando a la URL raw del repositorio — y
simplemente lo renderiza, refrescando su caché aproximadamente cada minuto.

## ¿Por qué git, precisamente?

Porque un repositorio git es, discretamente, el mejor gestor de contenidos
jamás construido, y ya sabes usarlo. Considera lo que obtienes sin instalar
nada:

- **Publicar es un push.** Editas un fichero Markdown, commit, push — tu
  librería se actualiza en un minuto. Sin despliegues, sin compilación, sin
  sesión de administración.
- **El historial es automático.** Cada versión de cada lección, para
  siempre, con autoría y fechas. ¿Un estropicio? Reviertes el commit.
  ¿Quieres saber qué cambió en un curso desde primavera? `git diff`.
- **La revisión sale gratis.** Un colega puede proponerte una corrección
  como pull request. Lees el diff, fusionas. Ese flujo le costó décadas de
  refinamiento a la ingeniería de software, y tu librería lo hereda entero.
- **El servidor es desechable.** Sin estado no hay nada que respaldar, nada
  que migrar, nada que se pueda perder. Si el contenedor muere, arrancas
  otro; si la plataforma te decepciona, apuntas otra distinta al mismo
  repositorio. Tu librería no puede ser tomada como rehén.
- **Apertura radical, estructural.** Tu contenido no está *en* una
  plataforma; ES un repositorio público. Cualquiera puede leer su historia,
  aprender de cómo está construida, o arrancar su propia librería a partir
  de una copia — lo cual, dada la tradición a la que pertenece este
  proyecto, es exactamente la gracia.

## La forma del contenido

Una regla de diseño mantiene agradable el formato: **el texto largo nunca
vive dentro del JSON**. Los descriptores JSON son pequeños y estructurales
— títulos, orden, metadatos, definiciones de examen — mientras que cada
lección es un fichero Markdown corriente, referenciado por nombre. La prosa
se mantiene comparable, revisable y cómoda de escribir. La única excepción
deliberada son las preguntas de examen, que van dentro de `course.json`:
son estructura (opciones, respuestas correctas, explicaciones), no prosa.

Todo repositorio generado con el scaffolder incluye además un `AGENTS.md`
que documenta el formato completo en detalle. Sirve a la vez de referencia
para ti y de instrucciones para asistentes de programación con IA (Claude
Code, Codex, OpenCode…), de modo que uno pueda ayudarte a redactar,
estructurar y publicar tu material — tú pones el conocimiento y el
criterio; el asistente se encarga del formato.

## Lo que aquí no existe

En modo estático no hay cuentas de ningún tipo. Los visitantes estudian de
forma anónima; su progreso vive en sus navegadores; los exámenes se
corrigen al momento sin registrarse en ninguna parte. Registro,
notificaciones, certificados y panel de administración sencillamente no
existen — no desactivados: ausentes. Para muchas librerías eso no es una
limitación sino una virtud: nada que asegurar, nada que filtrar, nada que
mantener.

Esta misma librería funciona en modo estático. La página que estás leyendo
es un fichero Markdown en un repositorio público, y si consultas el
historial de ese repositorio puedes ver escribirse este mismo párrafo.
