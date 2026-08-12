Esta es la sección más importante del curso. No la más difícil: la más importante. Todo lo que viene después —componentes, circuitos, antenas, propagación— se apoya en las cuatro ideas que vas a aprender aquí. Vamos despacio y sin saltarnos nada.

## El átomo, o de dónde sale todo esto

Toda la materia está hecha de **átomos**. Un átomo tiene un núcleo central con **protones** (carga eléctrica positiva) y **neutrones** (sin carga), y a su alrededor una nube de **electrones** (carga negativa). La **carga eléctrica** es una propiedad fundamental de la materia, como la masa: no se puede explicar con nada más simple, es de las piezas básicas del universo. Solo necesitas saber tres cosas de ella:

1. Hay dos tipos, que llamamos **positiva** y **negativa**.
2. Las cargas del mismo signo se repelen; las de signo contrario se atraen.
3. La carga se mide en **culombios (C)**. Un culombio es una cantidad enorme: la carga de unos 6,24 trillones de electrones.

En un átomo normal hay tantos protones como electrones y el conjunto es eléctricamente neutro. Pero los electrones más externos de algunos materiales están sujetos con muy poca fuerza.

- En los **conductores** (los metales: cobre, plata, aluminio, oro...), los electrones externos andan tan sueltos que ni siquiera pertenecen a un átomo concreto: forman una especie de gas de **electrones libres** que vaga por el interior del metal. Por eso los metales conducen la electricidad.
- En los **aislantes** (vidrio, plástico, cerámica, goma, aire seco, madera seca...), todos los electrones están firmemente sujetos. No hay quien los mueva, y el material no conduce.
- Y hay un tercer grupo, los **semiconductores** (silicio, germanio), que conducen «a medias» y de forma controlable. Son la base de los diodos y transistores, y les dedicaremos buena parte de la sección 4.

Guárdate esta imagen: un cable de cobre es un tubo lleno de electrones libres desordenados, agitándose al azar sin ir a ninguna parte. Falta algo que los ponga en marcha a todos en la misma dirección.

## Corriente: la fila en marcha

Cuando algo empuja a esos electrones libres a avanzar todos en el mismo sentido, aparece una **corriente eléctrica**: un flujo ordenado de cargas.

- **Símbolo:** I (de *intensidad* de corriente).
- **Unidad:** el **amperio (A)**. Un amperio es el paso de un culombio de carga por segundo a través de la sección del conductor: `I = Q / t` (intensidad = carga entre tiempo).

Para las magnitudes pequeñas y grandes usamos los prefijos del sistema internacional, que en radio se usan sin parar y **caen en el examen**:

| Prefijo | Símbolo | Factor | Ejemplo |
|---|---|---|---|
| pico | p | billonésima (10⁻¹²) | 47 pF (condensador) |
| nano | n | milmillonésima (10⁻⁹) | 10 nF |
| micro | µ | millonésima (10⁻⁶) | 100 µA, 22 µF |
| mili | m | milésima (10⁻³) | 500 mA, 12 mV |
| kilo | k | mil (10³) | 3,5 kΩ, 144 kHz... no: 144 MHz 😉 |
| mega | M | millón (10⁶) | 7 MHz, 1 MΩ |
| giga | G | mil millones (10⁹) | 1,3 GHz |

Conviene automatizar las conversiones: 500 mA = 0,5 A; 3,5 kΩ = 3.500 Ω; 7 MHz = 7.000.000 Hz.

**Un matiz histórico que explica muchos libros confusos:** por convenio, el sentido de la corriente se dibuja **del polo positivo al negativo** por fuera del generador. Los electrones, que tienen carga negativa, viajan en realidad al revés. El convenio se fijó antes de descubrir el electrón y nos lo quedamos. Para cálculos y examen, usa siempre el sentido convencional (+ → −); la física subterránea no cambia ningún resultado.

Dos tipos de corriente que debes distinguir desde ya:

- **Corriente continua (CC):** fluye siempre en el mismo sentido. La producen pilas, baterías, paneles solares y fuentes de alimentación. Casi toda la electrónica de tu emisora funciona por dentro con CC (típicamente 12-13,8 V).
- **Corriente alterna (CA):** cambia de sentido periódicamente. Es la de tu enchufe (230 V, 50 veces por segundo en Europa) y —atención, idea clave del curso— **una señal de radio no es más que corriente alterna de frecuencia altísima**. La sección 3 entera va de esto.

## Tensión: el empujón

Los electrones libres no se mueven solos. Hace falta algo que los empuje: una diferencia de «presión eléctrica» entre dos puntos. Esa diferencia se llama **tensión**, **voltaje** o **diferencia de potencial**.

- **Símbolo:** U (a veces V o E en libros antiguos).
- **Unidad:** el **voltio (V)**.

