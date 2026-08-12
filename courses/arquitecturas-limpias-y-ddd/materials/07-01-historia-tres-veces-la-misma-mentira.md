El piloto creció, y con el crecimiento llegó un enemigo nuevo que no venía del Monstruo. Venía de ellos mismos.

Para el tercer mes, el módulo de facturación tenía tres puertas de entrada. Estaba la **remesa nocturna**, el proceso por lotes que a las 2:00 calculaba las facturas del día de los franquiciados piloto. Estaba la **pantalla interna**, que soporte usaba para emitir facturas sueltas y consultar remesas. Y estaba, recién nacida del plan pactado con Ferrán, la **API para Vesta**: el primer endpoint HTTP de la historia de Meridian que un cliente consumía directamente, con el que el equipo de Ferrán montaba sus cuadros de mando.

Tres puertas, y detrás de las tres, facturas. La misma facturación. En teoría.

El aviso llegó — cómo no — de contabilidad de Vesta, pero esta vez con un matiz nuevo: el error no estaba en producción del Monstruo, sino en el piloto. Una factura emitida a mano desde la pantalla interna por una compañera de soporte, Loli, no aplicaba la regla nueva de los abonos pendientes que la remesa nocturna sí aplicaba desde hacía dos semanas. Misma factura, distinto resultado, según la puerta por la que entraras.

Júlia lo investigó con el estómago encogido, porque esta vez no podía culpar a quince años de sedimento. El código era suyo. Y lo que encontró la hizo enrojecer a solas delante del monitor.

Cuando dos semanas atrás implementaron la regla de descontar abonos pendientes, lo hicieron donde la tarea decía: en la remesa nocturna. El fichero del proceso por lotes preparaba los datos, comprobaba los abonos, llamaba al dominio, guardaba. Diecisiete líneas de coreografía. Y la pantalla interna, escrita un mes antes, tenía su propia coreografía de catorce líneas — parecida, no igual — que nadie actualizó, porque nadie recordó que existía. Y la API de Vesta, nacida la semana anterior, tenía una tercera, copiada de la segunda «para ir rápido», con una comprobación cambiada de orden.

Tres puertas, tres coreografías, tres versiones de la verdad. Había reconstruido, en un módulo de tres meses con arquitectura de manual, el patrón exacto del informe de descuentos duplicado que le había explotado en la cara en la semana tres. A escala pequeña, con mejores nombres. Pero el mismo pecado.

—No te flageles tanto, que es aburrido —dijo Denís, aunque él también estaba serio—. Los tres sitios llaman al dominio. Las entidades validan. Los importes cuadran. No es como `calc2()`.

—Es *exactamente* como `calc2()` —dijo Júlia—. No en el dominio: en lo de alrededor. La pregunta «¿qué pasos hay que dar para emitir una factura?» tiene tres respuestas escritas en tres ficheros. Hoy divergen en los abonos. El mes que viene divergirán en otra cosa. El dominio está limpio y da igual: la *operación* está triplicada. —Se quedó mirando la pantalla—. Nos hemos protegido de la base de datos, de los floats, del SQL… y no nos hemos protegido de nosotros.

Esa noche tocaba, según el índice del faro, el capítulo siete. Júlia ya no se sorprendió de que pareciera escrito para su semana exacta; había entendido que no era magia, sino algo más triste y más útil: los errores de los equipos son tan repetibles que una mujer con ocho años de adelanto podía describirlos con fecha y hora.

> *Un sistema no son solo sus reglas. Son sus operaciones: «emitir una factura», «anular una remesa», «liquidar un periodo». Cada operación es una historia con pasos, y la pregunta importante es: ¿dónde está escrita esa historia?*
> *En ATLAS la respuesta es: en ninguna parte y en todas. Los pasos de «emitir una factura» están medio en la pantalla, medio en el proceso nocturno, medio en dos informes. Cada puerta de entrada cuenta la historia a su manera, y cuando las historias divergen — siempre divergen — el sistema miente por la puerta que menos se vigila.*
> *La regla que quiero: cada operación del negocio se escribe UNA vez, en un fichero que se llama como la operación. Las puertas de entrada — la pantalla, el proceso nocturno, la API del futuro — no cuentan la historia: la INVOCAN. Una puerta debe ser tonta: autentica, traduce lo que llega, llama a la operación, traduce lo que sale. Si una puerta toma una decisión de negocio, por pequeña que sea, esa decisión acaba de esconderse del resto del sistema.*
> *Y las operaciones no fabrican sus herramientas: las reciben. Una operación que construye dentro su conexión a base de datos es una operación que no se puede probar ni cambiar. Los pedidos, cocinados; la despensa, servida desde fuera.*

