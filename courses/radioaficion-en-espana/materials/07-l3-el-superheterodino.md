«El receptor no intenta trabajar en la frecuencia que tú sintonizas», le dijo Vicente a Marina. «Traduce todas las emisoras a una única frecuencia interna fija, y hace todo el trabajo fino allí, en su taller, con las herramientas clavadas en la pared.» Al día siguiente lo dibujó en la libreta cuadriculada, caja a caja.

Ya tienes las dos piezas que hacen falta: el problema (un filtro estrecho no puede ser móvil) y la herramienta (el mezclador, que traslada una señal sin estropearla). Esta lección las junta. Al terminar sabrás dibujar de memoria el esquema de bloques del receptor **superheterodino**, decir qué hace cada bloque y explicar por qué a la frecuencia interna fija se le saca tanto partido. Es pregunta segura de examen, y a veces la ponen en forma de dibujo.

## La idea: un taller que no se mueve

Quien repara a domicilio solo puede llevar las herramientas que le caben en un maletín. Quien tiene taller puede atornillar a la mesa las buenas, las que no se mueven, y hacer un trabajo mucho más fino; solo necesita un mensajero que le traiga las piezas.

El receptor superheterodino es eso:

- El **taller** es una cadena de filtros y amplificadores construidos para trabajar a **una sola frecuencia, siempre la misma**.
- El **mensajero** es el mezclador con su oscilador local, que coge la emisora que tú elijas, esté donde esté, y la traslada a la frecuencia del taller.

A esa frecuencia fija del taller se le llama **frecuencia intermedia**.

> **Frecuencia intermedia (FI):** la frecuencia fija a la que el receptor superheterodino traslada cualquier señal que sintonices, y en la que hace el filtrado fino y casi toda la amplificación.

El nombre es histórico: en los primeros receptores de este tipo quedaba a medio camino entre la radiofrecuencia que entra por la antena y la audiofrecuencia que sale por el altavoz. Hoy puede estar incluso por encima de la señal recibida; lo que la define es que es **fija**. Valores muy usados son 455 kHz, 9 MHz y 10,7 MHz.

## Cómo se sintoniza: cambia el oscilador, no el taller

Pongamos un receptor con una frecuencia intermedia de 9 MHz y el oscilador local por encima de la señal. La regla es una sola: **el oscilador local se pone siempre 9 MHz por encima de la emisora que quieres**, para que la diferencia valga 9.

| Quiero escuchar | Pongo el oscilador local en | Diferencia |
|---|---|---|
| 7,1 MHz | 7,1 + 9 = 16,1 MHz | 16,1 − 7,1 = **9 MHz** |
| 14,1 MHz | 14,1 + 9 = 23,1 MHz | 23,1 − 14,1 = **9 MHz** |
| 21,3 MHz | 21,3 + 9 = 30,3 MHz | 30,3 − 21,3 = **9 MHz** |

La emisora cambia. El oscilador local cambia con ella. La diferencia no cambia nunca. Todo lo que hay detrás del mezclador —los filtros, los amplificadores— recibe siempre una señal de 9 MHz y no se entera de en qué banda estás. Cuando giras el dial no estás moviendo ningún filtro: estás cambiando la frecuencia del oscilador local, y la pantalla del equipo hace la resta por ti para enseñarte la frecuencia de la emisora.

—Sigo sin ver la ganancia —dijo Marina—. Has cambiado el problema de sitio. Antes tenía que mover un filtro; ahora tengo que mover un oscilador.

—Es que mover un oscilador es fácil y mover un filtro estrecho es imposible —contestó Vicente—. Un oscilador solo tiene que dar una frecuencia limpia, y eso con un cristal y un sintetizador está resuelto desde hace décadas. He cambiado un problema sin solución por uno resuelto. Eso es media ingeniería.

## El receptor, bloque a bloque

Este es el plano de cajas que el examen pide. Síguelo en el dibujo, de arriba abajo, con el ejemplo de una señal de SSB en 7,1 MHz.

![Esquema de bloques de un receptor superheterodino, de arriba abajo: antena; filtro de entrada y amplificador de radiofrecuencia, que trabajan a la frecuencia de la emisora, 7,1 megahercios; mezclador, al que llega por un lado la señal del oscilador local, 16,1 megahercios; filtro de frecuencia intermedia, a 9 megahercios, donde se consigue la selectividad; amplificador de frecuencia intermedia; demodulador, al que en SSB y CW llega la señal del BFO; amplificador de audio y altavoz.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s07-superheterodino.svg)

