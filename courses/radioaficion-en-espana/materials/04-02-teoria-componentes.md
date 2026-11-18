Este material es el **resumen de la sección**: lo esencial de las nueve lecciones anteriores, en formato de chuleta para repasar antes del examen. Aquí no se explica nada desde cero; si algún apartado no te suena, la explicación paso a paso está en la lección que se indica entre paréntesis.

## Resistencias (lección 1)

- Pieza de dos patas, sin polaridad, con un valor fijo en ohmios. Limita la corriente, reparte la tensión o produce calor.
- **Código de colores** (4 franjas): cifra, cifra, número de ceros, tolerancia. Se empieza por el lado contrario a la franja de tolerancia.

| Negro | Marrón | Rojo | Naranja | Amarillo | Verde | Azul | Violeta | Gris | Blanco |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

- Tercera franja dorada: dividir entre 10; plateada: entre 100. Negro en tercera posición: ningún cero.
- **Tolerancia:** marrón ± 1 %, rojo ± 2 %, dorado ± 5 %, plateado ± 10 %, sin franja ± 20 %.
- **Potencia:** depende del tamaño, no del valor. P = I² × R. Regla práctica: que no trabaje a más de la mitad de lo que aguanta.
- **LED con resistencia en serie:** R = (tensión de la fuente − tensión del LED) / corriente del LED.
- **Variables:** potenciómetro (tres patas, la central es el cursor), LDR (baja con la luz), termistor NTC (baja al calentarse) y PTC (sube al calentarse).

## Condensadores (lecciones 2 y 3)

- Dos placas separadas por un aislante (**dieléctrico**). Almacena carga, y con ella energía, en un campo **eléctrico**.
- **Capacidad:** C = Q / U, en **faradios**. Crece con la superficie de las placas, al acercarlas y con un mejor dieléctrico.
- **1 µF = 1.000 nF = 1.000.000 pF.**
- **Constante de tiempo:** R × C, en segundos (ohmios × faradios). En una constante alcanza el 63 % de la tensión; en cinco, se considera cargado. La descarga tarda lo mismo.
- **En continua:** se carga (tarda del orden de R × C) y después bloquea el paso.
- **En alterna:** se carga y descarga continuamente y por el circuito circula corriente, sin que ningún electrón cruce el dieléctrico.
- **Reactancia capacitiva:** **XC = 1 / (6,28 × f × C)**, en ohmios. Baja al subir la frecuencia o la capacidad. La corriente va **adelantada 90°** respecto a la tensión. No gasta energía.
- **Tipos:** cerámico, de plástico, variable (sintonía) y **electrolítico**, que tiene polaridad, revienta si se conecta al revés y envejece. Todos tienen una tensión máxima.
- Usos: acoplo (deja pasar la señal y detiene la continua), desacoplo (deriva a masa las frecuencias altas), filtros y sintonía.

## Bobinas (lecciones 4 y 5)

- **Campo:** zona en la que un objeto ejerce fuerza a distancia. Toda corriente crea un campo magnético (Ørsted); un campo magnético **que cambia** induce tensión (Faraday).
- **Bobina** (o inductor): hilo enrollado en espiras. Se opone a los **cambios** de corriente y almacena energía en un campo **magnético**.
- **Inductancia:** L, en **henrios** (en radio, mH y µH). Crece con el número de espiras (el doble de espiras, cuatro veces más), con el diámetro, al apretarla y con un núcleo de hierro o ferrita.
- **En continua:** deja pasar. **En alterna:** se opone, más cuanto mayor es la frecuencia.
- **Reactancia inductiva:** **XL = 6,28 × f × L**, en ohmios. Sube con la frecuencia y con la inductancia. La corriente va **retrasada 90°** respecto a la tensión. No gasta energía.
- Una bobina puesta en serie para frenar la radiofrecuencia y dejar pasar la continua se llama **choque**.
- **Impedancia (Z):** oposición total de un circuito a la alterna, en ohmios, combinando resistencias y reactancias (no es una simple suma).

| | Corriente continua | Alterna de baja frecuencia | Alterna de alta frecuencia |
|---|---|---|---|
| **Condensador** | La bloquea | Estorba mucho | Pasa con facilidad |
| **Bobina** | La deja pasar | Estorba poco | La bloquea |

## Transformadores (lección 6)

- Dos bobinas, **primario** y **secundario**, sobre un mismo núcleo, sin conexión eléctrica entre ellas.
- **Tensiones:** U secundario = U primario × (N secundario / N primario). Menos espiras en el secundario: reductor; más: elevador.
- **Corrientes**, al revés: I secundario = I primario × (N primario / N secundario). La potencia se conserva, salvo pérdidas.
- **Impedancias:** se transforman con el **cuadrado** de la relación de espiras.
- **Solo funciona con alterna:** un campo que no cambia no induce nada.
- Además aísla (aislamiento galvánico) y adapta impedancias.

## Semiconductores y diodos (lección 7)

