En la entrada de tu casa hay una caja con una fila de interruptores que casi nadie mira hasta que se va la luz. Es el cuadro eléctrico, y dentro están los dispositivos de los que depende que una avería se quede en un susto. Vicente aludió a uno de ellos cuando habló de la tierra del enchufe; aquí los vas a conocer uno por uno.

La lección anterior terminó con una pregunta abierta: cuando una avería manda la corriente por el hilo de tierra, ¿quién la corta? Esta lección la contesta, y añade los otros dos guardianes de una estación: los fusibles de los equipos y la costumbre de comprobar antes de tocar.

Al terminar sabrás qué protege el diferencial y qué protege el magnetotérmico —confundirlos es uno de los errores más frecuentes del examen—, cómo se sustituye un fusible y por qué un aparato desenchufado puede seguir siendo peligroso.

## El interruptor diferencial: protege a las personas

Recuerda una idea de la sección 2: en un circuito, la corriente que sale es la que vuelve. Por el hilo de fase y por el hilo neutro debe pasar exactamente la misma.

El **interruptor diferencial** vigila eso continuamente: compara la corriente que va por la fase con la que vuelve por el neutro. Mientras sean iguales, no hace nada. Si de pronto vuelve menos de la que fue, es que una parte se está escapando por otro sitio: por el hilo de tierra de un aparato averiado, o por el cuerpo de alguien hacia el suelo. En ese momento corta.

> **Interruptor diferencial:** dispositivo que corta el circuito cuando detecta que una parte de la corriente se está **fugando a tierra**. Los de las viviendas saltan cuando la fuga alcanza **30 mA**, y lo hacen en muy poco tiempo: centésimas de segundo con las corrientes de un contacto directo, algo más si la fuga es pequeña.

Los 30 mA no son casualidad: en la tabla de la lección anterior, es el nivel a partir del cual la corriente empieza a ser de verdad peligrosa.

![El interruptor diferencial. En funcionamiento normal, por la fase van 5 amperios y por el neutro vuelven 5 amperios: no hay diferencia y no actúa. Con una fuga, por la fase van 5,05 amperios y por el neutro vuelven 5: los 50 miliamperios que faltan se están escapando a tierra a través de una persona, y el diferencial corta.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s10-diferencial.svg)

—O sea, que con diferencial no puede pasarme nada —dijo Marina—. Como mucho me pasan treinta miliamperios.

—No —dijo Vicente—. Y es importante que no te quedes con esa idea. El diferencial no limita la corriente: la corta. Hasta que corta, por ti pasa lo que diga la ley de Ohm, que pueden ser cien o doscientos miliamperios. Lo que consigue es que eso dure centésimas de segundo en vez de segundos. La descarga la recibes igual. Es la última red, no un permiso.

Tiene, además, un punto ciego. El diferencial detecta la corriente que se escapa **a tierra**. Si alguien toca a la vez la fase y el neutro sin estar en contacto con nada más, toda la corriente que va por un hilo vuelve por el otro, y el diferencial no ve ninguna diferencia.

Lleva un botón de prueba, marcado con una **T**. Al pulsarlo se provoca una pequeña fuga a propósito, y el diferencial debe saltar. Los fabricantes recomiendan pulsarlo periódicamente; una vez al mes es una buena costumbre. Y si el cuadro de tu casa no tiene diferencial —ocurre en viviendas antiguas—, lo primero que necesita tu futura estación no es una antena: es un electricista.

## El interruptor magnetotérmico: protege los cables

El **magnetotérmico** es, en esencia, un fusible que se puede volver a armar. Vigila que por un circuito no pase más corriente de la que sus cables soportan.

> **Interruptor magnetotérmico:** dispositivo que corta el circuito cuando la corriente supera un valor determinado (10 A, 16 A, 25 A…), sea por una **sobrecarga** (demasiados aparatos a la vez) o por un **cortocircuito**.

Su nombre describe sus dos mecanismos: una parte *térmica*, que salta cuando un exceso moderado de corriente la calienta durante un rato, y una parte *magnética*, que salta al instante ante la corriente enorme de un cortocircuito.

Y aquí está la clave: **el magnetotérmico no te protege a ti.** Uno de 16 A deja pasar tranquilamente 15,9 amperios, y a una persona le bastan 0,03. Los 100 mA de un contacto con la red son, para él, una corriente insignificante.