**1. Filtro de entrada y amplificador de radiofrecuencia.** Lo primero que encuentra la señal es un filtro paso banda *ancho*, que deja pasar la banda entera en la que estás (toda la banda de 40 metros, por ejemplo) y rechaza lo que queda lejos. No separa emisoras vecinas: solo quita de en medio lo que no pinta nada, y en la lección siguiente verás que tiene además otra misión, muy importante. Después, un amplificador de bajo ruido da el primer empujón a la señal, cuando todavía es diminuta. A este conjunto se le llama *etapa de radiofrecuencia* o *frente de entrada*.

**2. Mezclador y oscilador local.** El mensajero. Traslada la señal de 7,1 MHz a 9 MHz, como viste en la lección anterior.

**3. Filtro de frecuencia intermedia.** El corazón del taller, y **el bloque que da la selectividad al receptor**. Como siempre trabaja a 9 MHz, no tiene que ser ajustable, y puede fabricarse con la mejor tecnología disponible: varios cristales de cuarzo combinados. Recuerda de la sección 5 que un cristal de cuarzo se comporta como un circuito resonante de un factor Q altísimo, cientos de veces mejor que el de cualquier bobina. Con ellos se construyen filtros de 2,4 kHz de ancho para SSB, o de 500 Hz para morse, con unos bordes casi verticales (los técnicos los llaman *flancos*): lo que cae dentro pasa, lo que cae fuera desaparece. El regalo de Amparo era uno de estos. Muchos equipos llevan varios y eligen uno u otro según el modo.

**4. Amplificador de frecuencia intermedia.** Aquí se da la mayor parte de la amplificación. Amplificar mucho a una sola frecuencia fija es mucho más fácil, y da resultados más estables, que hacerlo a lo largo de bandas enteras.

**5. Demodulador.** La señal ya está limpia de vecinos y es grande, pero sigue siendo radiofrecuencia. Falta sacarle el sonido, y cada modo necesita su circuito:

| Modo | Demodulador | Qué hace, en una frase |
|---|---|---|
| AM | **Detector de envolvente** (un diodo) | La *envolvente* es la línea imaginaria que une las crestas de la onda; en AM, esa línea dibuja la voz. El diodo y un condensador la siguen. |
| FM | **Discriminador**, precedido de un **limitador** | El limitador iguala la amplitud (y con ella se va el ruido, como viste en la sección 6); el discriminador convierte los cambios de frecuencia en cambios de tensión, que son el sonido. |
| SSB y CW | **Detector de producto**, con su **BFO** | Otro mezclador (se llama «de producto» porque multiplica): combina la señal de FI con la del BFO, y la diferencia cae directamente en frecuencias audibles. Es la reinserción de portadora de la sección 6. |

**6. Amplificador de audio y altavoz.** La señal ya es audiofrecuencia. Se amplifica hasta poder mover el altavoz o los auriculares.

Para el examen, memoriza la cadena así, en una línea:

> **Antena → filtro y amplificador de RF → mezclador (con su oscilador local) → filtro de FI → amplificador de FI → demodulador → amplificador de audio → altavoz.**

## Tres ayudantes que encontrarás en el panel

Tres circuitos más, que no cambian el plano pero tienen mando o indicador en el panel de todos los equipos:

- **Control automático de ganancia (CAG, en inglés AGC).** Las señales llegan con tamaños muy distintos, y una misma señal sube y baja. El CAG mide, a la salida del demodulador, lo fuerte que llega la señal, y con esa medida gobierna los amplificadores de RF y de FI: reduce su amplificación cuando la señal es fuerte y la aumenta cuando es débil, de modo que el volumen en el altavoz se mantenga parecido. Sin él habría que andar con la mano en el mando de volumen todo el rato.
- **Medidor de señal (S-meter).** La aguja o la barra que indica lo fuerte que llega una estación. Aprovecha precisamente la información del CAG. Su escala va de S1 a S9 y cada punto equivale a 6 dB (el doble de tensión, o cuatro veces la potencia); por encima de S9 se cuenta en decibelios («S9 más 20»). Por convenio, en HF un S9 corresponde a 50 µV en la entrada de antena. Usarás esa escala en la sección 11 para dar reportes.
- **Silenciador (squelch).** En FM, cuando no hay ninguna señal, el receptor entrega un soplido fuerte y muy molesto. El silenciador corta el audio mientras no llega nada y lo abre en cuanto aparece una señal. Su mando fija a partir de qué nivel se abre. La cadena de un receptor de FM termina, por tanto, así: limitador → discriminador → silenciador → amplificador de audio.

