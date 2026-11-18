Morientes, el vecino del 2.º B, se presentó con el mando de la tele en la mano: desde que Marina tenía «el aparato ese», la película se le llenaba de rayas, *ta-ta-tá, ta-ta-tá*. La prueba que organizaron —Vicente transmitiendo con su indicativo desde la estación de Marina, Lucía haciendo de enlace por el hueco de la escalera— dio un veredicto incómodo: con poca potencia, nada; con potencia media, la imagen se estropeaba. Y Vicente dictaminó algo que a primera vista parece contradictorio: «culpables, a medias».

Esta lección explica ese «a medias». Cuando una señal de radio molesta a un aparato ajeno hay dos causas posibles, completamente distintas, con responsables distintos y con remedios distintos. Saber distinguirlas es casi todo el trabajo, y es una de las preguntas más repetidas de esta parte del examen.

Al terminar sabrás qué es la compatibilidad electromagnética y cómo averiguar por cuál de los dos mecanismos se está interfiriendo. Los remedios, uno por uno, y lo que dice el reglamento quedan para la lección siguiente.

## Convivir en el mismo espacio

Hoy cualquier casa está llena de aparatos electrónicos, y todos comparten el mismo aire y los mismos cables. Cada uno genera señales eléctricas, a propósito o sin querer, y cada uno puede verse alterado por las de los demás.

> **Compatibilidad electromagnética (EMC):** del inglés *ElectroMagnetic Compatibility*; la capacidad de un aparato para funcionar correctamente en su entorno sin causar perturbaciones a otros aparatos y sin resultar perturbado por ellos.

La definición tiene dos mitades:

- **No molestar**: lo que un aparato emite sin deber. Se llama *emisión*.
- **No dejarse molestar**: lo bien que aguanta las señales ajenas. Se llama *inmunidad*.

Un radioaficionado vive en los dos lados. Tiene un transmisor potente, así que puede molestar. Y tiene un receptor sensibilísimo, así que casi todo le molesta. Esta lección y la siguiente tratan el primer lado; la última de la sección, el segundo.

Una aclaración antes de seguir. Morientes habló de «rayas», que es como se ha dicho toda la vida y como se veían las interferencias en la televisión analógica. La televisión digital de hoy no hace rayas: cuando algo la perturba, la imagen **se pixela, se congela o aparece el aviso de «sin señal»**. Esos son los síntomas que hay que buscar.

## Primer caso: la señal sale sucia

Recuerda de la sección 7 que, además de la señal que se quiere emitir, un transmisor puede emitir otras que no se quieren:

- **Armónicos:** señales en los múltiplos exactos de la frecuencia de transmisión. Si se transmite en 7 MHz, los armónicos están en 14, 21, 28 MHz…
- **Espurias:** cualquier otra emisión fuera del canal que no sea un armónico, producida por un defecto de diseño o por una avería.

Si una de esas señales cae justo sobre la frecuencia en la que otro aparato está recibiendo, ese aparato la recibe como si fuera una emisora más. Y hace bien: está funcionando exactamente como debe.

**Ejemplo.** *Un aficionado transmite en la banda de 2 metros, en 145 MHz. ¿Dónde cae su cuarto armónico?*

4 × 145 = 580 MHz. La televisión digital terrestre se emite entre unos 470 y 694 MHz. Si ese transmisor tiene un cuarto armónico apreciable, cae en mitad de la banda de televisión. (Del mismo modo, el segundo armónico de una emisión en 50 MHz cae en 100 MHz, en plena banda de radio FM.)

En este caso **el defecto está en el transmisor**, y el aparato del vecino es inocente. El remedio se aplica en la estación:

- Un **filtro paso bajo** a la salida del transmisor. Recuerda de la sección 5: deja pasar las frecuencias por debajo de su frecuencia de corte y atenúa las superiores. La señal pasa; sus armónicos, que están siempre por encima, se quedan. Los equipos comerciales lo llevan dentro, pero un amplificador externo o un equipo antiguo pueden necesitar uno añadido.
- **No saturar** el equipo: ni micrófono excesivo ni amplificador forzado. La saturación deforma la señal, y la deformación es la fábrica de armónicos.
- **Reparar** el equipo si las emisiones no deseadas vienen de una avería.

