Júlia Ferrer llevaba veinte minutos siendo programadora profesional cuando aprendió la primera lección del oficio: nadie te enseña dónde está nada.

—Tu usuario es `jferrer`, la contraseña te la cambias al entrar, el café de la máquina del fondo sabe a lo que sabe y el repositorio es ese icono que pone ATLAS —le dijo Denís, el otro junior, un chico larguirucho con una camiseta de un grupo que Júlia fingió conocer—. Cualquier otra pregunta, al señor de la esquina. Se llama Gabriel. No muerde, pero tarda en arrancar, como los servidores viejos.

La oficina de Meridian Sistemas ocupaba la segunda planta de un edificio de los ochenta en una ciudad de provincia: moqueta gris, una pecera de reuniones, treinta personas y un zumbido permanente de ventiladores. En la pared del fondo, alguien había colgado hacía años un póster descolorido de *La guerra de las galaxias* y nadie lo había quitado. A Júlia, veinticuatro años, grado recién terminado y una carpeta de apuntes ordenada por colores, aquello le pareció — lo pensó con total sinceridad — el lugar más emocionante del mundo. Era su primer trabajo. Era lunes. Todo estaba por estrenar.

El repositorio tardó cuarenta minutos en clonarse.

Mientras la barra avanzaba, Júlia hizo lo que hacía siempre que algo la esperaba: abrir un fichero de texto plano y tomar notas. Lo apuntaba todo desde niña, en ficheros con nombres como `notas_2026_08.txt`, con la fe tranquila de quien juega a roguelikes y sabe que morir está bien si tomaste nota de por qué. Escribió: *Día 1. ATLAS = el producto. ERP de facturación. 15 años. Cliente gordo: Grupo Vesta (supermercados). Preguntar qué es un ERP sin que se note mucho.*

A las 11:04, ATLAS terminó de clonarse. Júlia abrió el directorio raíz y se quedó mirando la pantalla con la sensación exacta de haber abierto la puerta de un trastero donde una familia entera hubiera ido metiendo cosas durante quince años. Doscientos treinta y un ficheros en la raíz. Carpetas llamadas `nuevo`, `nuevo2`, `viejo_NO_BORRAR`, `tmp_pruebas_karim`. Un fichero llamado `facturacion.php` de veintidós mil líneas. Otro llamado `facturacion_v2.php`, de dieciocho mil, que — comprobaría después — no reemplazaba al primero sino que lo *necesitaba*.

—Ah —dijo Denís por encima de la mampara, sin levantar la vista—. Ya has conocido al Monstruo.

—¿Siempre es así?

—No. A veces es peor. —Denís giró la silla, teatral—. Regla de la casa: el Monstruo funciona. Nadie sabe del todo por qué, pero funciona. Factura ciento y pico millones de euros al año de nuestros clientes. Así que la regla número uno es: no lo despiertes.

Júlia anotó: *Regla 1: no despertar al Monstruo.* Y debajo, porque su honestidad era más fuerte que su vergüenza: *No entiendo cómo algo puede funcionar y estar así.*

Tuvo tres semanas para averiguarlo. Le dieron tareas pequeñas — cambiar textos, añadir una columna a un listado, «cosas que no toquen cálculo» — y en cada una repitió el mismo ciclo: abrir un fichero, no entender nada, buscar quién llamaba a qué, descubrir que la respuesta era «todo llama a todo», preguntar a Denís, que sabía trucos pero no razones, y acabar en la mesa de Gabriel.

Gabriel Antúnez tenía sesenta y un años, una barba gris recortada, y una colección aparentemente infinita de camisetas negras de conciertos de grupos que ya no existían. Era el administrador de sistemas, el responsable del servidor Git, del despliegue, de la centralita y, en la práctica, la memoria histórica de Meridian. Hablaba poco y escuchaba con una atención ligeramente incómoda, como si las preguntas le parecieran más interesantes que las respuestas.

—Gabriel, ¿qué hace `calc2()`?

Fue la primera vez que Júlia lo vio sonreír. Fue una sonrisa breve, sin alegría, la sonrisa de quien reconoce a un viejo conocido en un mal sitio.

—`calc2()` calcula las facturas.

—¿Y `calc()`?

—También. Pero solo las de antes de 2014. Creemos. —Se rascó la barba—. ¿Por qué?