## ¿Por qué «super»?

Ya sabes de la lección anterior que *heterodinar* es combinar dos frecuencias para obtener otra. Lo de «super» no es propaganda. Los primeros receptores heterodinos mezclaban para obtener directamente un tono audible. Edwin Armstrong, el ingeniero y militar estadounidense que ideó este receptor en 1918, mezclaba para obtener una frecuencia todavía *por encima* de lo audible —«supersónica», en el lenguaje de entonces—, que luego volvía a tratar. De «supersónico heterodino» quedó *superheterodino*. Más de un siglo después, su plano sigue dentro de casi todos los receptores, del transceptor de Vicente a la radio del coche, incluidos —como verás dentro de dos lecciones— los que hoy hacen parte del trabajo con un programa en lugar de con piezas.

## Donde la gente se lía

- **«La selectividad la da el filtro de la entrada.»** No: el filtro de entrada es ancho y deja pasar la banda entera. La selectividad se consigue en los **filtros de frecuencia intermedia**. Es pregunta de examen muy repetida.
- **«La frecuencia intermedia cambia cuando cambio de emisora.»** Es justo lo que no cambia. Cambia el oscilador local.
- **«El oscilador local está en la misma frecuencia que la emisora.»** Está separado de ella exactamente el valor de la frecuencia intermedia.
- **«El mezclador saca el sonido.»** El mezclador solo traslada la señal a la FI; sigue siendo radiofrecuencia. El sonido lo saca el demodulador, varias cajas después.
- **Confundir oscilador local y BFO.** Los dos son osciladores, pero el local va al primer mezclador y decide qué emisora entra; el BFO va al demodulador y hace audible el morse o la SSB.

## Compruébalo tú

1. Un receptor tiene una FI de 455 kHz y su oscilador local trabaja por encima de la señal. ¿A qué frecuencia se pone el oscilador local para escuchar 3.650 kHz?
2. En ese mismo receptor, el oscilador local está en 14.505 kHz. ¿Qué emisora se está escuchando?
3. Ordena estos bloques tal como los recorre la señal: demodulador, mezclador, amplificador de audio, filtro de FI, amplificador de RF, amplificador de FI.
4. Pasas de escuchar morse a escuchar SSB. ¿Qué bloque conviene cambiar, y en qué?
5. Un receptor oye bien las estaciones de FM, pero entre una y otra suelta un soplido muy fuerte. ¿Qué mando hay que ajustar?
6. ¿Qué demodulador necesita una señal de AM? ¿Y una de CW?

**Soluciones**

1. El oscilador va por encima de la señal, a una distancia igual a la FI: 3.650 + 455 = **4.105 kHz**.
2. La que está 455 kHz por debajo del oscilador: 14.505 − 455 = **14.050 kHz**.
3. Amplificador de RF → mezclador → filtro de FI → amplificador de FI → demodulador → amplificador de audio.
4. El **filtro de FI**: de uno estrecho (unos 500 Hz) a uno de 2,4 a 2,7 kHz, que es lo que ocupa una voz en SSB.
5. El **silenciador** (squelch): se sube hasta que el soplido desaparece.
6. AM: un **detector de envolvente** (un diodo). CW: un **detector de producto con BFO**, porque una portadora que solo se enciende y se apaga no contiene ningún sonido y hay que fabricarle el tono por batido.

## En una frase

El superheterodino traslada cualquier emisora, con un mezclador y un oscilador local ajustable, a una frecuencia intermedia fija, y allí la filtra con filtros de cristal que no necesitan moverse; luego la amplifica, la demodula y la convierte en sonido.

El invento tiene un precio, y el examen lo pregunta casi siempre. El mezclador es demasiado honrado: hay *otra* frecuencia que también le sirve.