## Segundo caso: la señal es limpia, y aun así entra

Ahora supón que el transmisor es impecable: emite solo en su frecuencia, sin armónicos ni espurias apreciables. ¿Puede molestar igualmente? Sí.

Esa señal, perfectamente legal, es **muy fuerte** en los alrededores de la antena. Y el aparato del vecino puede no estar preparado para tener cerca una señal tan fuerte, aunque sea en una frecuencia que no le interesa en absoluto.

> **Sobrecarga por la fundamental** (en inglés, *fundamental overload*): interferencia que sufre un aparato cuando una señal fuerte y limpia, en la frecuencia correcta del transmisor, entra en él porque no está suficientemente protegido. Se llama así porque la causa es la frecuencia principal del transmisor (la *fundamental*), no un armónico.

Lo que le ocurre por dentro al aparato tiene tres formas, y dos las conoces de la sección 7:

- Se **bloquea**: su primera etapa se satura con la señal fuerte y deja de recibir lo suyo.
- **Intermodula**: mezcla la señal fuerte con otras y fabrica dentro señales que no existen fuera.
- **Detecta**, si es un aparato de audio. Cualquier diodo o transistor de su entrada rectifica la radiofrecuencia, igual que el detector de AM de la sección 6, y lo que sale por el altavoz es la modulación: la voz del aficionado, hecha un gangueo si emite en banda lateral. Por eso unos altavoces de ordenador, que no son ninguna radio, pueden «recibir» una emisión.

Y la señal entra por tres vías: por la **entrada de antena** del aparato, por **los demás cables** (alimentación, altavoces, teléfono), que hacen de antena, o **directamente** a través de una caja de plástico que no la detiene.

Los candidatos típicos son los aparatos baratos o con años: televisores con un **amplificador de antena** de mala calidad, que amplifica todo lo que le llega sin distinguir, como el «de oferta» de Morientes; altavoces de ordenador; porteros automáticos, teléfonos, alarmas, lámparas con regulador táctil que se encienden solas.

En este caso, **el defecto técnico está en el aparato afectado**, que no tiene la inmunidad que debería. Y el remedio se aplica **en ese aparato**: un filtro paso bajo en el transmisor no arregla nada, porque no hay ningún armónico que quitar.

![Las dos formas de interferir. Arriba, emisión no deseada: el transmisor emite, además de su señal, un armónico que cae dentro de la banda del televisor; el fallo está en el transmisor y se corrige con un filtro paso bajo. Abajo, sobrecarga por la fundamental: el transmisor emite solo su señal, limpia, pero es tan fuerte que entra en un televisor mal protegido; se corrige en el televisor, con ferritas y un filtro paso alto.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s10-armonico-o-sobrecarga.svg)

| | Emisión no deseada | Sobrecarga por la fundamental |
|---|---|---|
| Qué ocurre | El transmisor emite donde no debe (armónicos, espurias) | Una señal correcta es demasiado fuerte para un aparato mal protegido |
| Dónde está el defecto | En el **transmisor** | En el **aparato afectado** |
| Dónde se arregla | En la **estación**: filtro paso bajo, no saturar, reparar | En el **aparato**: ferritas, filtros, blindaje |
| Pista típica | Afecta a una frecuencia concreta, relacionada con un múltiplo de la de transmisión | Afecta a todo, o a aparatos que ni siquiera son receptores de radio |

## Cómo saber cuál de las dos es

Vicente no opinó. Montó una prueba. El método tiene pocos pasos y sirve para cualquier caso.

1. **Comprobar que la interferencia coincide con las transmisiones.** Con un observador delante del aparato afectado y alguien avisando de cuándo se transmite y cuándo no. Si la imagen se estropea también cuando nadie transmite, la causa es otra.
2. **Probar con potencias crecientes.** Las dos causas mejoran al bajar la potencia, así que este paso no distingue entre ellas, pero da un remedio provisional: la potencia a la que el problema desaparece.
3. **Probar banda a banda.** Quizá solo ocurre en una.
4. **Fijarse en qué se ve afectado.** En la televisión digital, varios programas comparten una misma frecuencia, formando lo que se llama un *múltiple*. Si se va un solo múltiple (un grupo de cuatro o cinco programas a la vez) y su frecuencia coincide con un múltiplo de la de transmisión, hay que sospechar de un armónico. Si se van todos, o el afectado no es un receptor de radio, hay que sospechar de sobrecarga.
5. **Probar el filtro paso bajo.** Si al intercalarlo desaparece el problema, eran armónicos. Si sigue exactamente igual, es sobrecarga.
6. **Apuntarlo todo.** Fecha, banda, potencia, resultado. La libreta, otra vez.

