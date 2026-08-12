Gramática aprendida. Esta ampliación cuenta lo que la teoría no tuvo espacio para contar: de dónde salió el hercio, por qué Europa late a 50 Hz y América a 60, la guerra industrial que decidió que tu enchufe fuera alterno, y la historia del decibelio, que empezó midiendo kilómetros de cable telefónico.

## Hertz, el hombre que no le vio utilidad

Heinrich Hertz demostró las ondas electromagnéticas en 1887 con un montaje de una elegancia brutal: un chispero emisor y, al otro lado del laboratorio, un simple aro de cobre con un huequecito microscópico. Cuando el chispero saltaba, en el hueco del aro —sin cable alguno de por medio— saltaba una chispita hermana. Esa chispita de milímetros es el tatarabuelo de todos los receptores. A Hertz se le atribuye haber dicho que aquello «no servía para nada; es solo un experimento que demuestra que el maestro Maxwell tenía razón». Murió en 1894, a los 36 años, sin ver que Marconi convertiría su chispita en industria mundial en menos de una década. En 1930 la unidad de frecuencia recibió su nombre; hasta entonces se decía «ciclos por segundo», y en libros y esquemas viejos (y en boca de radioaficionados veteranos) todavía encontrarás «kilociclos» y «megaciclos». Si un día Vicente dice «catorce megaciclos», ya sabes que son 14 MHz y que estás hablando con historia viva.

## Por qué 50 Hz (y por qué los aviones van a 400)

La frecuencia de la red eléctrica fue una decisión de ingeniería con margen de gusto: demasiado baja (menos de ~40 Hz) y las lámparas de la época parpadeaban visiblemente; demasiado alta y los transformadores y motores de entonces sufrían más pérdidas. AEG en Europa estandarizó 50 Hz; Westinghouse en América, 60 Hz, y cada mitad del mundo heredó la costumbre de sus proveedores. No hay un ganador técnico claro: son dos convenciones vecinas. La consecuencia curiosa está en los aviones: su red interna va a **400 Hz**, porque a más frecuencia los transformadores y motores necesarios son mucho más pequeños y ligeros (la razón la entenderás del todo con las bobinas de la sección 4), y en un avión el peso es oro. ¿Por qué no 400 Hz en tierra? Porque a esa frecuencia las pérdidas en líneas largas se disparan: 400 Hz solo funciona en redes cortas. Cada frecuencia tiene su hábitat: es la primera lección del espectro, repetida en miniatura dentro de un fuselaje.

## La guerra de las corrientes: Edison contra la alterna

En los años 1880, Thomas Edison había desplegado redes de corriente continua y defendía su inversión con uñas y dientes. George Westinghouse, con las patentes del genial Nikola Tesla, empujaba la alterna, que gracias al transformador podía viajar a alta tensión (pocas pérdidas) y bajarse a tensión doméstica en destino. La CC de Edison no podía hacer eso con la tecnología de la época, y la física era tozuda: perdía la partida. Edison respondió con una campaña de miedo que incluyó electrocuciones públicas de animales «para demostrar el peligro de la alterna» y presionar para que la primera silla eléctrica usara CA (buscaba que «morir electrocutado» se dijera «ser *westinghoused*»). No le funcionó: la Feria Mundial de Chicago de 1893 se iluminó con alterna de Westinghouse, las cataratas del Niágara se electrificaron con ella y el asunto quedó zanjado durante un siglo.

Epílogo con ironía histórica: hoy, los enlaces eléctricos de muy larga distancia y los submarinos (como los que unen la Península con Baleares) vuelven a ser de **corriente continua** en alta tensión (HVDC), porque con la electrónica de potencia moderna la CC ya sí puede transformarse y, en cables muy largos, pierde menos que la alterna. Edison ganó al final una batalla póstuma... con tecnología que ni él ni Tesla podían imaginar.

## El decibelio nació midiendo cansancio de cables

El decibelio no lo inventaron los locutores ni los sonidistas: lo inventó la compañía telefónica Bell hacia 1924. Su problema era prosaico: cuantificar cuánta señal se perdía por milla de cable telefónico. La primera unidad se llamó, literalmente, «milla de cable estándar» (*Mile of Standard Cable*): un circuito perdía «tantas millas». Al estandarizarla la rebautizaron **bel** en honor a Alexander Graham Bell, pero el bel resultó ser una unidad demasiado gorda (¡×10 de un salto!), así que el uso cotidiano se quedó con su décima parte: el **decibelio**. Detalle bonito: la «milla de cable estándar» original equivalía a ~0,95 dB, o sea que la nueva unidad científica quedó casi calcada a la vieja unidad artesanal, para no descolocar a los técnicos veteranos. Hasta las unidades hacen transiciones suaves.