- Silicio **dopado**: tipo **N** (con electrones libres de sobra) y tipo **P** (con *huecos*, vacantes que se comportan como cargas positivas móviles). Los dos son eléctricamente neutros.
- **Unión PN:** conduce en **directa** (positivo al lado P) y bloquea en **inversa**, salvo una corriente de fuga minúscula.
- **Diodo:** una unión PN con dos patas. **Ánodo** (P) y **cátodo** (N, marcado con una raya). La corriente pasa de ánodo a cátodo.
- **Tensión umbral:** unos 0,6 a 0,7 V en silicio; 0,2 a 0,3 V en germanio. No limita la corriente por sí mismo.

| Diodo | Cómo trabaja | Para qué sirve |
|---|---|---|
| Rectificador | En directa conduce, en inversa bloquea | Convertir alterna en continua |
| De señal | Igual, con señales débiles | Detectar señales de radio |
| LED | En directa, emite luz | Indicadores |
| Zéner | En inversa, a su tensión zéner | Tensión fija y estable |
| Varicap | En inversa, como condensador | Capacidad ajustable con una tensión: sintonía |

## Transistores (lección 8)

- Una señal pequeña en la pata de control gobierna una corriente grande, cuya energía aporta la fuente de alimentación.

| | Bipolar (BJT) | De efecto de campo (FET) |
|---|---|---|
| Patas | Emisor, **base**, colector | Fuente, **puerta**, drenador |
| Tipos | NPN y PNP | JFET y MOSFET |
| Se controla por | **Corriente** de base | **Tensión** de puerta |

- **Ganancia** del bipolar: corriente de colector = β × corriente de base. Entre base y emisor hacen falta unos 0,7 V.
- **Símbolo:** la flecha está en el emisor; hacia fuera, NPN; hacia dentro, PNP.
- **Dos oficios:** amplificador (en un punto intermedio) e interruptor (entre **corte** y **saturación**).
- **Tres montajes:** emisor común (el más usado; amplifica tensión y corriente), colector común o seguidor de emisor (entrada de impedancia alta, salida baja), base común (entrada baja, salida alta; radiofrecuencia).

## Válvulas, circuitos integrados y símbolos (lección 9)

- **Válvula:** ampolla al vacío con un **cátodo** caliente que emite electrones, una **placa** (ánodo) que los atrae y una **rejilla** que controla su paso. Sin rejilla, diodo; con una, **triodo**; con dos, tetrodo; con tres, pentodo.
- **Circuito integrado:** un circuito completo fabricado en una sola pieza de silicio. Ejemplo sencillo: el amplificador operacional.
- **Símbolos:** resistencia, zigzag (o rectángulo); condensador, dos rayas paralelas (con «+» el electrolítico); bobina, bucles; transformador, dos bobinas con rayas entre ellas; diodo, triángulo contra una barra (barra doblada: zéner; barra doble: varicap; flechitas: LED). Una flecha atravesada indica que es ajustable.

## Cómo se estropea cada familia

No entra en el examen, pero ahorra tiempo en una reparación.

| Componente | Avería típica | Cómo se nota |
|---|---|---|
| Resistencia | Se abre (deja de conducir) | A menudo se ve tostada |
| Condensador electrolítico | Se seca y pierde capacidad, o se hincha | Parte superior abombada; primer sospechoso en aparatos viejos |
| Diodo o transistor | Queda en cortocircuito, por calor o sobretensión | Conduce en los dos sentidos al medirlo con el polímetro |
| Bobina o transformador | Rara vez fallan, salvo sobrecalentamiento | Olor a quemado, hilo abierto |

Orden de sospecha en un aparato antiguo: electrolíticos, semiconductores que se calientan, soldaduras agrietadas y, solo al final, lo demás.

## Para el examen

- **Código de colores:** practica una docena de combinaciones en los dos sentidos.
- **Condensador frente a bobina:** quién bloquea la continua, quién frena la alta frecuencia, qué reactancia sube y cuál baja con la frecuencia, y el desfase de cada uno.
- **Cálculos:** XC y XL (pasando antes a faradios, henrios y hercios), constante de tiempo R × C, conversiones entre µF, nF y pF.
- **Transformador:** relación de espiras para tensiones, la inversa para corrientes y el cuadrado para impedancias. Solo alterna.
- **Diodos:** umbral del silicio y función del zéner, el LED y el varicap.
- **Transistores:** nombres de las patas de cada tipo, quién se controla por corriente y quién por tensión, cálculo con β, sentido de la flecha y los tres montajes.
- **Símbolos:** reconocer cada componente por su dibujo.

## Para profundizar

- OpenStax, *Física universitaria* vol. 2 (CC BY 4.0, en español): capacidad, inductancia e inducción electromagnética, con los experimentos de Faraday.
- Un kit de iniciación a la electrónica (placa de pruebas, resistencias, LED y pila) por menos de 20 €: montar un LED con la resistencia que tú mismo has calculado fija la sección mejor que cualquier relectura.
- El simulador gratuito falstad.com/circuit: dibujas un circuito y ves las corrientes moverse por él. Prueba con un condensador y con una bobina; la sección 5 empieza justo ahí.
