**¿Qué modo deberías ejecutar?** Una pregunta lo decide: *¿necesitan tus
estudiantes que la librería los recuerde?*

| | Modo estático | Modo base de datos |
|---|---|---|
| El contenido vive en | Un repositorio git público | SQLite + panel de administración |
| Publicar | `git push` | Editor visual |
| Cuentas | No existen | Identidades TOTP pseudónimas |
| Progreso | En el navegador del visitante | Entre dispositivos, en el servidor |
| Exámenes | Corregidos en el navegador | Corregidos y registrados en el servidor |
| Certificados | — | Sí, con PDF y URL de verificación |
| Estado del servidor | Ninguno: instancia desechable | Volumen `/data`: una instancia |
| Hosting | Donde sea, serverless incluido | Una máquina con disco (VPS) |
| Mantenimiento | Ninguno | Copias y actualizaciones (fáciles) |

Tres retratos, para hacerlo concreto:

- *Una profesora que publica un curso para quien lo encuentre* — estático.
  Sin cuentas que gestionar, sin servidor que mantener, contenido versionado
  en git, hosting prácticamente gratis.
- *Una escuela comunitaria que quiere que su alumnado conserve el progreso
  entre dispositivos y obtenga certificados* — modo base de datos en un VPS
  pequeño. Unos euros al mes y un hábito de copias.
- *Aún no lo tengo claro* — empieza en estático. Es el camino de cinco
  minutos, y una librería estática puede migrar después recreando su
  contenido en el panel de una instancia con base de datos. Muchas librerías
  no necesitarán cuentas jamás; sabrás que las necesitas cuando tus
  estudiantes empiecen a pedir ser recordados.

## La licencia, y para qué existe

Open Knowledge se publica bajo la **licencia MIT**, una de las más
permisivas que existen. En términos llanos dice: usa esto, cópialo,
modifícalo, redistribúyelo, incluso vende cosas construidas sobre ello —
conserva el aviso de copyright y acepta que viene sin garantía. Esa
permisividad es deliberada. Es como se extienden las herramientas abiertas,
y garantiza algo que a este curso le importa desde la primera lección: **tu
librería no depende del permiso de nadie** — ni de un proveedor, ni de una
plataforma, ni siquiera de este proyecto.

Pero el proyecto te pide entender la diferencia entre lo que la licencia
*permite* y aquello *para lo que* existe. Una licencia es ley; un proyecto
tiene además una tradición. **Open Knowledge no se construyó para impulsar
plataformas de cursos con muro de pago, negocios de
conocimiento-como-producto, ni librerías que traten a quien aprende como un
cliente que convertir.** Se construyó para que el conocimiento que alguien
se molestó en curar pudiera regalarse bien — en la tradición de la
biblioteca pública, del software libre, de Wikipedia: la tradición que su
curso hermano recorre a lo largo de veintisiete siglos. La licencia es un
suelo. La tradición es la brújula.

Si tienes conocimiento que merece compartirse, ya sabes todo lo necesario
para compartirlo. Genera un repositorio, súbelo, despliega — y deja la
puerta abierta al salir.
