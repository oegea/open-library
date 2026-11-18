Este material es el **resumen de la sección**: todo lo que has aprendido en las ocho lecciones anteriores, condensado en una chuleta para repasar antes del examen. Aquí no se explica nada desde cero; si al leer algún apartado notas que no lo entiendes, vuelve a la lección correspondiente, que es donde está la explicación paso a paso.

## Qué viaja por un cable

- La materia está hecha de **átomos**: núcleo con protones (carga **+**) y, alrededor, electrones (carga **−**). Cargas iguales se repelen; cargas distintas se atraen.
- En los metales hay **electrones libres**. Un cable está siempre lleno de ellos: la pila no los fabrica, los hace circular.
- **Conductores:** dejan pasar la corriente (metales; peor, el agua salada y el cuerpo humano). **Aislantes:** no la dejan pasar (plástico, goma, vidrio, aire seco). **Semiconductores:** caso intermedio y controlable (silicio).
- **Corriente eléctrica:** movimiento ordenado de cargas a lo largo de un conductor.
- Solo hay corriente si el camino es un **circuito cerrado**. Con el circuito **abierto** en un punto, no circula nada en ninguna parte.

## Las magnitudes

| Magnitud | Letra | Unidad | Qué es | En el circuito de agua |
|---|---|---|---|---|
| Carga | Q | culombio (C) | Cantidad de electricidad | Una cantidad de agua |
| **Tensión** | **U** (o V) | **voltio (V)** | El empuje entre dos puntos | La presión de la bomba |
| **Corriente** | **I** | **amperio (A)** | Carga que pasa cada segundo | El caudal |
| **Resistencia** | **R** | **ohmio (Ω)** | Oposición al paso de la corriente | Lo que estorba la tubería |
| Conductancia | G | siemens (S) | Facilidad de paso (lo contrario) | — |
| **Potencia** | **P** | **vatio (W)** | Energía gastada cada segundo | El trabajo de la rueda por segundo |
| Energía | E | julio (J), vatio-hora (Wh) | Cantidad total de trabajo | El trabajo total de la rueda |
| Capacidad de una batería | — | amperio-hora (Ah) | Carga que puede hacer circular | El agua que la bomba puede mover |

Ideas que conviene tener claras:

- La tensión existe siempre **entre dos puntos** y puede haberla sin corriente (una pila sin conectar). Tensión, voltaje y diferencia de potencial son lo mismo.
- **La fuente fija la tensión, el aparato fija la resistencia y la corriente es el resultado.**
- En un circuito de un solo camino, **la corriente es la misma en todos sus puntos**. Lo que se gasta en un aparato es energía, no corriente.
- Sentido convencional de la corriente: **del + al −** (los electrones van al revés).
- **Corriente continua (CC, DC):** siempre en el mismo sentido (pilas, baterías). **Corriente alterna (CA, AC):** cambia de sentido periódicamente (el enchufe, a 230 V).

## Las fórmulas

| Para qué | Fórmula |
|---|---|
| Corriente | I = Q / t |
| **Ley de Ohm** | **I = U / R**, o bien U = I × R, o bien R = U / I |
| **Potencia** | **P = U × I**, o bien P = I² × R, o bien P = U² / R |
| Energía | E = P × t |
| Resistencia de un cable | R = ρ × L / S |
| Conductancia | G = 1 / R |
| Tensión en bornes de una batería | f.e.m. − I × resistencia interna |
| Autonomía de una batería | horas = amperios-hora / amperios |
| Energía de una batería | Wh = Ah × V |
| Rendimiento | potencia útil / potencia consumida |

Equivalencias que conviene recordar:

- 1 amperio es 1 culombio cada segundo.
- 1 vatio es 1 julio cada segundo.
- 1 voltio es 1 julio por cada culombio.
- 1 Wh = 3.600 J, y 1 Ah = 3.600 C.

## Cables, baterías y cortocircuitos

