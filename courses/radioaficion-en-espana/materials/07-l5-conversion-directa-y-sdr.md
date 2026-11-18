El superheterodino no está solo en el mundo. Tiene dos parientes que te vas a encontrar enseguida: uno en los equipos pequeños que la gente del club se monta en casa, y otro en la pantalla del portátil de Marina, en aquella cascada de colores que la tuvo despierta hasta la una de la madrugada.

Esta lección es corta. Al terminar sabrás qué es un receptor de conversión directa, cuál es su punto débil y qué quiere decir que una radio esté «definida por software». Y verás que ninguno de los dos se sale de lo que ya has aprendido.

## El pariente sencillo: la conversión directa

En el superheterodino, el oscilador local se pone separado de la emisora, a una distancia igual a la frecuencia intermedia. ¿Y si se pone **en la misma frecuencia que la emisora**, o a unos cientos de hercios de ella?

Entonces la diferencia que sale del mezclador ya no es una frecuencia intermedia de varios megahercios. Es una frecuencia de cero a unos pocos kilohercios: directamente audio. Es un superheterodino cuya frecuencia intermedia vale cero, y por eso no necesita taller.

> **Receptor de conversión directa:** receptor que mezcla la señal de antena con un oscilador local situado en su misma frecuencia (o a unos cientos de hercios de ella), de modo que a la salida del mezclador se obtiene directamente el audio.

Sus bloques son solo cinco:

> **Filtro de entrada → mezclador (con su oscilador local) → filtro de audio → amplificador de audio.**

El filtro de audio hace aquí el papel del filtro de FI: como la señal ya es audio, la selectividad se consigue dejando pasar solo los tonos que interesan.

**Ejemplo.** Para escuchar una señal de morse que está en 7.030 kHz se pone el oscilador local 700 Hz más abajo. La diferencia es de 700 Hz: un tono que se oye directamente. El oscilador local hace a la vez de BFO.

Cinco cajas se montan en una tarde, y por eso este receptor es el favorito de los equipos artesanales de poca potencia.

—Algún inconveniente tendrá —dijo Marina—, o no existiría el otro.

—El mismo de la imagen, pero sin distancia de por medio —dijo Vicente—. Piensa en el espejo.

En el ejemplo, la señal deseada está 700 Hz por encima del oscilador y da un tono de 700 Hz. Pero una señal que esté 700 Hz **por debajo** del oscilador da exactamente el mismo tono. El receptor oye a la vez lo que hay a los dos lados del oscilador: el doble de vecinos. Y como la intrusa está pegada a la deseada, ningún filtro de entrada puede separarlas. Hay circuitos que lo remedian, pero el receptor deja entonces de ser tan sencillo.

## El pariente moderno: la radio definida por software

En una **radio definida por software** (**SDR**, de *Software Defined Radio*), la señal se convierte en números lo antes posible. Un circuito llamado *conversor analógico-digital* mide el valor de la señal millones de veces por segundo y entrega la lista de medidas a un procesador. A partir de ahí, mezclar, filtrar y demodular ya no lo hacen piezas: lo hacen operaciones matemáticas dentro de un programa.

Las consecuencias son tres:

- **Los filtros son cálculos.** Pueden tener el ancho que quieras, cambiarse al instante y tener unos bordes que ningún filtro de cristal alcanza.
- **Un modo nuevo es una actualización.** No hace falta un circuito nuevo para demodularlo: basta cambiar el programa.
- **Se puede ver la banda.** Como el procesador recibe de golpe un trozo entero de banda, puede dibujarlo. La **cascada** que miraba Marina era eso: una SDR enseñando a la vez todas las señales de la banda de 40 metros.

Casi todos los equipos nuevos funcionan ya así, en todo o en parte. Muchos conservan delante un mezclador y un filtro de los de siempre y hacen con números el resto.

Lo importante para ti es que **las operaciones son las mismas**. Una SDR sigue teniendo que seleccionar una señal, trasladarla, filtrarla y demodularla, y se le siguen pidiendo sensibilidad, selectividad y estabilidad. Lo que has aprendido en estas lecciones no caduca: solo ha cambiado el material de algunas cajas, que ahora son líneas de código.

## Donde la gente se lía

- **«La conversión directa no usa mezclador.»** Lo usa, y es su pieza central. Lo que no tiene es frecuencia intermedia ni filtros de FI.
- **«Un receptor más sencillo no puede tener defectos que el complicado no tenga.»** Oye a los dos lados del oscilador a la vez, cosa que al superheterodino no le pasa.
- **«Una SDR funciona con otros principios.»** Hace las mismas operaciones, con números en lugar de con componentes.
- **«En una SDR no hay nada analógico.»** La antena, el filtro de entrada y el conversor siguen siendo circuitos de verdad, y de su calidad depende todo lo que viene detrás.

## Compruébalo tú

1. Con un receptor de conversión directa quieres oír, con un tono de 600 Hz, una señal de morse que está en 14.060 kHz. ¿Dónde puedes poner el oscilador local?
2. El oscilador local de un receptor de conversión directa está en 3.560 kHz. Hay una estación 800 Hz por encima de él y otra 800 Hz por debajo. ¿Qué tono produce cada una? ¿Puede el receptor distinguirlas?
3. ¿Qué bloque de un receptor de conversión directa hace el trabajo que en un superheterodino hace el filtro de FI?
4. En la cascada de una SDR ves tres señales a la vez, y pasas de escuchar una a escuchar otra pulsando sobre ella. ¿Ha tenido que moverse algún filtro físico?

**Soluciones**

1. A **600 Hz** de la señal, por cualquiera de los dos lados: 600 Hz por debajo o 600 Hz por encima de los 14.060 kHz.
2. Las dos están a 800 Hz del oscilador, y las dos producen un tono de **800 Hz**. No puede distinguirlas: es el punto débil de la conversión directa sencilla.
3. El **filtro de audio**, colocado después del mezclador.
4. No. La SDR ya había digitalizado el trozo entero de banda; elegir otra señal es cambiar unos números en los cálculos de traslado y filtrado.

## En una frase

El receptor de conversión directa es un superheterodino con frecuencia intermedia cero: cinco bloques, muy sencillo, pero oye a los dos lados de su oscilador; la SDR hace las mismas operaciones de siempre con números en lugar de con piezas.

Ya conoces los receptores por dentro. En la lección siguiente aprendemos a juzgarlos: qué significan las cifras de su hoja de características y qué les pasa cuando les entran señales demasiado fuertes.