—«Las puertas no cuentan la historia: la invocan» —leyó Denís por encima de su hombro—. Vale. ¿Y eso cómo se llama en los libros? Porque todo lo de esta mujer acaba teniendo nombre en los libros.

—Casos de uso —dijo Gabriel desde su mesa, sin levantar la vista del monitor—. O interactors, o application services, según el libro. Silvia decía «operaciones», porque odiaba que la misma cosa tuviera cuatro nombres. —Giró la silla—. ¿Sabéis qué es lo único bueno de vuestro problema? Que os ha pasado en el mes tres, con tres puertas. A Fénix le pasó en el año dos, con treinta. Cada pantalla de Fénix era su propia versión de cada operación. Nunca hubo un sitio donde leer «qué significa emitir una factura en este sistema». —Se encogió de hombros—. Por eso los céntimos no cuadraban y nadie podía decir por qué. No había dónde mirar.

La refactorización les llevó una semana, y fue de las que dejan el código más pequeño. Nació la carpeta que faltaba en `application/`: un fichero por operación — `emitirFactura.js`, `calcularRemesa.js`, `anularFactura.js` —, cada uno una función que recibía todo lo que necesitaba, repositorios incluidos, en un solo objeto de entrada. La coreografía de los abonos pendientes quedó escrita una vez, en `emitirFactura`, y las tres puertas quedaron en lo que Silvia pedía: tontas. La pantalla interna se quedó en nueve líneas: validar sesión, leer el formulario, llamar a `emitirFactura`, pintar el resultado o el error. La API de Vesta, en once. La remesa nocturna, en trece, porque además escribía su log.

Y en el proceso descubrieron el regalo escondido, el que ningún capítulo del faro les había anticipado del todo: los tests de operación. Con los repositorios en memoria, probar «emitir una factura con abonos pendientes descuenta los abonos» era un test de doce líneas que corría en milisegundos y no sabía nada de HTTP, ni de pantallas, ni de la madrugada. Cuarenta tests de operación después, Júlia se dio cuenta de que estaban escribiendo, sin querer, el documento que Meridian nunca había tenido: la lista completa, ejecutable y siempre al día, de lo que el sistema *hacía*.

—Léelos de arriba abajo —le dijo a Óscar en la revisión mensual, enseñándole el directorio de tests—. `emitirFactura.test.js`: «emite con los datos del pedido», «descuenta los abonos pendientes», «rechaza pedidos ya facturados», «redondea según el acuerdo de Vesta». Esto es lo que hace el sistema. Si mañana nos preguntan qué significa emitir una factura en Meridian, la respuesta ya no es "depende de la puerta". Es este fichero.

Óscar pasó las páginas de tests con el gesto de quien lee el contrato de una casa que empieza a querer comprar. Al terminar dijo una sola cosa, pero la dijo delante de todos:

—El consejo se reúne a final de mes para decidir lo de NG. Quiero que presentéis esto. Los dos dibujos, ¿eh? El de la cocina y este.

---

El viernes, con la presentación a medio preparar, Júlia bajó a por café y se encontró a Marta en la cocina, discutiendo por teléfono con alguien de Vesta sobre una liquidación. Cuando colgó, Júlia se lanzó, porque la nota de su fichero — *preguntar qué es un abono, a Marta, no a Denís* — llevaba tres semanas mirándola.

—Marta, pregunta rara. ¿Qué es exactamente un abono?

—¿Exactamente? —Marta se rio sin alegría, guardándose el móvil—. Depende de a quién preguntes, cariño. Para mí, comercial, un abono es un descuento pactado que compensa algo: una promoción, un error nuestro, lo que sea. Para contabilidad de Vesta es una factura rectificativa, un documento con número y firma. Y para vuestro sistema… —señaló vagamente hacia arriba, hacia donde vivía ATLAS— para vuestro sistema es un importe en negativo en la siguiente factura, que no es ni lo uno ni lo otro, y cada vez que liquidamos un trimestre me paso dos días cuadrando a mano las tres cosas. —Recogió su taza—. ¿Por qué? ¿Vais a arreglarlo?

Júlia se quedó con el vaso de café a medio llenar, oyendo el goteo de la máquina, con la sensación — física, inconfundible, ya conocida — de estar viendo por primera vez una grieta que llevaba años debajo de la moqueta.

Tres puertas con tres coreografías habían sido un aviso. Esto era otra cosa. Esto era **tres empresas usando la misma palabra para tres cosas distintas**, con un sistema en medio traduciendo mal, en silencio, desde siempre.

—Marta —dijo despacio—, ¿tienes una hora el lunes? Trae ejemplos de esos que cuadras a mano.

Aquella reunión del lunes no salía en ningún plan del piloto. Iba a resultar más importante que todo el código del trimestre.