—Porque tiene mil cuatrocientas líneas y hay una variable que se llama `$aux3` que se usa en seiscientas de ellas y todavía no sé qué contiene.

—Depende de la línea —dijo Gabriel, con la serenidad de un hombre que ha hecho las paces con el horror—. A veces es un importe. A veces es un cliente. Durante unas doscientas líneas, si no recuerdo mal, es una fecha.

Júlia esperó a que fuera una broma. No lo era.

---

El incidente empezó un martes a las 8:40 de la mañana, veintitrés días después de su llegada, y durante años en Meridian bastaría con decir «el martes» para que todo el mundo supiera cuál.

Júlia lo supo por el silencio. El zumbido de la oficina cambió de frecuencia: primero se apagaron las conversaciones, luego sonó un teléfono, luego dos, luego el móvil de Óscar Llovet, el director técnico, que cruzó la sala abrochándose la americana con la cara de quien corre hacia un incendio en zapatillas. En la pantalla de Denís, la bandeja del correo de soporte se recargaba sola: 87 mensajes sin leer. 130. 214. Todos con variantes del mismo asunto: **«Error importes factura agosto»**.

Grupo Vesta — sesenta supermercados, el sesenta por ciento de la facturación de Meridian — había emitido esa madrugada, a través de ATLAS, su remesa mensual: miles de facturas a proveedores y franquiciados. Y ATLAS había calculado mal. No todas: *algunas*. No mucho: *céntimos*. Céntimos por línea, multiplicados por cientos de líneas por factura, multiplicados por miles de facturas. La primera cifra que alguien se atrevió a escribir en la pizarra de la pecera fue 4.700,32 € de descuadre total. La segunda cifra fue peor: nadie sabía *cuáles* facturas estaban mal, así que había que revisarlas todas.

—¿Cómo puede estar mal *a veces*? —preguntó alguien de soporte desde la puerta de la pecera.

Nadie contestó, así que Júlia, desde su silla, cometió el primer acto profesional relevante de su carrera: se puso a leer `calc2()` de verdad. No a ojear: a *leer*, línea a línea, con papel y boli, como quien mapea una mazmorra. Tardó todo el día y parte de la noche. En su fichero de notas fue apareciendo, trabajosamente, el mapa de la función: los tres bloques que hacían lo mismo pero distinto; el `if ($tipo == 7)` — ¿qué era el tipo 7? nadie lo sabía; en la base de datos había facturas de tipo 1 al 9 y de tipo 7 no había *casi* ninguna —; el redondeo que unas veces se hacía por línea y otras al total, según un parámetro llamado `$modo_calc` que venía de una columna llamada `mc` de una tabla llamada `cfg2`.

A las 21:15 encontró la grieta. Una condición, en la línea 847:

```php
if ($cliente_dto > 0 && $aux3 > 1) { $imp = round($imp, 2); }
```

`$aux3`, en esa línea, era el número de líneas de la factura. Si un cliente tenía descuento y la factura tenía más de una línea, el importe se redondeaba *por línea* y después se sumaba. Si no, se sumaba primero y se redondeaba al final. Dos caminos, dos resultados, y una diferencia de fracciones de céntimo que casi nunca importaba. Esa madrugada, Vesta había aplicado por primera vez un descuento nuevo — un acuerdo comercial firmado la semana anterior — a miles de facturas a la vez. La grieta llevaba años ahí, dormida, esperando su noche.

Júlia se quedó mirando la línea mucho rato. No sentía triunfo. Sentía una especie de vértigo moral que no sabía nombrar todavía y que este curso va a pasar varias secciones nombrando. La línea *funcionaba*. Hacía exactamente lo que decía. El problema era que nadie — ni su autor, fuera quien fuera, hacía los años que fueran — habría podido decir *qué quería decir*. `$aux3 > 1`. Un descuadre de 4.700,32 euros y un cliente furioso cabían enteros en la distancia entre lo que el código hacía y lo que el código decía.

Cuando levantó la vista, Gabriel estaba de pie junto a su mesa con dos cafés de máquina. Se había quedado, como ella. Le tendió uno.

—Enséñame —dijo.

Miró la línea en silencio. Asintió despacio, como quien confirma un diagnóstico que se temía.

