Este material es el **resumen de la sección**: lo que has aprendido en las ocho lecciones anteriores, condensado en formato de chuleta para repasar antes del examen. Aquí no se explica nada desde cero; si algún apartado no te suena, vuelve a la lección correspondiente, que es donde está la explicación paso a paso.

## Serie y paralelo (lección 1)

| | En serie (un solo camino) | En paralelo (varios caminos) |
|---|---|---|
| Corriente | La misma en todos | Se reparte; la total es la suma |
| Tensión | Se reparte; la mayor resistencia se lleva más | La misma en todos |
| Resistencia total | R1 + R2 + … | Menor que la menor |

- Paralelo, fórmula general: **1 / R total = 1 / R1 + 1 / R2 + …**
- Atajos: resistencias iguales, **R / número**; dos distintas, **(R1 × R2) / (R1 + R2)**. Ejemplo: 4 Ω y 8 Ω dan 32 / 12 ≈ 2,67 Ω.
- **Kirchhoff:** en un nudo, la corriente que entra es la que sale; al dar la vuelta a un circuito, las caídas de tensión suman la tensión de la fuente.
- Circuitos mixtos: se resuelven por partes, sustituyendo cada grupo por su equivalente.

## Divisor de tensión, bobinas y condensadores (lección 2)

- **Divisor:** dos resistencias en serie; la salida se toma en R2. **U2 = U × R2 / (R1 + R2)**: la parte del total que representa R2. Ejemplo: 9 V con 1 kΩ y 2 kΩ dan 6 V.
- Lo que se conecta a la salida queda en paralelo con R2 y **baja la tensión**: el mismo divisor con una carga de 2 kΩ da 4,5 V. Un divisor da referencias, no alimenta aparatos. El potenciómetro es un divisor ajustable.

| | En serie | En paralelo |
|---|---|---|
| Resistencias y bobinas | Se suman | Inversos: menor que la menor |
| **Condensadores** | **Inversos: menor que el menor** | **Se suman** |

## Resonancia (lecciones 3 y 4)

- **Impedancia (Z):** oposición total a la corriente alterna, en ohmios. I = U / Z. La resistencia gasta energía; las reactancias (XL de la bobina, XC del condensador) la guardan y la devuelven.
- **Circuito resonante (LC):** bobina y condensador se pasan la energía a un ritmo propio, la **frecuencia de resonancia**:

  **f₀ = 1 / (2π × √(L × C))**, o con el atajo, **f₀ (MHz) = 159 / √(L × C)** con L en µH y C en pF. Ejemplo: 10 µH y 100 pF dan 5,03 MHz.
- **Más L o más C, menor frecuencia.** Para bajar a la mitad hay que cuadruplicar C (o L).
- En resonancia, **XL = XC**, y como son contrarias, se anulan.

| | LC serie | LC paralelo |
|---|---|---|
| Impedancia en resonancia | **Mínima** | **Máxima** |
| Imagen | Puerta abierta para esa frecuencia | Tapón para esa frecuencia |
| Entre el camino y masa | La elimina | Impide que se escape: sintonía |
| En el camino de la señal | La deja pasar | Le corta el paso: trampa |

- Resistencia y reactancia no se suman: **Z = √(R² + X²)**. Con R = 30 Ω y X = 40 Ω, Z = 50 Ω.
- **Factor Q = XL / R:** lo selectivo que es el circuito. **Ancho de banda B = f₀ / Q** (medido entre los puntos de −3 dB). Con 7 MHz y Q = 100, B = 70 kHz. Q alto: estrecho y selectivo.

## Filtros (lección 5)

La **frecuencia de corte (fc)** es el punto donde la potencia ha caído a la mitad (−3 dB). El nombre del filtro dice lo que **deja pasar**.

| Filtro | Deja pasar | Uso típico |
|---|---|---|
| **Paso bajo** | Lo que está por debajo de fc | Salida del transmisor: quita los armónicos |
| **Paso alto** | Lo que está por encima de fc | Entrada de un televisor: rechaza la onda corta |
| **Paso banda** | Una franja | Receptor: selecciona la señal |
| **Rechazo de banda** (*notch*) | Todo menos una franja | Elimina una interferencia concreta |

- Paso bajo: bobinas en el camino, condensadores a masa. Paso alto: al revés.
- Con tres piezas: en **π** (dos elementos a masa y uno en el camino entre ellos) o en **T** (dos en el camino y uno a masa en el centro).
- Con resistencia y condensador: fc = 1 / (2π × R × C).
- **Filtro de cristal:** paso banda muy estrecho hecho con láminas de cuarzo.

## Fuente de alimentación (lección 6)

**Transformador → rectificador → filtro → regulador.**