| | Diferencial | Magnetotérmico |
|---|---|---|
| Vigila | Que la corriente que va sea igual a la que vuelve | Que la corriente no supere un máximo |
| Salta con | Una fuga a tierra de 30 mA | Sobrecargas y cortocircuitos: decenas de amperios |
| Protege | A las **personas** | A la **instalación** (cables, enchufes) |

Los dos son necesarios, y ninguno se anula ni se puentea jamás. Una protección que salta sin motivo aparente está avisando de algo: hay que encontrar la causa, o llamar a quien sepa encontrarla, no silenciarla.

## Los fusibles de los equipos

El magnetotérmico protege los cables de la pared. Dentro de cada equipo, y en los cables que salen de una batería, la misma función la hacen los **fusibles**, que conoces de la sección 2: un hilo calibrado que se funde cuando la corriente supera su valor.

Hay dos familias, y se distinguen por una letra grabada en el propio fusible:

- **Rápidos (F)**: se funden casi al instante. Protegen circuitos delicados.
- **Lentos o retardados (T)**: toleran durante un momento el pico de corriente que muchos aparatos piden al encenderse, y solo se funden si el exceso se mantiene.

Las reglas son dos:

> Un fusible se sustituye **siempre por otro del mismo tipo y de los mismos amperios**. Y si el nuevo también se funde, hay una avería: no se prueba con un tercero.

Un fusible mayor, o un trozo de alambre o de papel de aluminio en su lugar, no arregla nada: solo consigue que lo siguiente en quemarse sea el cable, o el equipo.

## Los condensadores no olvidan

Hasta aquí, todo el peligro venía del enchufe. Hay uno que sobrevive al desenchufar.

Recuerda de la sección 4 que un condensador almacena carga, y de la sección 5 que las fuentes de alimentación llevan condensadores grandes para alisar la corriente. Un condensador cargado se queda cargado si nada lo vacía. **Durante horas, o días, después de desenchufar el aparato.**

En la salida de una fuente de 13,8 V eso da, como mucho, un buen chispazo. Pero dentro de los equipos hay tensiones mucho mayores:

- Las **fuentes conmutadas** (sección 5), incluso las pequeñas, tienen en su entrada un condensador cargado a más de 300 V. La razón la sabes desde la sección 3: los 230 V de la red son el valor eficaz, y el valor de pico, que es al que se carga el condensador, es 230 × 1,41 ≈ 325 V.
- Las fuentes de los **equipos de válvulas** y de los amplificadores de válvulas trabajan con cientos o miles de voltios.

Un condensador así, tocado con el aparato desenchufado y la tapa abierta, puede dar una descarga tan peligrosa como la de la red.

Para quien abre un equipo, la norma es fija:

1. **Desenchufar.** No basta con apagar con el interruptor.
2. **Esperar** unos minutos. Los aparatos bien diseñados llevan unas resistencias que vacían los condensadores poco a poco.
3. **Comprobar primero el propio polímetro.** Selector en tensión continua, escala más alta, cable rojo en VΩ, y una medida de prueba sobre una pila. Ya sabes que un cero puede ser un selector mal puesto, y aquí un cero falso es justo lo que no puede ocurrir. Con el cable rojo en el agujero de los amperios, además, el polímetro pondría el condensador en cortocircuito.
4. **Medir** entre los dos terminales de cada condensador grande, tocando solo con las puntas y sin apoyar la otra mano en el aparato. No hay que fiarse de que las resistencias de descarga existan o funcionen.
5. Si marca más de unos pocos voltios, **no se toca**: se cierra, se espera más y se vuelve a medir. Si la tensión no baja, ese aparato es para alguien con experiencia. Un condensador no se descarga nunca haciendo puente con un destornillador.

Este procedimiento vale para equipos modernos de transistores. **Un equipo de válvulas, o cualquier otro con alta tensión, no es para que lo abra un principiante**: sus tensiones superan incluso lo que un polímetro corriente puede medir.

Y un criterio previo a todo lo anterior: si nunca has abierto un equipo que se enchufa a la red, la primera vez no se hace solo. Se hace en el radioclub, con alguien al lado que sepa.

## Reglas de trabajo

Reunidas, son pocas:

