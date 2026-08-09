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

A la instancia se le indica dónde vive ese repositorio (una variable de
entorno, `OK_CONTENT_REPO`, apuntando a la URL raw del repositorio) y
simplemente lo renderiza, refrescando su caché aproximadamente cada minuto.

Las consecuencias merecen saborearse:

- **Publicar es un git push.** Editas un fichero Markdown, commit, push — tu
  librería se actualiza en un minuto. Git es tu panel de administración, y
  te llevas gratis historial de versiones, revisión y marcha atrás.
- **El servidor es desechable.** Sin estado no hay nada que respaldar, nada
  que migrar, nada que romper. La instancia puede correr en plataformas
  serverless, capas gratuitas o un contenedor en cualquier parte.
- **Tu contenido es radicalmente abierto.** No está *en* una plataforma; ES
  un repositorio público. Cualquiera puede leer su historia o arrancar su
  propia librería copiando la tuya — que es exactamente el espíritu.
- **No existen cuentas de ningún tipo.** Los visitantes estudian de forma
  anónima y su progreso vive en sus navegadores. Registro, notificaciones,
  certificados y panel de administración sencillamente no existen en este
  modo.

El texto largo nunca vive dentro del JSON: los descriptores son pequeños y
estructurales, y cada lección es un fichero Markdown corriente — agradable
de escribir a mano, e igual de agradable de trabajar con un asistente de
programación con IA. Todo repositorio de contenido generado con el
scaffolder incluye un `AGENTS.md` que enseña a los asistentes (Claude Code,
Codex, OpenCode…) el formato completo, para que puedan ayudarte a redactar,
estructurar y publicar tu material.

Esta misma librería funciona en modo estático. La página que estás leyendo
es un fichero Markdown en un repositorio público.
