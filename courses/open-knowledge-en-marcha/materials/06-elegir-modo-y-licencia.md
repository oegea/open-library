**¿Qué modo deberías ejecutar?** La pregunta que lo decide: *¿necesitan tus
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

Si dudas, empieza en estático: es el camino de cinco minutos, y una librería
estática siempre puede migrar después — recreando el contenido en el panel
de una instancia con base de datos. Muchas librerías no necesitarán cuentas
jamás.

**Sobre la licencia, y sobre el espíritu.** Open Knowledge se publica bajo
la **licencia MIT**. Legalmente, MIT permite prácticamente todo: usar,
copiar, modificar, redistribuir, incluso vender, con atribución. Esa
permisividad es deliberada — así se extienden las herramientas abiertas, y
tu librería no depende del permiso de nadie.

Pero el proyecto te pide entender la diferencia entre lo que la licencia
*permite* y aquello *para lo que* existe. **Open Knowledge no se construyó
para impulsar plataformas de cursos con muro de pago, negocios de
conocimiento-como-producto, ni librerías que traten a quien aprende como un
cliente que convertir.** Se construyó para que el conocimiento que alguien
se molestó en curar pudiera regalarse bien — en la tradición de la
biblioteca pública, del software libre, de Wikipedia. La licencia es un
suelo. La tradición es la brújula.

Si tienes conocimiento que merece compartirse, ya sabes todo lo necesario
para compartirlo. Genera un repositorio, súbelo, despliega — y deja la
puerta abierta al salir.