- **No se trabaja ni se mide dentro de un aparato enchufado a la red.** Con este curso no vas a hacerlo nunca. Para reparar o modificar, primero se desenchufa. La mayoría de los accidentes ocurren por un «solo es un momento».
- Lo que sí se puede medir con tensión son las **tensiones muy bajas de continua**: los 13,8 V de la fuente en sus bornes de salida, una batería, los cables de alimentación del equipo. (Ojo con el nombre: en los reglamentos, «baja tensión» incluye los 230 V del enchufe.)
- **Después de desenchufar, se comprueba** con el voltímetro que no queda tensión.
- **Manos y suelo secos.** Nada de trabajar descalzo ni con humedad.
- Las tensiones altas de los equipos de válvulas quedan para quien tenga formación específica.
- En la estación, **un interruptor general accesible** que lo corte todo, y que quienes viven en la casa sepan dónde está.

Y si alguien está recibiendo una descarga:

1. **No lo toques.** Mientras siga en contacto con la tensión, tocarlo es recibirla tú.
2. **Corta la corriente** en el cuadro, o desenchufa. Solo si no es posible, sepáralo con algo seco y aislante, como un palo de madera.
3. **Llama al 112.** Si no responde o no respira y sabes hacer la reanimación, empiézala mientras llega la ayuda.
4. Aunque parezca recuperado, **que lo vea un médico**: una descarga puede alterar el corazón horas después.

## Donde la gente se lía

- **«El magnetotérmico me protege de un calambre.»** No. Salta con decenas de amperios. De las personas se ocupa el diferencial, que salta con 30 mA.
- **«Con diferencial no me puede pasar nada.»** No limita la corriente: acorta el tiempo. Y no ve un contacto entre fase y neutro.
- **«Si el diferencial salta mucho, es que está muy sensible: lo cambio por uno menos sensible.»** Está avisando de una fuga. Hay que encontrarla.
- **«Un fusible más gordo aguanta mejor.»** Aguanta él; lo que se quema es lo que protegía.
- **«Está desenchufado, luego es seguro.»** Los condensadores pueden seguir cargados.

## Compruébalo tú

1. ¿Qué compara un interruptor diferencial, y con qué valor de fuga salta el de una vivienda?
2. Un circuito protegido por un magnetotérmico de 16 A tiene una fuga de 80 mA a través de una persona. ¿Salta el magnetotérmico? ¿Qué protección debería actuar?
3. Por la fase de un circuito pasan 8,00 A y por el neutro vuelven 7,96 A. ¿Cuánta corriente se está fugando? ¿Saltará un diferencial de 30 mA?
4. Si una persona recibe una descarga y el diferencial salta, ¿ha pasado por ella una corriente de solo 30 mA?
5. El fusible de tu fuente, marcado «T 4 A», se ha fundido. Tienes a mano uno «F 4 A» y otro «T 10 A». ¿Cuál pones?
6. Vas a mirar el interior de una fuente de alimentación. La has apagado con su interruptor. ¿Qué falta antes de tocar nada?
7. ¿Por qué el condensador de entrada de una fuente conmutada se carga a más de 300 V, si la red es de 230 V?

**Soluciones**

1. Compara la corriente que va por la **fase** con la que vuelve por el **neutro**. Salta cuando la diferencia, que es lo que se fuga a tierra, llega a **30 mA**.
2. El magnetotérmico **no salta**: 80 mA son 0,08 A, muy por debajo de sus 16 A. Debe actuar el **diferencial**.
3. Se fugan 8,00 − 7,96 = 0,04 A = **40 mA**. Supera los 30 mA: el diferencial **salta**.
4. **No.** Ha pasado la que diga la ley de Ohm, que puede ser de 100 mA o más. El diferencial no la limita: hace que dure centésimas de segundo.
5. **Ninguno de los dos.** Hay que conseguir uno del mismo tipo y valor, «T 4 A». El rápido puede fundirse al encender; el de 10 A dejaría el equipo sin protección. Y si el nuevo también se funde, hay una avería.
6. **Desenchufarla** de la red (apagar no basta), **esperar** unos minutos y **comprobar con el voltímetro** que los condensadores grandes están descargados.
7. Porque 230 V es el valor **eficaz** de la red; el condensador se carga al valor de **pico**, que es 230 × 1,41 ≈ 325 V.

## En una frase

El diferencial corta cuando 30 mA se fugan a tierra y protege a las personas, aunque no limita la corriente sino el tiempo; el magnetotérmico y los fusibles cortan los excesos de corriente y protegen cables y equipos, no a ti; y un aparato no es seguro hasta que está desenchufado y se ha comprobado que sus condensadores están descargados.

La red eléctrica no es el único peligro de una estación. En las dos lecciones siguientes, los que son propios del oficio: la radiofrecuencia, las alturas y los rayos.