- La resistencia de un cable **aumenta** con la longitud y con la temperatura, **disminuye** con la sección y depende del material (**resistividad**, ρ; lo contrario es la **conductividad**). El doble de diámetro son cuatro veces más sección.
- **Caída de tensión:** cada resistencia que la corriente atraviesa se queda con I × R voltios. Cuando hay varias cosas en fila, la tensión de la fuente se reparte entre ellas. Por eso los cables de alimentación se quieren **cortos y gruesos**.
- Toda batería tiene **resistencia interna**. Sin carga, entre sus bornes está su **fuerza electromotriz (f.e.m.)**; con carga, algo menos.
- **Cortocircuito:** los bornes unidos por un camino sin apenas resistencia. La corriente solo la limita la resistencia interna (**corriente de cortocircuito** = f.e.m. / resistencia interna) y puede ser de cientos de amperios.
- **Fusible:** hilo calibrado que se funde y abre el circuito si la corriente pasa de su valor. Va en serie, cerca de la batería, y se sustituye siempre por otro igual.
- **En serie** (en fila) se suman las tensiones y la capacidad es la de una. **En paralelo** (lado a lado) la tensión es la de una y se suman las capacidades.

## Medir

| Instrumento | Mide | Se conecta | Por dentro |
|---|---|---|---|
| **Voltímetro** | Tensión | **En paralelo**, tocando dos puntos | Apenas deja pasar corriente |
| **Amperímetro** | Corriente | **En serie**, abriendo el circuito | Es casi un cable |

El polímetro hace de los dos. Un amperímetro conectado como un voltímetro provoca un cortocircuito.

## Prefijos

| Prefijo | Símbolo | Significa |
|---|---|---|
| giga | G | × 1.000.000.000 |
| mega | M | × 1.000.000 |
| kilo | k | × 1.000 |
| mili | m | ÷ 1.000 |
| micro | µ | ÷ 1.000.000 |
| nano | n | ÷ 1.000.000.000 |
| pico | p | ÷ 1.000.000.000.000 |

Cada prefijo vale mil veces el siguiente: pasar de uno al de al lado es mover la coma tres lugares. **Antes de usar una fórmula, todo a voltios, amperios y ohmios.** Atajo: mA × kΩ = V.

## Seguridad, en dos líneas

Lo que hace daño es la corriente que atraviesa el cuerpo, y bastan unos 30 mA a través del pecho para que sea mortal. La tensión de un enchufe (230 V) es siempre peligrosa. Los 12 V de una batería no dan calambre, pero un cortocircuito en ella puede provocar un incendio.

## Para el examen

- La ley de Ohm cae **seguro**, casi siempre con una conversión de unidades escondida (mA, kΩ). Es el punto más regalado del examen si conviertes antes de calcular, y el más perdido si no.
- Las tres fórmulas de la potencia, sobre todo P = I² × R: primero el cuadrado, luego la multiplicación.
- Prefijos, de pico a giga: pregunta directa habitual («¿cuántos hercios son 3,5 MHz?»).
- Distinguir conductor, aislante y semiconductor; continua y alterna; y de qué depende la resistencia de un conductor.
- Cómo se conectan voltímetro (paralelo) y amperímetro (serie).
- Autonomía de una batería (Ah / A), su energía (Ah × V) y qué ocurre con tensión y capacidad al asociar baterías en serie o en paralelo.
- Resistencia interna, f.e.m. y tensión en bornes; qué es un cortocircuito y para qué sirve un fusible.

## Para profundizar

- OpenStax, *Física universitaria* vol. 2 (openstax.org, licencia CC BY 4.0, disponible en español): capítulos de carga eléctrica, corriente y resistencia. El desarrollo formal y gratuito de todo lo anterior.
- Un polímetro básico (desde 10 €) y una pila: mide la tensión de pilas nuevas y gastadas, la resistencia de una bombilla apagada, la continuidad de un cable. Diez minutos de práctica valen un capítulo.