—¿Sabes qué es lo gracioso? —dijo por fin—. Que el que escribió esto no era malo. Era rapidísimo. Resolvía en una tarde lo que otros en una semana. —Bebió café—. Solo que escribía para la máquina. Y la máquina, fíjate, le entendía perfectamente. Le hemos entendido todos menos las personas.

—¿Quién era?

Gabriel no contestó a eso. Dejó el vaso en la mesa de Júlia y dijo:

—Mañana va a ser un día muy largo. Vesta ha pedido reunión con dirección. —Se detuvo un momento, de espaldas, y añadió sin volverse—: Has hecho un buen trabajo hoy. Leer código que no escribiste es el noventa por ciento de este oficio. Nadie lo cuenta en la universidad.

---

La reunión con Vesta duró tres horas y salió de ella una cifra que corrió por la oficina en voz baja: **doce meses**. Vesta no se iba — todavía —, pero exigía un plan. «Modernización verificable», decían las actas. Doce meses para demostrar que ATLAS podía dejar de ser una caja negra que fallaba por céntimos, o el mayor cliente de la casa empezaría a migrar a un competidor. Óscar salió de la pecera con la mandíbula apretada y una palabra nueva en la boca, que Júlia le oyó decir por teléfono esa misma tarde: *reescritura*.

Pero eso — el plan de Óscar, y todo lo que desencadenó — pertenece a capítulos posteriores. Lo que cierra este capítulo ocurrió esa noche, a las 19:40, cuando Júlia, con la oficina ya medio vacía, hizo una cosa pequeña que lo cambió todo: buscó al autor de la línea 847.

`git blame` le dio un nombre que no conocía y una fecha imposible, porque la migración de CVS a Git de 2015 había aplastado la historia anterior: todo lo viejo aparecía firmado por `migracion-svc`. Pero el nombre real estaba en los comentarios de cabecera del fichero, en un bloque que alguien había ido copiando de versión en versión como se copian las lápidas:

```
// facturacion.php — módulo de cálculo
// (c) Meridian Sistemas
// autora original: S. Roca — mantenido por: [ver wiki]
```

*S. Roca.* La wiki enlazada llevaba a una página borrada. Júlia hizo lo que cualquier persona con su carácter habría hecho: entró en el servidor Git interno — Gabriel daba acceso de lectura a todo el mundo, «aquí no hay secretos», decía — y buscó `roca` en la lista completa de repositorios. Aparecieron dos. Uno se llamaba `atlas-legacy-mirror`. 

El otro se llamaba `faro`.

Último commit: hacía ocho años. Sin descripción. Un solo colaborador: **Silvia Roca**. Júlia lo clonó — tardó dos segundos; era pequeño, era *limpísimo* — y encontró dentro una estructura de carpetas ordenada como un jardín japonés y una serie de ficheros markdown numerados: `01-los-nombres.md`, `02-las-funciones.md`, `03-el-acoplamiento.md`… Dieciocho ficheros. El primero empezaba así:

> *Cuaderno de faro, 1.*
> *Un faro no evita las tormentas. Solo evita que los barcos se estrellen contra lo que no ven.*
> *Escribo estas notas para quien venga después, porque he entendido tarde una cosa: este sistema no se está hundiendo por falta de talento. Se está hundiendo por falta de luz. Nadie puede leer lo que escribimos. Yo la primera.*
> *Empiezo por lo más pequeño que existe en el código, que es también lo más importante: los nombres. Un nombre es una promesa. Cada variable, cada función, cada fichero le está prometiendo algo a quien lo lee. En este sistema hemos roto tantas promesas que ya nadie se fía de nada, y por eso todo cuesta el triple.*
> *Si estás leyendo esto, seas quien seas: no escribas para la máquina. La máquina entiende cualquier cosa. Escribe para el que llegue detrás de ti, cansado, con prisa, a las nueve de la noche de un martes malo. Escribe para que esa persona no se estrelle.*

Júlia leyó los dieciocho títulos con el corazón acelerado, la sensación inconfundible de haber encontrado el mapa de la mazmorra entera. Luego volvió al primero y lo leyó despacio, dos veces.

Después abrió su fichero de notas y escribió: *Día 23. He encontrado un faro. ¿Quién es Silvia Roca y por qué nadie habla de ella?*

En la oficina a oscuras, la única luz encendida era la de su monitor.
