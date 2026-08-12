El miércoles por la mañana, Meridian entera esperaba el parche.

El plan cabía en una frase, y Óscar lo dijo en la reunión de las nueve con la voz tensa de quien lleva dos noches sin dormir: se corrige el redondeo de `calc2()`, se refacturan las remesas afectadas de Vesta, y soporte va cerrando incidencias. Júlia había encontrado el bug; Júlia haría el parche, con Denís de apoyo. «Es una línea», dijo alguien al fondo, aliviado. «Es una línea», repitió Óscar, y a Júlia le pareció que lo decía como quien toca madera.

La corrección, en efecto, era una línea. Unificar el criterio: redondear siempre al total, nunca por línea. Júlia la escribió en veinte segundos. Después se quedó mirándola, con el cursor parpadeando, y una vocecita incómoda le repitió la frase del cuaderno de faro que había leído dos noches atrás: *en este sistema hemos roto tantas promesas que ya nadie se fía de nada*.

—Denís —preguntó—, ¿cómo sabemos que esto no rompe otra cosa?

—Lo subes al entorno de pruebas y haces una factura de prueba —dijo Denís—. Si sale bien, va bien.

—¿Una factura? `calc2()` tiene como treinta caminos distintos. Descuentos, abonos, el tipo 7 ese que nadie sabe qué es…

—Pues haces… ¿tres facturas? —Denís se encogió de hombros, pero sin convicción, y bajó la voz—: Mira, te digo la verdad. Aquí siempre se ha probado así. A mano, lo que te dé tiempo, y a rezar. Por eso nadie toca el cálculo. Lo llamamos el dragón: mientras duerme, hay paz. Tu bug de los céntimos es la primera vez en años que alguien le ve un ojo abierto.

Júlia hizo sus tres facturas de prueba. Salieron bien. El parche se desplegó el miércoles a las 17:00 con Óscar mirando por encima de cuatro hombros a la vez.

El jueves a las 9:20, contabilidad de Vesta llamó otra vez. No por las facturas: las facturas, ahora, cuadraban. Llamaron porque **el informe mensual de descuentos** — un listado que Vesta usaba para liquidar acuerdos con sus proveedores — había dejado de cuadrar *con las facturas nuevas*. Descuadre: céntimos por línea. A Júlia se le heló el estómago con una intuición horrible, fue al código del informe, y allí estaba, en un fichero llamado `informes_dto.php` que nadie había mirado porque nadie sabía que existía la relación: el informe **recalculaba los descuentos por su cuenta**, duplicando la vieja lógica de `calc2()` — la de redondear por línea — línea a línea, con su propio código, copiado y pegado hacía años y evolucionado por separado.

Durante una década, dos copias del mismo cálculo habían mentido *igual*, y por eso nadie lo notó. El parche de Júlia había arreglado una copia y desenmascarado la otra.

—No lo entiendo —dijo Júlia en la mesa de Gabriel, con el orgullo hecho trizas—. Arreglé el bug. El cálculo ahora es *correcto*. Y el resultado es que he roto un informe que ni sabía que existía. ¿Cómo se puede trabajar así? Es como… —buscó la comparación exacta, porque las comparaciones exactas eran su manera de no llorar— es como jugar a un roguelike a oscuras. Pisas una baldosa y se activa una trampa en otra habitación.

Gabriel escuchó todo el relato sin interrumpir, asintiendo despacio. Luego se levantó, fue a la estantería metálica donde guardaba manuales de sistemas que ya no existían, y volvió con un libro de tapas gastadas en inglés: *Working Effectively with Legacy Code*, Michael Feathers, 2004.

—Te voy a enseñar la única definición útil que conozco de código legacy —dijo—. No es «código viejo». Ni «código malo». Feathers lo define así: **código legacy es código sin tests.** Sin más. Puede tener quince años o quince minutos. Si no tiene tests, es legacy, porque tocarlo da miedo, y el miedo es exactamente lo que te ha pasado hoy.

—Pero si hubiera hecho tests… —Júlia se frenó—. ¿Tests de qué? ¡Si el comportamiento viejo estaba *mal*! ¿Qué iba a testear, el bug?

Gabriel sonrió de verdad por primera vez desde que lo conocía.

—Sí. Exactamente eso. —Acercó una silla—. Mira. Todo el mundo cree que un test dice «esto es correcto». Pero hay otro tipo de test, más humilde y más poderoso cuando estás a oscuras, que solo dice «esto es *lo que hace hoy*». Se llaman tests de caracterización. Antes de cambiar nada, rodeas al dragón de espejos: le haces trescientas facturas variadas, guardas los resultados exactos que produce hoy — con sus bugs, con todo — y los conviertes en tests. En ese momento tienes algo que este sistema no ha tenido en quince años: una alarma. A partir de ahí, cualquier cambio que hagas te dice al instante *todo* lo que ha alterado. Si cambias el redondeo y se encienden doce alarmas, esas doce alarmas son la lista exacta de sitios donde el sistema dependía del comportamiento viejo. Tu informe de descuentos habría estado en esa lista, el miércoles a las cinco menos cuarto, en tu pantalla. No el jueves a las nueve y veinte, en el teléfono de Vesta.

