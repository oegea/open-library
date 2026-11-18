Aquella noche, Marina abrió en el portátil un receptor de los de websdr.org y se quedó hasta la una mirando la cascada: columnas anchas, penachos de un solo lado, hilos intermitentes y, en una esquina, una franja de rayitas que parpadeaban todas a la vez cada quince segundos. Las tres primeras cosas ya sabes lo que son. La cuarta es el tema de esta lección: los modos en los que no habla una persona, sino un ordenador.

Al terminar sabrás qué hace distinto a un modo digital, por qué algunos descifran señales que el oído no llega a percibir y qué son los que más oirás nombrar.

## Qué es un modo digital

Todos los modos que has visto hasta ahora, salvo el morse, transmiten algo *continuo*: una voz, con sus infinitos matices. Un **modo digital** transmite otra cosa: una lista de **símbolos** tomados de un repertorio pequeño y fijo.

El repertorio más pequeño posible tiene dos símbolos: sí o no, uno o cero. A cada una de esas decisiones entre dos opciones se le llama **bit**. Con grupos de bits se representa cualquier cosa: una letra, un número, una posición en el mapa. Un ordenador convierte el texto en bits antes de enviarlo y los bits en texto al recibirlo.

> **Modo digital:** modo en el que la información se envía como una sucesión de símbolos de un repertorio fijo, que genera y descifra un ordenador o un circuito especializado.

Visto así, el morse fue el primer modo digital de la historia: dos símbolos, punto y raya, que un ser humano descifra de oído. Los modos digitales modernos dejan ese trabajo a una máquina, que es más rápida y, sobre todo, más paciente.

¿Cómo se suben esos símbolos a la portadora? De las tres maneras que conoces desde la lección 2, y nada más:

| Lo que se cambia para pasar de un símbolo a otro | Nombre técnico | Ejemplo |
|---|---|---|
| Portadora encendida o apagada | Manipulación de amplitud | El morse |
| La frecuencia salta entre dos o más valores fijos | **FSK** (manipulación por desplazamiento de frecuencia) | RTTY, FT8 |
| La fase da un salto: la onda se invierte de golpe y, donde tocaba cresta, sale valle (un salto de 180°) | **PSK** (manipulación por desplazamiento de fase) | PSK31 |

A la cantidad de símbolos que se envían cada segundo se le llama velocidad en **baudios**. Un modo de 45 baudios envía 45 símbolos por segundo.

Baudios y bits por segundo no son siempre lo mismo, y conviene saberlo por si lo ves nombrado. Si en cada símbolo se elige entre dos valores, cada símbolo lleva 1 bit. Pero si se elige entre cuatro —por ejemplo, entre cuatro fases distintas, lo que se llama **QPSK**—, cada símbolo lleva 2 bits, y a 45 baudios pasan 90 bits por segundo. Combinando varias fases con varias amplitudes (**QAM**) caben aún más bits en cada símbolo. Es la manera de enviar más datos sin cambiar más veces por segundo.

—¿Y hace falta una emisora especial? —preguntó Marina.

—La misma del club —dijo Dani—. El ordenador fabrica unos tonos de audio, como si silbara, y se los mete al transmisor por la entrada del micrófono, en SSB. ¿Recuerdas qué pasa cuando silbas en SSB?

—Que sale una portadora.

—Pues eso. Un silbido que cambia de nota es una portadora que cambia de frecuencia. El ordenador silba, la emisora lo convierte en radio, y al otro lado otro ordenador escucha los silbidos por el altavoz y los traduce. Por convenio, en USB en todas las bandas; la única excepción con solera es el RTTY, que por tradición va en LSB.

## El truco: decir poco, muy despacio y con paciencia

Los modos digitales de señal débil consiguen algo que parece magia: completar un contacto con señales que no se oyen. No es magia; son las tres ideas que ya tienes, llevadas al límite.

**Primera: decir muy poco por segundo.** La regla de la lección 2 decía que a menos información por segundo, menos ancho de banda. Un modo que tarda quince segundos en enviar una frase de trece letras puede caber en una franja de 50 Hz.

**Segunda: escuchar por una rendija.** Con el morse viste que el ruido está repartido por todo el dial y que, cuanto más estrecha es la franja que se abre, menos ruido entra. Un ordenador puede mirar una rendija de unos pocos hercios. Ahí dentro el ruido es mínimo, y una señal debilísima, que en la franja de 2.700 Hz de la voz quedaría sepultada, sobresale.

**Tercera: repetir con astucia.** Estos modos añaden al mensaje bits de sobra, calculados de tal modo que, si una parte llega estropeada, el ordenador puede deducir lo que faltaba. Se llama *corrección de errores*. Otros sistemas de datos más sencillos (como el packet, que aparece un poco más abajo) no corrigen: añaden al mensaje una suma de comprobación (se abrevia **CRC**) y, si al recibirlo la suma no cuadra, piden que se repita.

Por eso se dice que el modo FT8 descifra señales «a 20 decibelios por debajo del ruido». La frase tiene truco, y conviene entenderla: quiere decir que la señal es cien veces más débil que el ruido que entra en una franja de voz. Nuestro oído, que escucha esa franja entera, no percibe nada. El ordenador, que escucha solo la rendija donde está la señal, sí.

## Los modos que oirás nombrar

**RTTY** (radioteletipo; se pronuncia «ritty»). El abuelo, en uso desde los años treinta. La portadora salta entre dos frecuencias separadas 170 Hz, una para los unos y otra para los ceros, a 45 baudios. Suena como un gorjeo rápido y ocupa unos 250 Hz. Todavía se usa mucho en concursos.

