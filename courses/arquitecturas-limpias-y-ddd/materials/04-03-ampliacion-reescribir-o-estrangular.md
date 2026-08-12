La historia de Fénix no es una fábula inventada para este curso: es el patrón de fracaso mejor documentado de la industria. Esta ampliación reúne la evidencia, los nombres y la alternativa — el material con el que se ganan (o se evitan) las reuniones como la de Óscar.

## El caso contra la reescritura big-bang

**Joel Spolsky** escribió en el año 2000 el artículo que sigue siendo la referencia: *Things You Should Never Do, Part I* (joelonsoftware.com, gratuito). Su tesis, a propósito de la decisión de Netscape de reescribir su navegador desde cero — reescritura que tardó tres años, durante los cuales el navegador viejo se quedó congelado y la cuota de mercado se evaporó:

> «[Reescribir el código desde cero] es el peor error estratégico que puede cometer una empresa de software.» *(traducción propia)*

Sus argumentos son exactamente los que Júlia y Gabriel descubren por su cuenta, y merecen lista:

- **«Es más difícil leer código que escribirlo.»** Por eso el código ajeno (y el propio, con meses) *parece* peor de lo que es, y por eso la frase «sería más rápido hacerlo de nuevo» se siente verdadera aunque casi nunca lo sea.
- **El código viejo feo está lleno de conocimiento invisible.** Aquella condición absurda de dos líneas es el arreglo de un bug que un cliente sufrió en 2019. «Cuando tiras el código, tiras ese conocimiento»: los céntimos que no cuadraban en Fénix, las quince mil pequeñas verdades del Monstruo.
- **El blanco móvil.** Mientras reescribes, el sistema viejo sigue evolucionando, porque el negocio no puede parar. La reescritura debe correr más rápido que el cambio del original solo para *empatar*.
- **El coste de oportunidad**: los mejores desarrolladores dejan de producir valor visible durante años, mientras el producto que paga las nóminas se degrada — y esa degradación acelerada realimenta la sensación de que la reescritura era necesaria.

A esto se suma el clásico de Fred Brooks, *The Mythical Man-Month* (1975): el **efecto segundo sistema** (*second-system effect*). El segundo sistema que diseña una persona es el más peligroso de su carrera: en él descarga todas las ideas y refinamientos que se quedaron fuera del primero. La reescritura no solo persigue un blanco móvil — lo persigue *cargando* con todas las ambiciones acumuladas. Fénix no intentó ser ATLAS limpio; intentó ser ATLAS más todo lo que ATLAS nunca fue. Los dos efectos se multiplican.

¿Significa esto que ninguna reescritura es legítima? No: hay casos válidos — el producto cambia de propósito, la plataforma muere de verdad (el proveedor cierra), el sistema es pequeño y está bien caracterizado por tests. La honestidad exige decir que Netscape/Mozilla, tras años de travesía, acabó produciendo Firefox. Pero fíjate en el patrón de los éxitos: o el sistema era pequeño, o hubo un patrocinador dispuesto a financiar *años* sin retorno. Pregunta de control antes de firmar una reescritura: «¿tenemos caja y paciencia para que esto no dé nada durante N años, siendo N el doble de lo estimado?». Meridian, con doce meses de ultimátum, obviamente no.

## La higuera estranguladora

La alternativa tiene nombre de botánica y padrino conocido: **Strangler Fig Application**, descrita por Martin Fowler en 2004 (martinfowler.com, entrada gratuita; hoy renombrada de «strangler» a «strangler fig» precisamente para subrayar la imagen). Fowler la concibió observando las higueras estranguladoras australianas: la semilla germina en la copa de un árbol, crece descolgando raíces *mientras el árbol sigue vivo y da soporte*, y años después el árbol original ha sido sustituido por una higuera con su misma forma.

Traducción a software, tal como la servilleta de Silvia la resumía:

1. **Interceptar**: se coloca una fachada delante del sistema viejo (un proxy HTTP, una capa de enrutado, un módulo interceptor) por la que pasa todo el tráfico.
2. **Construir al lado**: se elige *una* capacidad — la que más duela o más valor tenga; en Meridian, facturación — y se construye su versión nueva, con arquitectura limpia, junto al monolito, no dentro.
3. **Desviar gradualmente**: la fachada empieza a enrutar esa capacidad al sistema nuevo — primero en sombra (los dos calculan, se comparan resultados: exactamente el arnés de golden master de la sección 2, reutilizado como comparador de paridad), luego un cliente piloto, luego todos.
4. **Repetir y podar**: capacidad a capacidad. El código viejo que deja de recibir tráfico se apaga y se borra. El monolito muere de inanición, no de incendio.

Las virtudes que lo hacen ganar la discusión económica: **entrega valor desde el primer mes** (la primera capacidad migrada ya mejora vidas), **el riesgo está acotado siempre** (si la pieza nueva falla, la fachada devuelve el tráfico al viejo: hay botón de deshacer, cosa que una migración big-bang no tiene), **no hay blanco móvil** (los cambios de negocio se hacen una sola vez, en la pieza que toque), y **es compatible con seguir vivo**: nadie congela el producto.

Su coste, para ser honestos: exige convivencia larga de dos sistemas (doble operación, sincronización de datos donde las capacidades comparten estado — el problema técnico más delicado del patrón), disciplina para *terminar* las migraciones (el anti-patrón conocido: el estrangulamiento eterno, donde la higuera y el árbol cohabitan una década), y una fachada por la que de verdad pase todo. Es más lento sobre el papel que la reescritura. La diferencia es que su lentitud es real y la rapidez de la otra es imaginaria.

## Screaming architecture aplicada al plan

Detalle fino para cerrar: cuando construyas la «habitación nueva» del estrangulamiento, la estructura de carpetas es tu primera decisión arquitectónica pública. La propuesta de Júlia — la veremos crecer en las próximas secciones — no empieza por `src/controllers` y `src/models` (gritaría «¡soy un framework!»), sino por `src/modules/facturacion/` con `domain/`, `application/` e `infrastructure/` dentro: grita «facturación», y dentro de facturación, grita el teorema de la servilleta. La sección 8 dará el criterio para decidir cuántos módulos como ese existen y dónde cortan sus fronteras — no es una decisión técnica, y ahí está la clave de todo.

## Para llevar

- La reescritura big-bang fracasa por causas estructurales, no por mala suerte: leer es más difícil que escribir, el código feo contiene conocimiento invisible, el blanco se mueve, y el efecto segundo sistema (Brooks) carga la reescritura con diez años de ambiciones aplazadas.
- Referencias canónicas: Spolsky, *Things You Should Never Do* (2000); Brooks, *The Mythical Man-Month* (1975); ambos concuerdan con décadas de casos.
- Strangler fig (Fowler, 2004): fachada delante, construir al lado, desviar gradualmente (sombra → piloto → todos), podar lo muerto. Valor temprano, riesgo acotado, botón de deshacer.
- Costes reales del estrangulamiento: convivencia y sincronización de datos, y la disciplina de terminar. Vigila el estrangulamiento eterno.
- La reescritura legítima existe, pero exige lo que casi nadie tiene: años de financiación sin retorno y un sistema pequeño o congelable.
- El golden master de la sección 2 reaparece como comparador de paridad en la fase sombra: nada se tira en este oficio.
