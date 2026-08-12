Óscar dijo que sí un miércoles, y lo dijo de la manera más rara posible: enfadado.

—Tres meses. Facturación de Vesta, solo franquiciados, en paralelo y sin tocar producción. —Repartió las condiciones como quien reparte cartas boca abajo—. La consultora sigue con el diseño de NG, porque el consejo quiere ver «la apuesta de futuro». Vosotros sois… —buscó la palabra— …el plan B. Si en tres meses vuestra facturación en sombra no cuadra al céntimo con la real, plan B cancelado y todos a NG. ¿Equipo?

—Denís y yo. Y Gabriel a ratos.

—Gabriel a ratos. —Óscar soltó una risa corta, sin humor—. Ya. La banda de los tests. —Se levantó, y al llegar a la puerta se giró con algo menos de coraza—: El arnés de los trescientos doce casos. Ampliadlo a todo el ciclo de Vesta. Si vais a comparar céntimos conmigo mirando, quiero que se compare *todo*.

Cuando salió, Denís exhaló como un globo pinchado.

—¿Te das cuenta de que nos acaba de dar exactamente lo que pedíamos fingiendo que nos castiga?

—Es su manera de cubrirse —dijo Gabriel desde su mesa, sin levantar la vista—. Si funcionáis, el mérito es de su plan de dos vías. Si falláis, siempre tuvo razón NG. No lo juzguéis mal: es la primera vez en diez años que deja convivir las dos ideas. —Hizo una pausa y añadió, más bajo—: Eso ya es más de lo que consiguió Silvia.

---

El repositorio nuevo se llamó, por unanimidad de tres, `meridian-facturacion`. Júlia escribió la primera estructura de carpetas con el cuaderno de faro abierto en la otra pantalla, como quien cocina con el libro de recetas apoyado en la encimera:

```
src/modules/facturacion/
  domain/
  application/
  infrastructure/
  test/
```

—Cuatro carpetas vacías —dijo Denís, solemne—. Nunca un viernes dio para tanto.

Pero no eran carpetas: eran fronteras. En `domain` viviría el negocio puro — facturas, líneas, impuestos, sin un solo import hacia fuera. En `application`, las operaciones — «emitir factura», «calcular remesa». En `infrastructure`, el mundo: la base de datos vieja de ATLAS, de la que el módulo nuevo leería los pedidos mientras el Monstruo siguiera vivo. La higuera, creciendo pegada al árbol.

La primera semana fue embriagadora. Sin quince años de sedimento, las cosas costaban lo que deberían costar: una tarde para el modelo de líneas de factura, otra para los descuentos de franquiciado, con tests que corrían en milisegundos. Denís, converso con el fervor de los conversos, llegó a decir en voz alta que programar así era «como jugar con las reglas puestas en la caja».

El viernes de la segunda semana conectaron el módulo nuevo al comparador — el golden master ampliado, que ahora hacía de juez entre dos mundos: cada remesa de prueba se calculaba con `calc2()` *y* con el módulo nuevo, y el arnés cotejaba céntimo a céntimo.

Trescientos nueve de trescientos doce.

—¿Tres fallos? —Denís se inclinó hacia la pantalla—. A ver, a ver. Diferencia de… un céntimo. Un céntimo exacto, en tres facturas. Las tres con muchas líneas y descuento raro. —Se volvió hacia Júlia—. El viejo redondea mal en tres casos, seguro. El Monstruo lleva quince años redondeando con los codos, lo hemos visto.

Gabriel, que estaba de paso con un café, se detuvo. No dijo nada; se quedó mirando la pantalla con la cabeza ligeramente ladeada, como escuchando un ruido lejano en un motor.

—¿Qué? —dijo Denís.

—Nada. Solo que llevo oyendo «seguro que el viejo se equivoca» desde dos mil quince. —Sopló el café—. Demostradlo.

Lo demostraron. En dirección contraria.

Tardaron toda la mañana en aislarlo, y cuando lo tuvieron delante era tan pequeño que daba risa, y tan grave que la quitaba. Júlia lo escribió en la consola de Node para verlo desnudo:

```
> 0.1 + 0.2
0.30000000000000004
```

—Es una broma —dijo Denís.

—No es una broma. Es coma flotante. —Júlia lo recordaba de una asignatura, vagamente, como se recuerdan las cosas que uno aprobó sin creer que fueran a existir de verdad—. Los ordenadores guardan los decimales en binario. Un décimo, en binario, es periódico: no cabe exacto, como un tercio no cabe exacto en decimal. Todos los números que manejamos — 19,90, el 21% de IVA, un descuento del 3,5% — se guardan *casi* exactos. Y «casi», multiplicado por doscientas líneas y un descuento y un redondeo… — señaló la pantalla— …es esto. Nuestro módulo nuevo, el limpio, el moderno, llevaba el error *dentro del tipo de dato*. `calc2()` no falla en estos tres casos. Fallamos nosotros.

