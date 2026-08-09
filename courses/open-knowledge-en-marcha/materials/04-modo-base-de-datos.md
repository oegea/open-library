El modo con base de datos es Open Knowledge como **institución viva**, más
que como artefacto publicado. La instancia mantiene su propio estado — una
base de datos SQLite y los medios subidos, en disco local, sin ningún
servicio externo — y con la memoria llegan las funciones que la necesitan.
Lo que no cambia es la filosofía: leer sigue sin exigir cuenta, y quien
aprende sigue sin ser un producto.

## Identidad sin datos personales

El registro en Open Knowledge no pide nombre, ni correo, ni teléfono. En su
lugar, la instancia te ofrece un pseudónimo generado — algo como
`Erudito#4821` — y un código QR. Lo escaneas con cualquier aplicación
autenticadora TOTP (la misma clase de app que quizá ya usas para la
verificación en dos pasos), y desde entonces entras con tu pseudónimo más
el código de seis dígitos que tu app genera. Un **código de recuperación**
de un solo uso, mostrado una única vez al registrarte, es tu salvavidas si
pierdes el dispositivo.

Merece la pena apreciar lo que este diseño se niega a hacer. No hay correo
que filtrar, ni contraseña que reutilizar, ni perfil que construir, ni
manera de que la librería sepa quién eres — y por tanto nada personal que
pueda tener una brecha. La identidad de quien aprende es exactamente tan
real como su aprendizaje, y ni un poco más. La única excepción deliberada:
puedes definir opcionalmente un nombre para tus certificados, y quitarlo
cuando quieras.

## Lo que compra la memoria

- **Progreso entre dispositivos.** Continúas en el móvil lo que empezaste
  en el portátil; la librería recuerda tu página como la recordaba tu
  navegador en modo estático, pero en todas partes.
- **Exámenes corregidos y registrados en el servidor**, asociados a tu
  pseudónimo — la base de la completitud.
- **Certificados.** Completar un curso — todos los materiales obligatorios,
  exámenes aprobados — otorga un certificado compartible con su URL de
  verificación y un PDF descargable. No es una credencial académica; es una
  forma bella y duradera de reconocer que un recorrido de aprendizaje se
  caminó hasta el final.
- **Notificaciones** de cursos nuevos y certificados obtenidos. Nada
  social: ni comentarios, ni seguidores, ni feeds. La lista de cosas que el
  modo base de datos deliberadamente *no* añade importa tanto como la de
  las que sí.

## El panel de administración

La primera cuenta registrada en una instancia recién desplegada se
convierte en la administradora — así que registrarse inmediatamente después
de desplegar forma parte del despliegue. Desde el panel, se gestiona:

- **Cursos**, en un editor visual: secciones, materiales de los cuatro
  tipos, un constructor de exámenes con bancos de preguntas, subida de
  portadas y medios, publicar y despublicar.
- **Noticias y páginas auxiliares** (acerca de, avisos legales…), con
  colocación en menú o pie.
- **Ajustes del sitio**: nombre de la librería, textos e imagen del hero,
  hasta tres logos (cabecera, certificados, documentos exportados),
  registro abierto o cerrado, noticias activadas o no.
- **Usuarios**: listar identidades, abrir el detalle de una persona,
  ajustar el nombre de sus certificados, revocar certificados, promover a
  administrador a alguien de confianza, o eliminar una cuenta.
- **Copias de seguridad**: un clic descarga un zip del entorno completo —
  base de datos, medios, ajustes, todo. Restaurar ese zip en una instancia
  nueva reproduce la librería exactamente. Es recuperación de desastres,
  herramienta de migración y tranquilidad en un solo botón.

Todo lo que una librería estática expresa como ficheros en un repositorio,
el modo base de datos lo expresa como formularios. Cuál interfaz es mejor
no es cuestión de sofisticación sino de temperamento — hay gente que piensa
en git y gente que piensa en botones — y de si tus estudiantes necesitan
que la librería los recuerde.
