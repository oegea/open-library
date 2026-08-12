Un transceptor moderno tiene dos mil componentes y una docena de ideas. Esta sección te da las ideas: los bloques del receptor y del transmisor, el truco central que Vicente llama «el taller de frecuencia fija», y las tres o cuatro cifras de mérito con las que se juzga a los equipos. Es una sección densa en conceptos de examen: receptores y transmisores son dos capítulos completos del temario oficial.

## El problema del receptor

Un receptor tiene un trabajo brutal: en su antena entran *a la vez* todas las señales del planeta —emisoras de megavatios y susurros de picovatios, separadas a veces por un pelo de frecuencia— y debe quedarse con una sola, amplificarla millones de veces y convertirla en audio limpio. Sus tres virtudes se llaman:

- **Sensibilidad:** capacidad de oír señales débiles. Se mide en microvoltios (µV) o dBm: cuanto menor la señal utilizable, más sensible el receptor. El límite no lo pone la amplificación (amplificar es barato), sino el **ruido**: el generado por el propio receptor y el que entra por la antena. Amplificar una señal enterrada en ruido amplifica también el ruido: la clave es añadir el mínimo ruido propio.
- **Selectividad:** capacidad de separar la señal deseada de las vecinas pegadas a ella. La dan los filtros (paso banda, ya los conoces) y es la diferencia entre copiar una señal débil o que te la pise el vozarrón de al lado.
- **Estabilidad:** quedarse clavado en la frecuencia sintonizada sin derivar con la temperatura o el tiempo. La resuelve el cristal de cuarzo y sus descendientes (PLL/DDS).

## La solución elegante: el superheterodino

Podrías intentar el enfoque directo: un filtro sintonizable que siga al dial y amplificadores detrás. Se hizo (receptores de radiofrecuencia sintonizada, años veinte) y era un tormento: filtros buenos *y* móviles es pedir peras al olmo; a frecuencias altas, ni con peras.

En 1918, Edwin Armstrong (sí, otra vez él) invirtió el problema con el **receptor superheterodino**, el diseño que domina desde entonces: *si no puedes llevar el taller a la señal, trae la señal al taller*.

La pieza clave es el **mezclador**: un circuito no lineal al que entran dos señales y del que salen, además de las originales, su **suma y su diferencia** de frecuencias (el «heterodinaje» que ya conociste en el BFO). El receptor funciona así:

1. **Frente de entrada:** un filtro paso banda ancho selecciona la banda de interés y un amplificador de RF de bajo ruido da un primer empujón educado.
2. **Mezclador + oscilador local (OL):** la señal entrante se mezcla con la señal de un oscilador local *ajustable* (el que de verdad mueves con el dial). De la mezcla interesa la **diferencia**: se elige el OL de modo que, sea cual sea la emisora sintonizada, la diferencia caiga siempre en la misma frecuencia fija, la **frecuencia intermedia (FI)**. Ejemplo con números: FI = 9 MHz; para escuchar 14,2 MHz, el OL se pone a 23,2 MHz (23,2 − 14,2 = 9). ¿Quieres 7,1 MHz? OL a 16,1. La emisora cambia; la diferencia, jamás.
3. **La cadena de FI: el taller.** Como la FI es fija, sus filtros son fijos: cristales de cuarzo tallados para esa frecuencia exacta, con selectividades soberbias imposibles en un filtro móvil (el filtro estrecho de CW que Amparo soldó era uno de estos). Aquí vive la selectividad del receptor, y aquí se amplifica la señal a placer.
4. **Demodulador:** según el modo: detector de envolvente para AM, discriminador para FM, mezcla con el BFO para CW/SSB (la reinserción de portadora de la sección 6).
5. **Amplificador de audio → altavoz.** Fin del viaje.