En el caso Morientes el resultado fue mixto, que es lo más habitual: un televisor con un amplificador que tragaba lo que no debía, y una estación a la que tampoco le sobraba una revisión. De ahí el «a medias», y de ahí que Vicente actuara en los dos lados: ferritas en casa del vecino, y filtro paso bajo y un repaso a las conexiones en la estación.

## Donde la gente se lía

- **«Si mi transmisor es legal y limpio, no puedo interferir.»** Puedes, por sobrecarga, a aparatos mal protegidos.
- **«Si hay interferencia, la culpa es siempre del radioaficionado.»** A menudo el defecto técnico está en el aparato afectado. Por eso se mide.
- **«Armónico y sobrecarga por la fundamental son lo mismo.»** Son lo contrario: en un caso se emite donde no se debe; en el otro se emite donde se debe y el aparato no lo soporta.
- **«Si al bajar la potencia desaparece, es sobrecarga.»** Los armónicos también bajan con la potencia. Ese dato no distingue.
- **«La tele hace rayas.»** La televisión digital se pixela, se congela o se queda sin señal.

## Compruébalo tú

1. Una estación transmite en 28,5 MHz. ¿En qué frecuencias están su segundo y su tercer armónico?
2. Cuando una estación transmite en 145 MHz, un vecino pierde un grupo de programas de televisión que comparten la misma frecuencia, cerca de 580 MHz; los demás se ven bien. ¿Qué causa es la más probable?
3. Otro vecino dice que por los altavoces de su ordenador sale, deformada, la voz del aficionado. ¿Es un armónico o una sobrecarga? ¿Qué ocurre dentro de los altavoces?
4. Se intercala un filtro paso bajo a la salida del transmisor y la interferencia en el televisor del vecino sigue exactamente igual. ¿Qué se ha averiguado?
5. En una prueba, la interferencia desaparece al bajar de 100 W a 20 W. ¿Sirve ese dato para saber si es un armónico o una sobrecarga?
6. Un portero automático emite un zumbido cada vez que un aficionado cercano transmite. No tiene antena. ¿Por dónde puede estar entrando la señal?
7. Un televisor pierde la imagen a ratos, también cuando la estación del vecino radioaficionado está apagada. ¿Es él la causa?

**Soluciones**

1. Segundo: 2 × 28,5 = **57 MHz**. Tercero: 3 × 28,5 = **85,5 MHz**.
2. Un **armónico**: 4 × 145 = 580 MHz, un múltiplo exacto, y afecta solo a esa frecuencia.
3. Una **sobrecarga por la fundamental**. Los altavoces no son un receptor: la señal se cuela por sus cables y algún componente de su entrada la **detecta**, como un detector de AM.
4. Que **no son armónicos**. Lo más probable es una sobrecarga, y hay que actuar en el televisor.
5. **No.** Las dos causas mejoran al bajar la potencia. Sirve como remedio provisional, no como diagnóstico.
6. Por **sus cables** (los de alimentación y los que recorren el edificio hasta cada vivienda, que hacen de antena) o **directamente** a través de su caja de plástico. La tercera vía, la entrada de antena, aquí no existe.
7. **No.** Si ocurre sin que nadie transmita, la causa es otra. Es lo primero que se comprueba.

## En una frase

Hay dos formas de interferir: emitiendo donde no se debe (armónicos y espurias, defecto del transmisor) o emitiendo bien pero tan fuerte que un aparato mal protegido se bloquea, intermodula o detecta la señal (sobrecarga por la fundamental, defecto del aparato); se distinguen midiendo, y casi siempre hay un poco de las dos.

Sabemos ya diagnosticar. En la lección siguiente, las piezas que lo arreglan y lo que el reglamento pide.
