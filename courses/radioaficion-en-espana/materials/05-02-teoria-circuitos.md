Los componentes eran las letras; esta sección enseña las palabras. Con media docena de combinaciones —serie, paralelo, divisor, resonante, filtro, fuente, amplificador, oscilador— podrás leer el diagrama de cualquier equipo de radio como un texto de izquierda a derecha. Y varias de esas combinaciones traen cuentas que caen en el examen: las haremos todas, paso a paso.

## Resistencias en serie y en paralelo

**En serie** (una tras otra, la misma corriente atraviesa ambas): las resistencias simplemente se suman.

**R total = R1 + R2 + ...**

Dos de 100 Ω en serie: 200 Ω. Lógico: el pasillo con obstáculos se ha hecho el doble de largo.

**En paralelo** (una junto a otra, la corriente se reparte entre ambas): la resistencia total es *menor que la menor* de ellas, porque hay más caminos disponibles. La fórmula general es la de «la suma de los inversos»:

**1/R total = 1/R1 + 1/R2 + ...**

Pero para el examen y para la vida bastan dos atajos que resuelven el 90 % de los casos:

- **Dos resistencias iguales en paralelo: la mitad.** Dos de 100 Ω → 50 Ω. (Cuatro iguales: un cuarto. N iguales: R/N.)
- **Dos distintas: producto entre suma.** R = (R1 × R2) / (R1 + R2). Ejemplo: 100 Ω y 25 Ω → 2500/125 = **20 Ω**. Comprobación instantánea: el resultado (20) es menor que la menor (25). Si te sale mayor, has sumado en vez de «paralelizar».

**Condensadores: al revés.** Es el vals de las fórmulas cruzadas, y al examen le encanta: los condensadores **en paralelo se suman** (placas juntas = más superficie = más capacidad) y **en serie se combinan con la fórmula de los inversos** (dos iguales en serie: la mitad). Las bobinas van como las resistencias: suman en serie, inversos en paralelo.

| | En serie | En paralelo |
|---|---|---|
| Resistencias | Se suman | Inversos (↓) |
| Bobinas | Se suman | Inversos (↓) |
| **Condensadores** | **Inversos (↓)** | **Se suman** |

## El divisor de tensión: la fórmula de la proporción

Pon dos resistencias en serie sobre una tensión y la tensión se **reparte proporcionalmente**: cada resistencia se lleva su parte proporcional del total. La tensión en R2 (medida entre el punto medio y el extremo de R2) vale:

**U2 = U total × R2 / (R1 + R2)**

*Ejemplo resuelto:* 12 V sobre R1 = 4 kΩ y R2 = 2 kΩ en serie. U2 = 12 × 2/(4+2) = 12 × 1/3 = **4 V**. (Y U1 = 8 V; la suma siempre reconstruye el total.)

Parece poca cosa y es omnipresente: el mando de volumen es un divisor ajustable (el potenciómetro), los circuitos de polarización de los transistores son divisores, y los medidores dividen las tensiones grandes para poder digerirlas. Primera palabra leída.

## El circuito resonante: el columpio de Dani

Ahora, la palabra más importante de la radio. Conecta una **bobina** y un **condensador** y deja que la física haga el resto: el condensador se descarga a través de la bobina, que convierte esa energía en campo magnético; al agotarse la corriente, el campo magnético se derrumba y recarga el condensador al revés; y vuelta a empezar. La energía va y viene entre campo eléctrico y campo magnético, oscilando: un columpio electromagnético. Como todo columpio, tiene su ritmo propio, su **frecuencia de resonancia**, que depende solo de los tamaños de ambos:

**f = 1 / (2π √(L·C))**

No necesitas calcularla a mano en el examen español más allá de casos sencillos; necesitas dominar sus *consecuencias*, que sí caen:

- **A más L o más C, menor frecuencia** (columpio más grande se mece más despacio). Para subir de frecuencia, reduce bobina o condensador. Por eso el condensador variable de las radios antiguas sintoniza: cambia C, cambia f.
- En la resonancia, el circuito LC **paralelo** presenta **impedancia máxima** (se comporta como si casi no estuviera para esa frecuencia... vista desde fuera deja caer sobre ella toda la tensión: perfecto para *seleccionar* una frecuencia), y el LC **serie**, **impedancia mínima** (traga esa frecuencia como un sumidero: perfecto para *eliminarla*). Este dúo máximo/mínimo es pregunta clásica.
- **Impedancia (Z)**, dicho sea de paso, es el nombre general de la oposición a la corriente alterna, en ohmios: combina la resistencia pura y las reactancias de bobinas y condensadores. En resonancia, las dos reactancias son iguales y opuestas y se cancelan: por eso la resonancia es especial.
- El **factor Q** (de *quality*) mide lo «fino» que es el columpio: un Q alto significa poca pérdida y una resonancia estrecha y selectiva (responde solo a su frecuencia exacta); un Q bajo, una resonancia ancha y perezosa. Cuando en la sección 8 midas antenas, y en la 7 hablemos de selectividad, será este Q quien mande.