**PSK31** (1998). Cambia la fase en lugar de la frecuencia, a 31 baudios, y ocupa entre **31 y 60 Hz**, según cómo se mida: menos que el morse. Está pensado para conversar tecleando en directo, con potencias muy bajas. Suena como un silbido tembloroso.

**FT8** (2017). El fenómeno de los últimos años, y lo que Vicente, citando a Amparo, llama «notaría». Sus rasgos:

- Los mensajes son cortísimos y tienen forma fija: los indicativos de las dos estaciones, un código de cuatro caracteres que dice en qué zona del mapa está cada una (el *localizador*) y una cifra que indica con qué fuerza se reciben (el *informe de señal*). Nada más.
- Cada transmisión dura unos 13 segundos dentro de turnos exactos de **15 segundos**, sincronizados con el reloj. Todas las estaciones del mundo empiezan y acaban sus turnos en los mismos instantes, unas transmitiendo en los turnos pares y otras en los impares: por eso las rayitas de la cascada parpadeaban al unísono.
- Ocupa **50 Hz**. En la franja de una sola conversación de voz caben decenas de contactos simultáneos.
- Descifra señales hasta unos 20 dB por debajo del ruido.

El resultado es el que Dani presumía: 143 países desde un balcón con una antena modesta. Y el precio es el que Vicente le reprocha: el intercambio es mínimo y lo hace prácticamente solo el ordenador, sin conversación. Técnicamente es un prodigio; socialmente, un sello en un pasaporte. Los dos tienen razón, y lo sensato es lo que decía Amparo: cada modo cuenta una parte del mundo que los otros no ven.

**Voz digital (DMR, D-STAR, C4FM).** Aquí lo que se convierte en bits es la propia voz. Se usa en VHF y UHF, con portátiles parecidos a los de FM y repetidores que además se enlazan entre sí por Internet. Son tres sistemas de orígenes distintos, incompatibles entre sí. El sonido es limpio mientras hay señal y se corta bruscamente cuando falta.

**Packet y APRS.** Datos por radio en VHF: mensajes cortos, telemetría y, sobre todo, posiciones. El sistema APRS dibuja en un mapa estaciones en movimiento, globos y estaciones meteorológicas. En Europa funciona en 144,800 MHz.

Para el examen no hace falta dominarlos. Basta con saber que existen, reconocer sus nombres y recordar la idea central: usan técnicas digitales para comunicar con muy poco ancho de banda o con señales muy débiles.

## Donde la gente se lía

- **«Los modos digitales necesitan Internet.»** No. Son radio pura: la señal va de antena a antena. El ordenador solo genera y descifra los tonos. (La voz digital por repetidores sí puede usar Internet para enlazar un repetidor con otro, pero eso es un añadido.)
- **«Descifrar por debajo del ruido es imposible; será un truco.»** Es por debajo del ruido que entra en una franja de voz. En la rendija estrecha que mira el ordenador, la señal está por encima.
- **«Digital significa mejor calidad.»** Significa otra cosa: símbolos en lugar de una señal continua. Según el modo, eso se usa para llegar más lejos, para ocupar menos o para añadir servicios.
- **«Con FT8 se puede charlar.»** No. Sus mensajes tienen forma fija y son mínimos. Para conversar tecleando hay otros modos, como PSK31 o RTTY.
- **«Baudios y bits por segundo son lo mismo.»** Solo cuando cada símbolo lleva un bit. Si cada símbolo elige entre cuatro valores, lleva dos bits, y los bits por segundo son el doble que los baudios.

## Compruébalo tú

1. ¿Cuántas señales de FT8, de 50 Hz cada una, caben en el ancho de una sola señal de SSB de 2.700 Hz?
2. Un modo envía 31 símbolos por segundo. ¿Cuál es su velocidad en baudios?
3. Un modo trabaja a 300 baudios y cada símbolo puede tomar cuatro valores distintos. ¿Cuántos bits por segundo transmite?
4. Una señal llega 20 dB por debajo del ruido. ¿Cuántas veces más débil que el ruido es, en potencia?
5. ¿Cuántos turnos de FT8 caben en un minuto? Si una estación transmite en uno de cada dos, ¿cuántas veces transmite por minuto?
6. ¿En qué banda lateral se pone el transmisor para FT8 en la banda de 40 metros? ¿Y para hablar en esa misma banda?

**Soluciones**

1. 2.700 / 50 = **54 señales**.
2. **31 baudios**: el baudio es precisamente un símbolo por segundo.
3. Elegir entre cuatro valores son 2 bits por símbolo: 300 × 2 = **600 bits por segundo**.
4. Recuerda la tabla de la sección 3: −10 dB es dividir entre 10, y −20 dB, entre 100. Es **cien veces** más débil.
5. 60 / 15 = **4 turnos** por minuto. Transmitiendo en uno de cada dos, **2 veces** por minuto; en los otros dos turnos, escucha.
6. Para FT8, **USB**, como casi todos los modos digitales en cualquier banda. Para voz en 40 metros, **LSB**, porque está por debajo de 10 MHz.

## En una frase

Un modo digital envía símbolos en lugar de una señal continua, y los más eficaces descifran señales inaudibles porque dicen muy poco por segundo, lo escuchan por una rendija mínima y corrigen los errores.

Ya conoces todos los modos. En la última lección de la sección aprendes a reconocerlos de un vistazo y a situar cada uno en su sitio.