| Etapa | Componente | Qué hace | Qué sale |
|---|---|---|---|
| Transformador | Dos bobinas acopladas | Baja la tensión y aísla de la red | Alterna de baja tensión |
| Rectificador | Diodos | Un solo sentido | Continua pulsante |
| Filtro | Condensador electrolítico grande | Rellena los valles | Continua con rizado |
| Regulador | Zéner + transistor, o un integrado | Fija la tensión, restando lo que sobra | Continua estable |

- **Media onda** (un diodo): 50 pulsos por segundo. **Onda completa** (puente de cuatro diodos, o dos diodos con transformador de toma central): 100 pulsos por segundo; da la vuelta a los semiciclos negativos.
- **Rizado:** ondulación que queda tras el filtro; **100 Hz** con onda completa. Crece con el consumo y con un condensador envejecido; se oye como zumbido.
- El condensador se carga al valor de pico: eficaz × 1,414, menos 1,4 V de los dos diodos.
- Estabilizador más simple: una resistencia en serie y un zéner en paralelo con la salida.
- **Fuente conmutada:** trocea a alta frecuencia; pequeña, ligera y con un rendimiento del 85-90 %, pero puede generar ruido de radiofrecuencia. La lineal: grande, 50-60 %, sin ruido.

## Amplificadores (lección 7)

- Un amplificador entrega una copia mayor de la señal con energía de la **fuente**. **Ganancia** en dB: se suman las de la cadena y se restan las pérdidas (13 dB = × 20 en potencia). Para tensiones, × 2 son 6 dB y × 10 son 20 dB.
- **Rendimiento** = potencia de señal que sale / potencia que consume.

| Clase | El transistor conduce | Rendimiento | Sirve para |
|---|---|---|---|
| **A** | Todo el ciclo | 25-30 % | Señales pequeñas; la más fiel |
| **B** | Medio ciclo (dos en contrafase) | 60-70 % | Potencia; distorsión de cruce |
| **AB** | Algo más de medio ciclo | 50-60 % | **Amplificadores lineales: SSB** |
| **C** | Menos de medio ciclo | 70-80 % | **Solo CW y FM**; necesita circuito resonante y paso bajo |

- **Saturación:** si se le pide demasiado, recorta las crestas. Aparecen **armónicos** (los quita el paso bajo) e **intermodulación** pegada a la propia señal (no la quita ningún filtro: es el *splatter*). Remedio: no llevar el equipo al máximo.

## Osciladores y el receptor completo (lección 8)

- **Oscilador:** amplificador con **realimentación positiva** (la salida vuelve a la entrada en fase) y ganancia suficiente para compensar las pérdidas. Un circuito resonante en el lazo fija la frecuencia. La realimentación negativa (en oposición de fase) no hace oscilar: estabiliza.
- **Oscilador LC (VFO):** variable, pero deriva con la temperatura.
- **Oscilador de cristal de cuarzo:** piezoelectricidad; Q de decenas de miles; **el más estable**, de frecuencia fija.
- **PLL (sintetizador):** frecuencia variable con estabilidad de cristal. Piezas: referencia de cristal, comparador de fase, filtro paso bajo, **VCO** (oscilador controlado por tensión) y divisor. Frecuencia = número del divisor × referencia. Su evolución, la síntesis digital directa (DDS), permite pasos de un hercio.
- **Receptor, de izquierda a derecha:** antena → filtro paso banda → amplificador → mezclador con su oscilador (sección 7) → filtro estrecho → amplificadores → **detector** (extrae el sonido) → amplificador de audio y altavoz. Debajo, la fuente.
- **Transmisor:** oscilador → etapas que añaden la voz → amplificadores (el último, AB o C) → filtro paso bajo → antena.

## Para el examen

- Cálculos de serie y paralelo con dos o tres resistencias, y el cruce de los condensadores: presencia casi garantizada. Comprueba siempre que un paralelo de resistencias da menos que la menor.
- El divisor de tensión con números redondos, y qué le pasa al conectarle una carga.
- Efecto de aumentar L o C sobre la frecuencia de resonancia (baja); impedancia del LC serie (mínima) y paralelo (máxima); B = f₀ / Q.
- Identificar el filtro por su función: para los armónicos de un transmisor, **paso bajo**.
- Orden de las etapas de la fuente y qué hace cada una; frecuencia del rizado (100 Hz con onda completa).
- Clases de amplificador: cuánto conduce cada una y por qué la C no sirve para SSB.
- El oscilador más estable (cristal de cuarzo) y qué es un PLL.

## Para profundizar

- El simulador falstad.com/circuit trae ejemplos animados de todos los circuitos de esta sección (busca «LRC», «rectifier», «filters»): ver un circuito LC intercambiando energía en tiempo real fija la idea mejor que cualquier texto.
- OpenStax, *Física universitaria* vol. 2, capítulos de circuitos de corriente alterna y oscilaciones electromagnéticas (CC BY 4.0): la matemática completa de la resonancia, para quien quiera el desarrollo formal.