El silencio duró lo que tarda en caerse un pedestal.

—Espera. —Denís se frotó la cara—. ¿Me estás diciendo que el Monstruo, el innombrable, el de `$aux3`, ¿hace *bien* los decimales?

Gabriel acercó una silla, y por primera vez desde que Júlia lo conocía, se sentó a contar una historia sin que se la pidieran.

—Dos mil once. Un descuadre de tres céntimos en una liquidación de fin de año de un cliente que ya no existe. Tres céntimos: el contable del cliente los persiguió durante una semana como si fueran tres millones, y tenía razón, porque en contabilidad un céntimo que no cuadra no es un importe, es una *grieta*: significa que no sabes de dónde salen tus números. —Bebió café—. Silvia estuvo dos días con aquello. Cuando encontró la causa — esta misma que tenéis en pantalla — se enfadó como nunca la vi enfadarse, pero no con el bug: con nosotros. «Llevamos años sumando dinero con un tipo de dato que no sabe sumar dinero.» Y esa semana el camino principal del cálculo pasó a céntimos. Enteros. Un euro con noventa son ciento noventa, y las divisiones solo donde el negocio diga cómo repartir el resto. No llegó a todas partes — el Monstruo es grande, y vuestra línea 847 con su `round` a dos decimales es de las esquinas que se quedaron a medias, por eso pudo bailar el redondeo —, pero el corazón quedó sano. Fue de las pocas veces que arreglamos algo *de raíz*. —Señaló la pantalla con la barbilla—. El código es horrible, pero esa lección la lleva dentro. Vosotros habéis escrito código precioso sin la lección. Ahí tenéis la diferencia entre limpio y correcto: ninguna de las dos cosas te regala la otra.

Júlia pensó en Fénix y sus céntimos que no cuadraban, y comprendió — con un pequeño escalofrío — que acababa de vivir, en miniatura y con red, exactamente aquello que había matado al proyecto sin red. Las quince mil verdades del Monstruo. Acababan de conocer la primera.

—Entonces, ¿cambiamos los float por enteros y ya? —preguntó Denís.

—No —dijo Júlia, lentamente, porque lo estaba viendo mientras lo decía. El capítulo cinco del faro, leído el domingo, se le estaba ordenando solo en la cabeza—. Si repartimos «céntimos como enteros» por todo el código, dentro de un año alguien nuevo escribirá `importe / 2` sin pensar en el resto, o sumará céntimos con un porcentaje, y volveremos aquí. La lección no puede vivir en la disciplina de cada uno. Tiene que vivir en *el tipo*. —Abrió el editor—. Hacemos una clase `Importe`. Dentro: céntimos, enteros, siempre. No se puede construir una inválida: si intentas meterle 19.9 flotante, explota en la puerta, con un error que te explica cómo se hace. No se puede modificar una vez creada: sumar dos importes te da un importe *nuevo*. Y las operaciones peligrosas — dividir entre doce meses, repartir un descuento — tienen nombre, y dentro está decidido qué pasa con el céntimo sobrante, *una vez*, donde un contable pueda leerlo.

Gabriel se levantó con su café y su sonrisa breve.

—Silvia lo llamaba «objetos que no saben mentir». —Se fue hacia su mesa, y desde media sala, sin volverse, añadió—: El capítulo cinco era su favorito.

---

Esa noche, releyendo el capítulo con otros ojos, Júlia encontró el pasaje que se le había resbalado el domingo y que ahora la esperaba:

> *La mitad de los bugs de este sistema no son errores de lógica. Son datos ilegales paseándose con papeles falsos: un importe negativo donde no puede haberlo, un NIF con letra imposible, una fecha de vencimiento anterior a la de emisión. Los validamos en la pantalla — a veces —, y a partir de ahí viajan por el sistema como si fueran de fiar, y revientan lejos, donde ya nadie recuerda de qué frontera entraron.*
> *La regla que quiero para el sistema que no llegué a construir: que los datos inválidos no puedan NACER. Que no exista manera de tener entre manos un Importe, un NIF, una Factura que mientan. Si cada concepto del negocio es un tipo, y cada tipo defiende sus propias reglas en su constructor, entonces la validación no es una costumbre que se olvida: es una ley física. En un sistema así, media categoría de bugs no se arregla. Se extingue.*

Júlia miró la hora — la 1:20 — y aun así abrió el editor y escribió, despacio, la primera clase del dominio nuevo. La llamó `Importe`. Le puso el constructor privado, el `create` que validaba, el error con el prefijo del nombre de la clase, como hacía Silvia en sus ejemplos.

En el comparador, a la mañana siguiente: **312 de 312**.

Denís miró el número, miró a Júlia, y declaró con la solemnidad de sus grandes ocasiones:

—Vale. Ahora ya no jugamos con las reglas puestas en la caja. Ahora las reglas juegan con nosotros.

Nadie supo muy bien qué quería decir, ni él tampoco, pero todos entendieron que era verdad.