Sintonizar una radio es, literalmente, ajustar un columpio LC (o varios) a la frecuencia de la emisora deseada. El «punto bueno» que buscaba el bigote de gato en la galena, el dial gordo del receptor gris, el mando de sintonía de cualquier equipo: todos mueven una L o una C.

## Filtros: aduanas de frecuencias

Un **filtro** es un circuito que trata distinto a las frecuencias distintas: deja pasar unas y atenúa otras. Se construyen justamente con los comportamientos opuestos que aprendiste en la sección 4 (el condensador facilita las altas frecuencias, la bobina las frena) y con resonancias LC. Cuatro tipos, y los cuatro caen en el examen:

- **Paso bajo:** deja pasar las frecuencias por *debajo* de su frecuencia de corte y atenúa las superiores. El uso estrella en radioafición: a la salida del transmisor, para dejar pasar tu señal y cortar sus **armónicos** (que están siempre por encima, en los múltiplos). Si en la sección 10 hay un televisor con rayas, ya intuyes qué faltaba.
- **Paso alto:** al revés: pasa lo de *arriba*, corta lo de abajo.
- **Paso banda:** solo deja pasar una franja intermedia. Es la aduana de la selectividad de los receptores: la rendija «finísima» de la que hablaba Dani. Un LC resonante con buen Q es un paso banda natural.
- **Rechazo de banda (o «notch», muesca):** el negativo del anterior: lo pasa todo *salvo* una franja. Para asesinar una interferencia concreta sin tocar lo demás.

Cómo reconocerlos en un esquema simple: si el camino de la señal atraviesa bobinas y los condensadores desvían a tierra, es paso bajo (las altas frecuencias tropiezan en las bobinas y se escurren por los condensadores a tierra); si es al revés —condensadores en el camino, bobinas a tierra—, paso alto. Los paso banda combinan resonantes serie en el camino o paralelos a tierra.

## La fuente de alimentación: las cuatro aduanas de Dani

La palabra completa más común del idioma. Convierte los 230 V alternos de la red en la continua limpia (típicamente 13,8 V) que quieren los equipos. Cuatro etapas, en este orden, y el orden cae en el examen:

1. **Transformador:** baja los 230 V de CA a la tensión vecina de la deseada (sigue siendo alterna). Además aísla galvánicamente de la red: primera barrera de seguridad.
2. **Rectificador:** diodos que solo dejan pasar los semiciclos de un sentido. Con un solo diodo (media onda) aprovechas la mitad; con el **puente rectificador** de cuatro diodos (onda completa), le das la vuelta a los semiciclos negativos y lo aprovechas todo. A la salida ya no hay CA... pero tampoco una continua digna: hay un pulso que sube y baja al ritmo de la red, la llamada **corriente continua pulsante**.
3. **Filtro:** condensadores electrolíticos grandes que se cargan en las crestas y sueltan carga en los valles, alisando el pulso. El residuo de ondulación que sobrevive se llama **rizado** (*ripple*, a 100 Hz en un puente sobre red de 50 Hz: cae en examen); si es excesivo se oye como zumbido grave en las transmisiones. El hinchado que Dani señaló con el destornillador era esta etapa, muerta de vieja.
4. **Regulador (estabilizador):** circuito (un zéner con ayuda, o un integrado) que clava la salida en su valor exacto aunque la red fluctúe o el consumo varíe. Los equipos de radio agradecen la estabilidad con su vida.

Variante moderna: las **fuentes conmutadas** trocean la energía a decenas o cientos de kHz con transistores (por eso son pequeñas y ligeras: recuerda los 400 Hz de los aviones, elevados a la enésima potencia) y luego rectifican y filtran. Baratas y eficientes... y con fama justificada de generar ruido de RF si son de mala calidad: el azote moderno de las bandas, como verás en la sección 10.

## Amplificadores: los grifos en cadena

Ya conoces el principio (el transistor-grifo). Como *palabra*, el **amplificador** es una etapa con su transistor (o válvula, o integrado), su alimentación y sus componentes de ajuste, que multiplica la amplitud de la señal. Lo que añade esta sección son los matices con nombre:

- **Ganancia:** cuántas veces multiplica (se expresa en dB, claro: un amplificador de 20 dB multiplica la potencia por 100).
- **Fidelidad vs rendimiento, las clases:** un amplificador puede conducir durante todo el ciclo de la señal (**clase A**: máxima fidelidad, pésimo rendimiento, mucho calor), medio ciclo cada transistor en pareja (**clase B**, y el compromiso fino **AB**: el estándar para amplificar SSB, donde la forma de la señal importa), o menos de medio ciclo a golpes (**clase C**: gran rendimiento, deforma la señal —solo válida para modos donde la forma no importa, como FM o CW— y genera armónicos que exigen filtro paso bajo detrás). La pareja «clase C ↔ solo FM/CW, nunca SSB» es pregunta de examen.
- **Saturación:** todo grifo tiene un caudal máximo. Si pides más, la cresta de la onda sale recortada (*clipping*), y ya sabes por Fourier qué nace al deformar una onda: armónicos e interferencias. Amplificar «a tope» es ensuciar; volverá en la sección 7 como *splatter*.

## Osciladores: el latido

Un **oscilador** es un amplificador que se muerde la cola: una parte de su salida vuelve a su entrada (realimentación) en fase, y el circuito se pone a oscilar solo, generando una señal continua a una frecuencia fijada por... exacto, un circuito resonante LC o un **cristal de cuarzo**. El cristal es una lámina de cuarzo que vibra mecánicamente a una frecuencia exactísima (efecto piezoeléctrico) y equivale a un LC con un Q altísimo, miles de veces mejor que cualquier bobina real: por eso los relojes llevan cuarzo y por eso los transmisores decentes también. Todo transmisor nace en un oscilador: es el latido del que sale la portadora.

El refinamiento moderno se llama **PLL** (*Phase-Locked Loop*, bucle enganchado en fase) y su evolución el **sintetizador digital directo (DDS)**: circuitos que generan cualquier frecuencia con la exactitud del cristal patrón. Son la razón de que tu futuro equipo sintonice a golpe de tecla frecuencias arbitrarias con precisión de hercio, cosa que en tiempos del receptor gris era ciencia ficción. Para el examen basta la idea: PLL = frecuencia variable con estabilidad de cristal.

## Leyendo el texto completo

Ahora ya puedes leer el receptor gris de izquierda a derecha, como prometió Dani: *antena → filtro paso banda (selecciona la franja) → amplificador (levanta lo débil) → [aquí ocurre algo llamado mezcla que es el plato fuerte de la sección 7] → filtro fino → más amplificación → altavoz*. Y debajo de todo, alimentándolo, la fuente con sus cuatro aduanas. Ningún esquema volverá a ser una maraña: serán estas palabras, en distinto orden y tamaño.

## Para llevar

- Serie: resistencias y bobinas suman; paralelo: inversos (dos iguales = mitad; producto/suma para dos). **Condensadores al revés.**
- Divisor de tensión: U2 = U × R2/(R1+R2). La proporción es todo.
- **Resonancia LC:** frecuencia propia f = 1/(2π√LC); más L o C = menos frecuencia; LC paralelo = impedancia máxima en resonancia, LC serie = mínima; Q alto = resonancia estrecha y selectiva.
- **Filtros:** paso bajo (mata armónicos del transmisor), paso alto, paso banda (selectividad del receptor), rechazo de banda (mata una interferencia).
- **Fuente:** transformador → rectificador → filtro → regulador; rizado = residuo de alterna por filtrado insuficiente.
- **Amplificador:** ganancia en dB; clase AB para SSB, clase C solo FM/CW; saturar = deformar = armónicos.
- **Oscilador:** amplificador realimentado + resonador (LC o cristal de cuarzo, el más estable); PLL/DDS = variable con precisión de cristal.

## Para el examen

- Cálculos de serie/paralelo con dos o tres resistencias (y el cruce traicionero de los condensadores): presencia casi garantizada.
- El divisor de tensión con números redondos.
- Efecto de aumentar L o C sobre la frecuencia de resonancia (baja), e impedancia del LC paralelo/serie en resonancia (máxima/mínima).
- Identificar el tipo de filtro por su función («para atenuar armónicos a la salida del transmisor se usa un filtro...»: **paso bajo**).
- Orden de las etapas de la fuente y qué hace cada una; qué es el rizado y su frecuencia (100 Hz con puente en red de 50 Hz).
- Cuál es el oscilador más estable (cristal de cuarzo) y qué clase de amplificador no sirve para SSB (la C).

## Para profundizar

- El simulador falstad.com/circuit trae ejemplos animados de todos los circuitos de esta sección (busca «LRC», «rectifier», «filters»): ver el columpio LC intercambiando energía en tiempo real fija el concepto para siempre.
- OpenStax, *Física universitaria* vol. 2, capítulos de circuitos de corriente alterna y oscilaciones electromagnéticas (CC BY 4.0): la matemática completa de la resonancia, si quieres el andamiaje formal.