Júlia se quedó muy quieta.

—Los espejos no arreglan al dragón —dijo despacio, pensándolo mientras lo decía.

—No. Solo te dejan verlo entero. —Gabriel le puso el libro delante—. Arreglarlo viene después, y con calma: funciones pequeñas, nombres honestos, una cosa cada vez. Pero la red va primero. Siempre. Es la diferencia entre operar con anestesia o sin ella.

Se llevó el libro a su mesa esa noche. En el capítulo del cuaderno de faro que tocaba — `02-las-funciones.md` — encontró un pasaje que parecía escrito para ese jueves exacto:

> *Hoy he vuelto a encontrar el cálculo de descuentos copiado en otro fichero. Es la tercera copia que conozco. No las culpo: duplicar es la única manera de tocar este sistema sin miedo, porque tocar el original rompe cosas que nadie recuerda. Así se pudre un sistema: el miedo produce copias, las copias divergen, la divergencia produce más miedo. La salida no es valentía. La valentía sin red es como saltar sin cuerda: sale bien hasta que sale mal. La salida es hacer que el miedo sobre. Tests primero, luego funciones tan pequeñas y tan bien nombradas que mentir sea difícil. Una función debería hacer una cosa, hacerla bien, y no hacer nada más. Si no puedes nombrarla sin usar «y», es que son dos.*

Bajo el pasaje, con otra tinta, como añadido tiempo después, había una sola línea que a Júlia le erizó la piel sin saber por qué:

> *P.D.: Hoy Óscar me ha preguntado si no sería más rápido tirarlo todo y empezar de cero. Le he dicho que esa pregunta la responde mal todo el mundo. Espero que no la haga nunca en serio.*

---

Tardaron nueve días, Denís y ella, en rodear al dragón. Gabriel les montó un entorno con una copia anonimizada de la base de datos y les enseñó a escribir el arnés: un script que generaba facturas de todos los tipos — con descuento y sin él, de una línea y de doscientas, abonos, rectificativas, y cuarenta y una facturas históricas reales del misterioso tipo 7 — las pasaba por `calc2()` *y* por el informe de descuentos, y guardaba cada resultado, céntimo a céntimo, en ficheros de referencia. Trescientos doce casos. La primera vez que la suite entera pasó en verde — 312/312, catorce segundos —, Denís estiró los brazos y dijo, con una solemnidad de la que luego renegaría:

—Vale. Confieso. Esto es lo más tranquilo que he estado en esta empresa desde que entré.

Sobre esa red, el arreglo de verdad fue casi un trámite: una sola política de redondeo, en una sola función con nombre de contrato — `redondearImporteDeLinea()` —, usada por los dos caminos; el informe dejó de duplicar el cálculo y empezó a preguntarle a la fuente. Doce tests se encendieron al hacer el cambio: los doce eran exactamente los casos cuyo comportamiento *querían* cambiar. Los revisaron uno a uno, actualizaron las referencias, y desplegaron un martes por la mañana — «los viernes no se despliega», dijo Gabriel, «esa regla es más vieja que yo» — sin contener la respiración.

Nada se rompió. Esa semana, por primera vez, Júlia entendió una cosa que ya no la abandonaría: la seguridad no era un estado de ánimo. Era una infraestructura.

El viernes, Óscar la paró en el pasillo. Llevaba días encerrado en la pecera con dirección y una consultora externa, y tenía el aspecto de un hombre que hace equilibrios sobre una cifra.

—Lo del arnés de tests. ¿Cuánto os costó?

—Nueve días. Pero para todo el módulo de cálculo, no solo el bug.

—Nueve días. —Óscar hizo un cálculo mental que le agrió la cara—. ¿Sabes cuántos módulos como ese tiene ATLAS? A nueve días por módulo, echa cuentas. No tenemos ese tiempo, Júlia. Vesta quiere resultados visibles en doce meses. —Se pasó la mano por la cara y, por un segundo, pareció simplemente cansado—. Hicisteis buen trabajo. En serio. Pero a este sistema no se le puede ir salvando a cucharadas. El lunes hay reunión general. Ven. Se va a hablar del futuro.

Se alejó por el pasillo. Júlia se quedó con una pregunta en la punta de la lengua que no se atrevió a hacer, y con la posdata del cuaderno de faro latiéndole en la cabeza.

*Espero que no la haga nunca en serio.*
