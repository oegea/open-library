El modo con base de datos es Open Knowledge como institución viva, más que
como artefacto publicado. La instancia mantiene su propio estado — una base
de datos SQLite y los medios subidos, en disco local, sin ningún servicio
externo — y con el estado llegan las funciones que necesitan memoria:

- **Identidades pseudónimas.** El registro no pide nombre, ni correo, ni
  teléfono. Se te asigna una identidad como `Erudito#4821`, protegida con
  cualquier aplicación autenticadora TOTP (escaneas un QR, tecleas el
  código) y recuperable con un código de un solo uso. Open Knowledge nunca
  sabe quién eres — por diseño, no hay nada personal que filtrar.
- **Progreso entre dispositivos.** Quien aprende continúa en el móvil lo que
  empezó en el portátil.
- **Exámenes corregidos en el servidor**, con resultados anotados a la
  identidad.
- **Certificados.** Completar un curso (todos los materiales obligatorios,
  exámenes aprobados) otorga un certificado de finalización precioso y
  compartible, con URL de verificación y PDF descargable. Quien aprende
  puede definir opcionalmente un nombre amigable para sus certificados — el
  único campo personal opcional de toda la aplicación, voluntario y
  eliminable.
- **Un panel de administración visual.** La primera cuenta registrada se
  convierte en administradora: editor de cursos con secciones y materiales,
  constructor de exámenes, subida de medios, noticias, páginas auxiliares,
  ajustes del sitio (nombre, logos, hero), gestión de usuarios y **copia de
  seguridad completa del entorno en un clic** — un zip que restaura toda tu
  librería en cualquier instancia nueva.
- **Notificaciones**, para que quien está registrado se entere de cursos
  nuevos y certificados obtenidos. Nada social: ni comentarios, ni
  seguidores, ni feeds.

Aquí el contenido se gestiona desde el panel en lugar de git: creas un
curso, añades secciones y materiales en el editor, subes portadas, publicas
cuando está listo. Todo lo que una librería estática expresa como ficheros,
el modo base de datos lo expresa como formularios amables.

La filosofía de cara a quien aprende no cambia un milímetro entre modos:
leer no exige cuenta, y quien aprende no es nunca un producto. Las cuentas
existen únicamente para *conservar el estado de aprendizaje*, y no guardan
más que un pseudónimo, credenciales, progreso y resultados.