**El peaje del invento: la frecuencia imagen.** El mezclador es honesto: da la diferencia con *cualquiera* que diste 9 MHz del OL, por arriba o por abajo. Con OL en 23,2 y FI de 9, la deseada es 14,2... pero una señal en 32,2 MHz (23,2 + 9) también produce 9 MHz de diferencia y entraría como un fantasma indistinguible. Esa intrusa es la **frecuencia imagen** (siempre a 2×FI de la deseada), y se combate con el filtro del frente de entrada (que deje pasar 14,2 y aplaste 32,2) y eligiendo FI altas (cuanto más lejos esté la imagen, más fácil filtrarla). Muchos equipos usan **doble conversión** (dos FI: una alta para alejar la imagen, otra baja para filtrar fino): más mezcladores, más osciladores, mismo principio en cadena. La frecuencia imagen es pregunta clásica de examen: sabérsela es distinguir un receptor de una caja mágica.

**Los parientes:** el receptor de **conversión directa** mezcla la señal directamente a audio (FI = 0): sencillez deliciosa, popular en equipos QRP artesanales. Y la **SDR** (*Software Defined Radio*, radio definida por software) digitaliza la señal cuanto antes y hace mezclas, filtros y demodulación con matemáticas en un procesador: filtros imposibles para el hardware, cascada visual incluida (la que Marina miraba de madrugada), y el diseño dominante en los equipos nuevos. Los bloques son los mismos; ahora algunos son código.

## El transmisor: el viaje inverso

El transmisor es conceptualmente más simple: generar una portadora impecable, modularla y darle músculo.

1. **Oscilador (VFO/sintetizador):** nace la portadora, con estabilidad de cristal (PLL/DDS). Toda la limpieza posterior depende de esta cuna.
2. **Modulador:** se le sube la información. En FM, la voz empuja directamente la frecuencia del oscilador. En SSB, el método clásico es elegante: un **modulador balanceado** mezcla voz y portadora *cancelando la portadora* a su salida (quedan las dos bandas laterales) y un **filtro de cristal** corta la banda lateral sobrante. Queda la «sombra»: SSB pura.
3. **Etapas excitadoras:** amplificaciones intermedias hasta el nivel que necesita la etapa final.
4. **Amplificador de potencia (PA):** el músculo final (los MOSFET grandes, o válvulas en amplificadores externos). Aquí mandan las clases de la sección 5: **AB para SSB** (la forma de la señal ES la información: hay que respetarla), **C solo para FM/CW** (la información va en la frecuencia o en el on/off: deformar no la daña y el rendimiento se agradece).
5. **Filtro paso bajo → antena:** la última aduana mata los armónicos del PA antes de que salgan al mundo. Obligatoria por ley y por vergüenza torera.

**La potencia y sus apellidos.** En CW o FM la potencia es constante y se mide sin drama. Pero la SSB no tiene potencia fija: sube y baja con la voz (¡sin voz no hay emisión!). Por eso se usa la **PEP** (*Peak Envelope Power*, potencia de cresta de la envolvente): la potencia en los picos de modulación. Es la medida que usa la normativa española para los límites legales (el anexo de la Orden IET/1311/2013 fija los máximos «p.c.e.» —potencia de cresta, PEP— por bandas: en HF, hasta 1 kW). Cuando leas «100 W PEP», ya sabes: crestas de 100, promedio muy inferior.

## Los pecados del transmisor

El examen (y la convivencia en las bandas) exige conocer las formas en que un transmisor ensucia:

- **Armónicos:** múltiplos de tu frecuencia (viejos conocidos). Nacen en los amplificadores, sobre todo si están saturados; los mata el filtro paso bajo. Transmitir en 7 MHz y aparecer en 21 es delito técnico flagrante.
- **Espurias:** cualquier emisión fuera de tu canal que no sea armónico: productos de mezcla que se escapan, oscilaciones parásitas. Delatan diseño pobre o avería.
- **Sobremodulación y splatter:** el pecado del ansia. Si le das más micrófono del que el modulador admite (o más excitación de la que el PA amplifica limpio), las crestas se recortan; el recorte —Fourier, siempre Fourier— genera frecuencias nuevas que **ensanchan tu señal** sobre los vecinos: el *splatter*, la mancha. En AM, sobremodular más del 100 % rompe la envolvente; en SSB, saturar el PA embarra tres kilohercios a cada lado. La norma del buen operador: micrófono con moderación y vigilar el **ALC** (control automático de nivel, el circuito del equipo que frena el exceso; su indicador es el chivato de tu limpieza).
- **Deriva de frecuencia:** irse resbalando de la frecuencia con el calentamiento. Los sintetizadores modernos casi lo extinguieron; los equipos antiguos mal cuidados aún se deslizan como caracoles.