¿Y por qué logarítmico? Por dos motivos que se refuerzan: los números de la telecomunicación abarcan órdenes de magnitud (y el logaritmo los comprime a cifras manejables), y además la percepción humana —del volumen, del brillo— es aproximadamente logarítmica: para que algo «suene el doble de fuerte» hace falta cerca de diez veces más potencia. El decibelio habla a la vez el idioma de los cables y el del oído.

## S-metros y microvoltios: el decibelio que verás en tu primer equipo

En cuanto enciendas un receptor verás una aguja o barra marcada **S1...S9**: el **S-meter** (medidor de intensidad de señal). Es puro decibelio disfrazado: por convención de la IARU Región 1, cada punto S equivale a **6 dB** (×4 en potencia), y S9 corresponde a 50 µV en la entrada del receptor en HF. Cuando un corresponsal te diga «me llegas S8», te está diciendo, en escala logarítmica, exactamente cuánto empuja tu señal en su antena. Y las señales «S9 +20 dB» de los días buenos son eso: cien veces más potencia que S9. El reporte de señal completo (el famoso RST) te lo enseñaremos en la sección 11; el S-meter era su mitad instrumental.

## Fourier, o por qué el zoológico del dial se puede domesticar

La teoría te dijo que toda onda periódica equivale a una suma de senoides (fundamental + armónicos). La idea es de Joseph Fourier, que la publicó en 1822 estudiando... la propagación del calor. Los matemáticos de su tiempo (Lagrange incluido) la recibieron con escándalo: ¿cualquier forma, hasta una onda cuadrada con esquinas, suma de curvas suaves? Pues sí. Dos siglos después, esa idea es posiblemente el teorema más *usado* del planeta: cada segundo, tu móvil, la TDT, el wifi y el receptor SDR con el que mirarás el espectro ejecutan millones de **transformadas de Fourier** (en su versión rápida, la FFT, redescubierta en 1965) para descomponer señales en sus frecuencias. Aquella «cascada» de colores que verás caer en la pantalla de un SDR, con cada emisora en su columna, es la transformada de Fourier dibujada en tiempo real: el zoológico entero del dial, ordenado por especies matemáticamente. Cuando Vicente dice que «cada ruido es alguien diciendo algo de una manera distinta», Fourier es el traductor.

## Tres divisiones de cabeza, de regalo

La fórmula de los trescientos da juego mental. Tres perlas para presumir en el radioclub:

- **Tu microondas:** 2.450 MHz → λ = 300/2450 ≈ 12 cm. Por eso la rejilla de la puerta te deja ver dentro sin cocinarte: sus agujeros de milímetros son minúsculos comparados con 12 cm, y la onda «no cabe» por ellos. Las longitudes de onda no atraviesan agujeros mucho menores que ellas: el mismo principio protege (o estorba) en las antenas dentro de coches.
- **La onda del enchufe:** 50 Hz → λ = 300.000.000/50 = **6.000 kilómetros**. La red eléctrica europea entera es «eléctricamente corta»: cabe en una fracción de su propia onda. Por eso tu instalación doméstica no radia como antena (menos mal).
- **El wifi de tu casa:** 2,4 GHz y 5 GHz → 12,5 y 6 cm. Ondas cortísimas que rebotan mal en paredes gruesas: ahora ya sabes por qué el router no llega al trastero, y de paso, por qué las bandas bajas «llegan más lejos» será un tema serio en la sección 9.

## Para seguir tirando del hilo

- Wikipedia (CC BY-SA): «Guerra de las corrientes», «Heinrich Hertz», «Decibelio» y «Serie de Fourier» — artículos bien referenciados para cada historia de esta ampliación.
- El vídeo del canal 3Blue1Brown «But what is a Fourier series?» (en inglés, subtitulado): la visualización más bella que existe de la suma de senoides.
- En websdr.org, abre cualquier receptor y mira la cascada: intenta distinguir a ojo una emisora de AM (columna ancha con espinazo central) de una de morse (hilo finísimo). Estás leyendo transformadas de Fourier. En la sección 6 les pondremos nombre a todas las especies.
