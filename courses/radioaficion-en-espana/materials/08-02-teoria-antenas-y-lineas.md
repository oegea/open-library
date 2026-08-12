Ningún componente de tu estación importa más que la antena. Un transceptor mediocre con una antena excelente hace contactos toda la noche; el equipo más caro del mercado con una mala antena escucha ruido de lujo. Esta sección —de las más preguntadas del examen— te da la física de por qué un hilo radia, el catálogo de antenas fundamentales, y el asunto que une equipo, cable y antena: impedancia, ROE y líneas de transmisión.

## Por qué radia un hilo

Recuerda la sección 6: una corriente alterna crea campos eléctrico y magnético oscilantes que, si la frecuencia es suficiente, se independizan y vuelan. Una **antena** no es más que un conductor *dimensionado a propósito* para que esa fuga sea máxima: un trozo de circuito diseñado para perder energía elegantemente hacia el espacio.

¿Y por qué el tamaño importa tanto? Por resonancia. Una antena es, eléctricamente, un circuito resonante estirado: tiene su frecuencia natural, a la que la corriente y la tensión se distribuyen en ondas estacionarias perfectas a lo largo del hilo y la radiación es máxima con mínimo esfuerzo. Esa frecuencia natural depende de su longitud física comparada con la longitud de onda. Una antena «a medida» de su banda trabaja sola; una antena de medida equivocada hay que forzarla (se puede, con acopladores, pagando rendimiento). De ahí la obsesión de este oficio con los metros y centímetros: la regla de Amparo, la cinta métrica de la azotea.

**El factor de acortamiento:** la onda viaja por el hilo algo más despacio que por el vacío (y los extremos de la antena añaden efectos capacitivos), así que la antena real se corta ~5 % más corta que la teoría del espacio libre: el «pellizco» que recortaron en la azotea. Para el dipolo práctico se usa la fórmula con 0,95 incorporado: **longitud total (m) ≈ 142,5 / f (MHz)** (media onda ya acortada).

## El dipolo de media onda: la antena patrón

El **dipolo de media onda** es la antena fundamental, la referencia con la que se comparan todas: dos brazos conductores de un cuarto de onda cada uno (media onda en total), alimentados por el centro, donde se conecta la línea que viene del equipo.

Su carné de identidad (todo esto cae en examen):

- **Longitud:** λ/2 (con el 5 % de acortamiento: 142,5/f). Para 7,1 MHz: 142,5/7,1 ≈ 20,1 m totales, los diez metros y pico por brazo de Marina.
- **Impedancia en el punto de alimentación: ~73 Ω** en el espacio libre (en la práctica, entre 50 y 75 Ω según la altura sobre el suelo). Enseguida verás por qué este número es una bendición.
- **Distribución:** la corriente es máxima en el centro y nula en las puntas; la tensión, al revés (máxima en las puntas: por eso los extremos «muerden» con RF y se alejan de lo tocable). Alimentarlo por el centro es conectarse donde la corriente manda.
- **Diagrama de radiación:** radia máximo en las direcciones *perpendiculares* al hilo y casi nada por las puntas: visto desde arriba, un ocho (∞). No es omnidireccional: un dipolo tendido norte-sur favorece este-oeste.
- Colocado horizontal es la antena clásica de HF; su altura sobre el suelo importa muchísimo (a más de media onda de altura, ángulos de salida bajos, mejores para larga distancia: el porqué madurará en la sección 9).

## El monopolo de cuarto de onda: medio dipolo y un espejo

¿No caben 20 metros de hilo? El **monopolo vertical de cuarto de onda** usa un truco de espejo: un solo brazo de λ/4 vertical, y en lugar del segundo brazo, un **plano de tierra** conductor (la tierra real mejorada con **radiales** —hilos extendidos por el suelo— o, en antenas elevadas y de coche, la chapa o varios radiales elevados). El plano refleja la antena como un espejo eléctrico: el sistema se comporta como un dipolo completo del que solo has construido la mitad.

- **Longitud:** λ/4 (la vertical blanca de Vicente para 40 m: unos 10 m).
- **Impedancia: ~36 Ω** (justo la mitad del dipolo: has construido media antena).
- **Radiación omnidireccional** en el plano horizontal (no favorece ninguna dirección) y de polarización vertical.
- Su rendimiento depende críticamente de la calidad del plano de tierra: pocos radiales o suelo pobre = vatios calentando lombrices. La mítica frase de club: «una vertical rinde lo que rinde su tierra».
- Es la arquitectura de las antenas de coche, de los walkies (con tu cuerpo y la placa del equipo como contrapeso), y de las emisoras de onda media.

## La yagi: apilar los deberes en una dirección

La **yagi** (Yagi-Uda, 1926, invento japonés que Occidente tardó en valorar... hasta que la encontró en los radares japoneses de la Segunda Guerra Mundial) añade al dipolo elementos *parásitos* —varillas no conectadas a nada, solo colocadas con precisión—:

- Un **reflector** detrás (algo más largo que el dipolo): rebota la energía hacia delante.
- Uno o varios **directores** delante (algo más cortos): enfocan la radiación.

El resultado es la antena de televisión de toda la vida y la reina de los concursos: concentra la radiación en una dirección (**ganancia**) a costa de las demás, y hay que **orientarla** (de ahí los rotores). Ganancias típicas: 5-6 dB una yagi pequeña de 3 elementos, 10 dB o más las grandes. Recuerda qué es la ganancia de antena: no crea energía; *redistribuye* la tuya, como una linterna frente a una bombilla.

**Las unidades de la ganancia, matiz de examen:** **dBi** = ganancia respecto a la antena *isotrópica* (radiador ideal que reparte igual en todas direcciones: no existe, es la referencia matemática); **dBd** = respecto al dipolo. Como el dipolo ya tiene 2,15 dBi de ganancia sobre la isotrópica, **dBd = dBi − 2,15**. Truco publicitario clásico: anunciar en dBi para que el número parezca mayor. Ahora ya no te la cuelan.

**Menciones de catálogo** que conviene reconocer: la **antena de hilo largo** (un hilo de varias longitudes de onda, alimentado en un extremo, con acoplador: sencilla y multiuso), la **G5RV y los dipolos multibanda**, las **verticales multibanda con trampas** (circuitos LC que «cortan» eléctricamente la antena a distintas frecuencias: ¡el columpio otra vez, trabajando de tijera!), y el **cuadro o loop**. Cada una es un compromiso distinto entre espacio, bandas y rendimiento.

## Impedancia: el acuerdo entre las partes

Toca el concepto que une estación entera. Cada elemento del sistema —la salida del transmisor, el cable, la antena— tiene su **impedancia** (esa oposición compleja a la corriente alterna, en ohmios, que conociste en la sección 5). La regla de oro de la transferencia de energía: **la potencia pasa íntegra de un elemento a otro cuando sus impedancias coinciden** («adaptación» o *matching*). Si no coinciden, parte de la energía **se refleja** en la frontera y vuelve por donde vino, como una ola contra un malecón.

El estándar universal de la radio es **50 Ω**: los transmisores salen a 50 Ω, los cables se fabrican de 50 Ω, y las antenas... las antenas dan lo que dan (73 el dipolo, 36 la vertical), pero se diseñan y ajustan para acercarse. La cadena feliz: transmisor 50 → cable 50 → antena ≈50 = toda la potencia al aire.

## ROE: el medidor del acuerdo

La **ROE** (Relación de Ondas Estacionarias; en inglés **SWR**) mide cuánta energía se refleja por desacuerdo de impedancias. Es EL número de la práctica de antenas y pregunta segurísima de examen:

- **ROE 1:1** — adaptación perfecta: nada se refleja. El 1,2 de la azotea: excelente.
- **ROE 1,5:1** — reflejo del 4 % de la potencia: bien.
- **ROE 2:1** — reflejo del 11 %: aceptable, límite de confort de muchos equipos.
- **ROE 3:1** — reflejo del 25 %: mal asunto; los transmisores modernos se autoprotegen recortando potencia.
- **ROE infinita** — cable cortado o en cortocircuito: todo vuelve.

Matices que separan al que entiende del que repite:

- La potencia reflejada **no se pierde toda** (rebota de nuevo en el transmisor y parte vuelve a salir): el daño principal de una ROE alta no es «la potencia que se pierde», sino que **el transmisor sufre** (tensiones y corrientes elevadas en su etapa final: por eso se protege) y que **el cable pierde más** (la energía que va y viene por un cable con pérdidas paga peaje en cada viaje).
- La ROE se mide con el **medidor de ROE** (reflectómetro) intercalado en la línea, o con el **analizador de antenas** que usó Dani (que además dibuja la curva de resonancia completa).
- El **acoplador de antena** («tuner») es una caja de bobinas y condensadores ajustables que *transforma* la impedancia que ve el transmisor hasta darle sus 50 Ω amados. Importante entender qué hace y qué no: contenta al transmisor (que ya no se protege), pero **no arregla la antena**: el desacuerdo entre cable y antena sigue donde estaba, con sus pérdidas de ida y vuelta en el cable. Es un diplomático, no un cirujano. Con antenas razonables y cables cortos, diplomático sobra.

## Líneas de transmisión: el viaje hasta la antena

La **línea de transmisión** lleva la RF del equipo a la antena. La dominante es el **cable coaxial**: conductor central, aislante (dieléctrico), malla de blindaje y cubierta. Su blindaje lo hace insensible a lo que toca (se puede grapar, enterrar, pasar junto a canalones) y por eso ganó la partida al viejo «hilo paralelo» (línea bifilar, dos hilos separados: menos pérdidas, pero delicada de instalar: nada metálico cerca).

Lo que hay que saber del coaxial:

- **Impedancia característica:** 50 Ω en radio (75 Ω en TV: parecidos, no intercambiables sin consecuencias). No depende de la longitud: la fijan los diámetros y el dieléctrico.
- **Pérdidas:** el cable roba una fracción de la potencia (en dB por cada 100 m), y aquí la regla crucial: **las pérdidas crecen con la frecuencia**. Un RG-58 finito de 30 m pierde ~1,5 dB en 7 MHz (tolerable) pero ~4,5 dB en 145 MHz (¡dos tercios de tu potencia calentando cable!). Por eso «el barato se come los vatios como churros», sobre todo en V/UHF, y por eso en VHF/UHF se usan coaxiales gordos de baja pérdida y longitudes cortas. Dinero en cable rinde más que dinero en vatios.
- Conectores habituales: **PL-259/SO-239** (el clásico de HF), **BNC** (bayoneta, portátiles), **N** (roscado, estanco, el serio para V/UHF y potencias).

## El balun y la carga artificial: dos auxiliares con oficio

- **Balun** (*BALanced-UNbalanced*): transformador (a menudo unas vueltas de cable sobre un toroide de ferrita: el yoyó de Dani) que casa una línea *asimétrica* (el coaxial, con su vivo y su malla a tierra) con una antena *simétrica* (el dipolo, con sus dos brazos iguales). Sin él, la corriente de RF encuentra un tercer camino: **volver por el exterior de la malla del coaxial**, convirtiendo tu propio cable en antena involuntaria que radia hacia abajo, hacia tu casa y la del vecino: RF «en la choza», interferencias, y el diagrama de la antena deformado. Un balun de choque en el punto de alimentación cierra esa puerta. (Los baluns también existen en versión transformadora de impedancias: 4:1, 9:1, para antenas de impedancias exóticas.)
- **Carga artificial** (*dummy load*): una resistencia pura de 50 Ω capaz de tragarse la potencia del transmisor **sin radiar** (apenas). Para probar y ajustar el equipo sin salir al aire: obligatoria en toda estación seria y exigida por la buena práctica (ajustar transmitiendo por la antena es ensayar la trompeta en el rellano). Recuerda: 50 Ω resistivos, ROE 1:1 perfecta, y silencio hacia el mundo.

## Para llevar

- La antena es un circuito resonante estirado: su longitud fija su frecuencia; fórmula práctica del dipolo: **L(m) = 142,5 / f(MHz)** (media onda con acortamiento del 5 %).
- **Dipolo λ/2:** ~73 Ω, alimentado al centro (máximo de corriente), radia en ocho perpendicular al hilo.
- **Monopolo λ/4:** ~36 Ω, necesita plano de tierra/radiales (su rendimiento es su tierra), omnidireccional, polarización vertical.
- **Yagi:** reflector + directores = ganancia direccional; **dBd = dBi − 2,15**; la ganancia redistribuye, no crea.
- **Adaptación:** todo a 50 Ω; el desacuerdo refleja energía; la **ROE** lo mide (1:1 perfecta; 2:1 aceptable; 3:1 protección). El acoplador contenta al transmisor pero no arregla la antena.
- **Coaxial:** 50 Ω, pérdidas que crecen con frecuencia y longitud: cable bueno y corto, sobre todo en V/UHF.
- **Balun:** evita que la malla del coaxial radie (corriente de modo común); **carga artificial:** 50 Ω que no radian, para pruebas.

## Para el examen

- Longitud del dipolo y del monopolo para una frecuencia dada (con 142,5/f o el λ/2 teórico: lee qué pide el enunciado): cae constantemente.
- Impedancias típicas: dipolo ~73 Ω, vertical λ/4 ~36 Ω, coaxial 50 Ω.
- Qué es la ROE, valores buenos/malos, con qué se mide y qué consecuencias tiene alta.
- Diagramas: dipolo = ocho; vertical = omni; yagi = directiva (y papeles del reflector/director).
- dBi vs dBd (la resta 2,15 se pregunta).
- Pérdidas del coaxial: crecen con frecuencia y longitud.
- Función del balun y de la carga artificial: preguntas directas habituales.

## Para profundizar

- *Ética y procedimientos operativos para el radioaficionado* (IARU): poco de antenas, pero su insistencia en señales limpias empieza en esta sección: antena adaptada = transmisor feliz = señal limpia.
- Los manuales de antenas clásicos (el *ARRL Antenna Book* si el inglés no te asusta) son pozos sin fondo; para empezar, cualquier calculadora de dipolos online y una tarde con hilo, aisladores de plástico y el analizador del club: la antena de la azotea de Marina cuesta menos de 30 € en materiales. Es el mejor euro-por-decibelio de toda la radio.
- Software gratuito de simulación de antenas (MMANA-GAL, 4nec2): dibuja el dipolo de la historia y mira su «ocho» girar en 3D. Ver el diagrama entender por qué la orientación importa.