Regla de oro heredada de un siglo de convivencia: **tu transmisor no es solo tuyo; sus defectos son de todos.** Un receptor mediocre castiga a su dueño; un transmisor sucio castiga al vecindario entero. Por eso el examen insiste tanto en esta parte.

## Cifras que juzgan un equipo (miniglosario del comprador futuro)

- **Sensibilidad** (µV o dBm): qué susurro es utilizable. En HF sobra sensibilidad en casi cualquier equipo: manda el ruido de la banda.
- **Selectividad** (ancho del filtro a −6 dB): 2,4 kHz para SSB, 500 Hz o menos para CW.
- **Rango dinámico:** la joya oculta: capacidad de oír al débil *con un fortísimo al lado* sin emborracharse (la borrachera técnica se llama **intermodulación**: señales fuertes mezclándose dentro de tu propio receptor y engendrando fantasmas). Distingue equipos buenos de anuncios buenos.
- **Estabilidad** (partes por millón, ppm): cuánto deriva. Con TCXO (cristal compensado en temperatura), el asunto está resuelto para uso normal.
- **Potencia** (W, PEP en SSB): la cifra más cacareada y la menos decisiva: los primeros 100 W los da cualquier equipo; los siguientes 6 dB los da la antena (sección 8) mucho más barato.

## Para llevar

- Receptor: **sensibilidad** (oír lo débil: la limita el ruido), **selectividad** (separar vecinos: la dan los filtros de FI), **estabilidad** (no derivar: cuarzo y PLL).
- **Superheterodino:** mezclador + oscilador local trasladan cualquier emisora a una **FI fija**, donde filtros de cristal fijos hacen el trabajo fino. Peaje: la **frecuencia imagen** (a 2×FI de la deseada), combatida con filtros de entrada y FI altas/doble conversión.
- Cadena RX: filtro/ampli RF → mezclador (OL) → FI → demodulador → audio.
- Cadena TX: oscilador → modulador (balanceado + filtro para SSB) → excitador → **PA** (AB para SSB, C solo FM/CW) → **filtro paso bajo** → antena.
- **PEP**: potencia de cresta; la unidad de los límites legales españoles en SSB.
- Pecados: armónicos, espurias, sobremodulación/splatter, deriva. El ALC es tu chivato; el filtro paso bajo, tu civismo.

## Para el examen

- Bloques del superheterodino en orden, y qué hace cada uno: pregunta segura, a veces como diagrama.
- **Frecuencia imagen:** definición y cálculo simple (imagen = señal ± 2×FI). La pregunta estrella de receptores.
- Para qué sirve la FI (filtrado fino con filtros fijos de gran selectividad).
- Definiciones de sensibilidad y selectividad (no confundirlas: llegan a preguntarlas del derecho y del revés).
- Bloques del transmisor SSB (modulador balanceado + filtro) y qué clase de amplificador exige la SSB (AB; nunca C).
- Qué es la PEP y qué es la sobremodulación/splatter y sus consecuencias (ensanchamiento, interferencia a canales vecinos).

## Para profundizar

- Ejercicio de un minuto que fija el superheterodino para siempre: elige FI = 9 MHz y calcula OL e imagen para tres emisoras cualesquiera. Cuando veas que la imagen siempre cae a 18 MHz de la señal (2×FI), el concepto es tuyo.
- En un websdr (que es una SDR literal), abre el máximo de ancho visual: estás viendo la «FI» digital entera de un receptor de conversión directa gigante. Filtra estrecho y ancho sobre una señal de CW y observa el compromiso selectividad/comodidad en vivo.
- Wikipedia (CC BY-SA): «Receptor superheterodino» (con los diagramas de bloques clásicos) y «Software-defined radio» para el presente y futuro del asunto.