La analogía clásica es la hidráulica, y es honesta si conoces sus límites: imagina dos depósitos de agua conectados por una tubería. Si están al mismo nivel, no fluye nada. Si uno está más alto, la *diferencia de altura* empuja el agua por la tubería. La tensión es esa diferencia de altura; la corriente, los litros por segundo que pasan por la tubería; y la resistencia, lo estrecha que sea la tubería. (Límite de la analogía: si cortas una tubería, el agua se derrama; si cortas un cable, la corriente simplemente se detiene. No fuerces la analogía más allá de presión/caudal/estrechez.)

Una pila o batería es una «bomba de electrones»: mantiene una diferencia de potencial constante entre sus dos bornes mediante reacciones químicas. Valores que conviene tener en la cabeza:

- Pila alcalina: 1,5 V. Batería de móvil (litio): ~3,7 V. Batería de coche (plomo-ácido): 12 V (12,6-12,8 V llena; en carga, unos 13,8 V — por eso las fuentes de radioaficionado dan 13,8 V).
- Enchufe doméstico europeo: 230 V de alterna.
- La tensión entre dos puntos se mide con el **voltímetro**, conectado **en paralelo** (entre los dos puntos, sin cortar el circuito). La corriente se mide con el **amperímetro**, conectado **en serie** (cortando el circuito para que la corriente pase por el aparato). El polímetro de Vicente hace de ambos.

## Resistencia: los codazos del pasillo

Cuando la corriente atraviesa un material, los electrones van chocando con los átomos del propio material y pierden energía en cada choque (que se convierte en calor). Esa oposición al paso de la corriente es la **resistencia**.

- **Símbolo:** R.
- **Unidad:** el **ohmio (Ω)**.

La resistencia de un conductor concreto depende de cuatro cosas, y esto es pregunta clásica de examen:

1. **Del material** (su *resistividad*): el cobre conduce mejor que el hierro; la plata, mejor que el cobre.
2. **De la longitud:** a doble longitud, doble resistencia. (Un cable largo «roza» más.)
3. **De la sección:** a doble grosor (sección), *mitad* de resistencia. (Un pasillo ancho permite pasar a más gente.)
4. **De la temperatura:** en los metales, a más temperatura, más resistencia (los átomos vibran más y estorban más).

Los componentes fabricados a propósito para tener una resistencia concreta se llaman **resistencias** o *resistores*, y son el componente más abundante de cualquier aparato. Los veremos en la sección 4.

También se usa el concepto inverso: la **conductancia** (símbolo G, unidad el **siemens, S**) es lo contrario de la resistencia: `G = 1 / R`. Un material muy conductor tiene mucha conductancia y poca resistencia. Aparece poco en la práctica diaria, pero el examen la conoce.

## La ley de Ohm: la frase más rentable del curso

En 1827, el profesor alemán **Georg Simon Ohm** publicó la relación entre las tres magnitudes. En notación moderna:

**U = I × R**

La tensión (voltios) es igual a la corriente (amperios) multiplicada por la resistencia (ohmios). En palabras: *para empujar una corriente I a través de una resistencia R hace falta una tensión U*. De la misma fórmula salen las otras dos formas, según lo que busques:

- **I = U / R** — ¿cuánta corriente circulará? (La tensión disponible entre lo que estorba.)
- **R = U / I** — ¿qué resistencia hay ahí? (Cuánta tensión ha hecho falta por cada amperio.)

Truco del triángulo: escribe U arriba, I y R abajo. Tapa la magnitud que buscas y lo que queda a la vista es la fórmula.

**Ejemplos resueltos, del estilo exacto del examen:**

1. *Una resistencia de 100 Ω se conecta a una batería de 12 V. ¿Qué corriente circula?*
   I = U / R = 12 / 100 = **0,12 A = 120 mA**.

2. *Por una resistencia circulan 2 A cuando se le aplican 24 V. ¿Cuánto vale la resistencia?*
   R = U / I = 24 / 2 = **12 Ω**.

3. *¿Qué tensión hay entre los extremos de una resistencia de 50 Ω por la que circulan 200 mA?*
   Primero, unidades: 200 mA = 0,2 A. U = I × R = 0,2 × 50 = **10 V**.
   (El error clásico del examen es no convertir los miliamperios. Cuidado ahí.)

## Potencia y energía: la cuenta de la batería

Falta la magnitud que lo paga todo. La **potencia** es el ritmo al que se consume (o entrega) energía.

- **Símbolo:** P. **Unidad:** el **vatio (W)**.
- Fórmula fundamental: **P = U × I** (potencia = tensión × corriente).

Combinándola con la ley de Ohm salen dos formas derivadas muy usadas:

- **P = I² × R** (útil cuando conoces la corriente que atraviesa una resistencia)
- **P = U² / R** (útil cuando conoces la tensión aplicada)

**Ejemplos:**

1. *Un transceptor consume 10 A a 12 V mientras transmite. ¿Qué potencia consume?*
   P = U × I = 12 × 10 = **120 W**. (Ojo: consume 120 W de la batería; su potencia de *emisión* será menor, porque parte se pierde en calor. El rendimiento aparecerá en la sección 7.)

2. *¿Qué potencia disipa una resistencia de 50 Ω por la que circulan 2 A?*
   P = I² × R = 4 × 50 = **200 W**. (Esa resistencia debe ser grande y aguantar calor: una resistencia pequeña de las de 0,25 W se convertiría en humo. La «potencia máxima» de un componente es un dato tan real como su valor.)

La **energía** es potencia acumulada en el tiempo: `E = P × t`. Su unidad oficial es el **julio (J)** (un vatio durante un segundo), pero en la práctica doméstica usamos el kilovatio-hora (kWh) y, en el mundo de las baterías, una unidad de *carga*: el **amperio-hora (Ah)**.

Una batería de **60 Ah** puede suministrar, idealmente, 60 amperios durante 1 hora, o 6 A durante 10 horas, o 1 A durante 60 horas. Ahora ya puedes auditar la cuenta que Vicente le hizo a Marina:

- Transmitiendo: 10 A → 60 Ah / 10 A = **6 horas** de transmisión continua.
- Escuchando: ~0,8 A → 60 Ah / 0,8 A = **75 horas** de escucha.
- Una noche real de emergencia (95 % escucha, 5 % transmisión): consumo medio ≈ 0,95 × 0,8 + 0,05 × 10 = 0,76 + 0,5 = 1,26 A → unas **47 horas** de autonomía. Por eso al amanecer «aún le quedaba cuerda», y por eso su regla era escuchar mucho y hablar corto.

(En la realidad las baterías no se deben descargar del todo y su capacidad baja con los años y el frío; la aritmética te da el orden de magnitud, y el orden de magnitud es lo que salva noches.)

## Cortocircuito y circuito abierto: los dos extremos

Dos situaciones límite que conviene nombrar ya, porque reaparecerán todo el curso:

- **Circuito abierto:** el camino está interrumpido (interruptor abierto, cable roto). Resistencia infinita, corriente cero. No pasa nada... literalmente.
- **Cortocircuito:** los dos polos de la fuente se unen por un camino de resistencia casi nula. La ley de Ohm es implacable: I = U / R con R diminuta da una corriente enorme. Los cables se calientan al rojo (recuerda P = I²R), la batería puede reventar. Por eso existen los **fusibles**: un hilo calibrado que se funde y abre el circuito cuando la corriente pasa de un límite. Un fusible no protege tu equipo del rayo ni de tus errores de diseño: protege el cableado del incendio. Ponlos siempre.

## Para llevar

- La materia contiene **electrones libres** (en los conductores); ordenarlos en marcha es la **corriente** (amperios), el empujón que los ordena es la **tensión** (voltios), la oposición del material es la **resistencia** (ohmios).
- **Ley de Ohm: U = I × R**, con sus tres formas. Convierte SIEMPRE mA→A y kΩ→Ω antes de calcular.
- **Potencia: P = U × I = I²R = U²/R**, en vatios. **Energía = potencia × tiempo**; capacidad de batería en **amperios-hora**.
- Resistencia de un cable: sube con la longitud y la temperatura, baja con la sección; depende del material.
- Voltímetro **en paralelo**, amperímetro **en serie**.
- Cortocircuito = corriente descontrolada = calor: **fusibles siempre**.

## Para el examen

- La ley de Ohm cae **seguro**, casi siempre con una conversión de unidades escondida (mA, kΩ). Es el punto más regalado del examen si te sabes el triángulo... y el más perdido si no conviertes unidades.
- Prefijos (pico a giga): pregunta directa habitual («¿cuántos hercios son 3,5 MHz?»).
- Distinguir CC/CA, conductor/aislante/semiconductor, y de qué depende la resistencia de un conductor.
- Las tres fórmulas de potencia. Practica P = I²R, que es la que menos intuitiva resulta.
- Cómo se conectan voltímetro y amperímetro.

## Para profundizar

- OpenStax, *Física universitaria* vol. 2 (openstax.org, licencia CC BY 4.0, disponible en español): capítulos de carga eléctrica, corriente y resistencia. El desarrollo formal y gratuito de todo lo anterior.
- Cualquier polímetro básico (desde 10 €) y una pila: mide tensiones de pilas nuevas y gastadas, la resistencia de tu cuerpo entre mano y mano, la continuidad de un cable. Diez minutos de práctica valen un capítulo.
