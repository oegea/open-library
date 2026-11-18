Cuando Vicente arregló el televisor de Morientes dejó, «de propina», una ferrita más: para el cargador del portátil de su mujer, «que ese bicho mete más ruido en mis bandas que tú películas ves». Con esa frase le dio la vuelta a la situación. El vecino había venido a quejarse de una interferencia, y resultó que en su casa había un aparato que estaba interfiriendo al radioaficionado.

Esta lección trata ese otro lado. Es, con diferencia, el problema más frecuente del radioaficionado de hoy, sobre todo si vive en una ciudad: no que él moleste, sino que el ruido eléctrico de las casas le tape las señales que quiere oír.

Al terminar sabrás qué es el ruido de fondo y por qué importa tanto, qué aparatos lo generan, cómo se localiza al culpable con un método de detective y qué derechos y obligaciones marca la ley.

## El ruido: el suelo sobre el que se escucha

Enciende un receptor de onda corta en una frecuencia donde no haya nadie. No oirás silencio: oirás un soplido continuo. Eso es **ruido**: energía de radio sin orden ni mensaje, que llega de todas partes.

Una parte es natural e inevitable, y la conoces del final de la sección anterior: el ruido atmosférico de las tormentas de medio planeta y el ruido galáctico. Otra parte la fabricamos nosotros con nuestros aparatos.

> **Ruido de fondo:** el nivel de ruido que hay en una frecuencia cuando no hay ninguna señal. Es el «suelo» por debajo del cual no se puede oír nada.

Recuerda de la sección 7 que la sensibilidad de un receptor no la limita la amplificación —amplificar es fácil— sino el ruido: una señal solo se entiende si sobresale por encima de él. Da igual lo bueno que sea tu receptor: una señal más débil que el ruido de fondo de tu casa no existe para ti.

Es como intentar oír a alguien que te habla desde lejos. En el campo, de noche, lo oyes a cien metros. En un bar lleno, no lo oyes a tres. La persona habla igual de fuerte: lo que ha cambiado es el ruido.

![El ruido de fondo y las señales. A la izquierda, en un lugar tranquilo, el ruido de fondo es bajo y se distinguen tres señales, incluida una débil. A la derecha, en un lugar con mucho ruido eléctrico, el suelo de ruido ha subido: la señal fuerte todavía sobresale, pero las otras dos han quedado enterradas.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s10-ruido-de-fondo.svg)

En una casa de campo, lejos de todo, el ruido de fondo en la banda de 40 metros puede ser muy bajo. En un piso de ciudad puede estar decenas de decibelios por encima. Y recuerda de la sección 3 lo que eso significa: cada 10 dB es una potencia diez veces mayor. Con 20 dB más de ruido, una estación lejana tendría que llegarte cien veces más fuerte para que la oyeras igual.

## Quién hace ruido

Casi todo el ruido doméstico tiene el mismo origen: aparatos que **conmutan** la corriente, es decir, que la cortan y la conectan muy deprisa.

Recuerda de la sección 3 que una onda deformada, que no sea una senoide suave, contiene armónicos: frecuencias en los múltiplos de la suya. Una corriente que se corta y se conecta bruscamente es la onda más deformada posible, y sus armónicos se extienden a lo largo de megahercios enteros. Si el aparato no lleva buenos filtros, esos armónicos salen por sus cables, que hacen de antena, y siembran de ruido las bandas de radio.

Los culpables habituales:

- **Las fuentes conmutadas baratas** (sección 5): cargadores de móvil y de portátil, alimentadores de routers y de televisores, y las fuentes de las tiras y bombillas LED (esas cajitas que a veces se venden como «transformadores electrónicos»). Trocean la corriente decenas o cientos de miles de veces por segundo. Las buenas llevan filtros; las malas, que son las más baratas, se los ahorran.
- **Los motores con escobillas**: taladros, batidoras, aspiradoras. Cada chispa interna es un pequeño estallido de radio. Hacen mucho ruido, pero solo mientras funcionan.
- **Los reguladores y termostatos**: reguladores de luz, mantas eléctricas, calderas, cercas eléctricas del campo.
- **Las instalaciones solares**: los inversores y, sobre todo, los optimizadores que se colocan debajo de cada panel, cuando son de mala calidad o están mal instalados. Con la extensión de los paneles en los tejados se han convertido en una de las fuentes de ruido más frecuentes.
- **El PLC** (del inglés *Power Line Communications*): los adaptadores que llevan la conexión de Internet de una habitación a otra **por los cables de la luz**. Para ello inyectan a propósito señales de radio, precisamente en las frecuencias de la onda corta, en unos cables que no están hechos para eso y que las radian. Algo parecido ocurre con algunas conexiones de Internet por el par de cobre del teléfono.

—¿Y cómo sé que es ruido de un aparato y no que la banda está mala? —preguntó Marina.

—Por el sonido y por el reloj —dijo Vicente—. El ruido natural es un soplido liso, o los chasquidos sueltos de las tormentas. El de los aparatos tiene dibujo: un zumbido, un *ta-ta-tá* regular, o un ruido que aparece, desaparece y vuelve a aparecer a intervalos iguales conforme giras el dial. Y tiene horario: aparece cuando alguien enciende algo y desaparece cuando lo apaga. Si tu ruido empieza cada tarde a la hora en que el vecino llega a casa, ya sabes mucho.

## El método del detective

El ruido eléctrico se encuentra igual que una gotera: descartando.

### Primer paso: ¿es de fuera o de mi casa?

Hace falta un receptor que funcione **con pilas** y que reciba esas frecuencias: una radio portátil de onda media o de onda corta. (Un walkie de VHF no sirve: no oye la onda corta.) Se sintoniza donde se oiga el ruido y, con él en la mano, se va al cuadro eléctrico y se **corta el interruptor general** de la vivienda.

Antes de cortar, avisa en casa y piensa en lo que no debe apagarse de golpe: ordenadores, aparatos médicos, el congelador si va a ser para rato. Y recuerda que lo que lleva batería —un portátil, un sistema de alimentación ininterrumpida, un inversor solar— sigue funcionando, y haciendo ruido, con el general bajado.

- Si el ruido **desaparece**, el culpable está en tu casa.
- Si **sigue igual**, viene de fuera.

Los veteranos lo dicen sin anestesia: más de la mitad de las veces, el ruido es propio. Antes de mirar al vecino, se mira uno a sí mismo.

### Segundo paso: si es de casa, ¿de qué circuito?

Vuelve a conectar el general y ve cortando los interruptores del cuadro **uno a uno**. Cuando al bajar uno desaparezca el ruido, ya sabes en qué circuito está: la cocina, los dormitorios, el salón.

### Tercer paso: ¿qué aparato?

En ese circuito, ve **desenchufando** los aparatos uno por uno. Desenchufar, no apagar: muchas fuentes siguen funcionando, y haciendo ruido, con el aparato «apagado». Cuando el ruido cese, has encontrado al culpable.

También sirve el método contrario: pasear la radio portátil por la casa, acercándola a cada aparato. Junto al culpable, el ruido sube de forma inconfundible.

### Cuarto paso: si es de fuera

Con la radio portátil en la calle, se camina buscando hacia dónde crece el ruido. Si el receptor tiene una antena direccional —una radio de onda media con su antena de ferrita interior lo es: el ruido casi desaparece cuando uno de los extremos del aparato señala hacia la fuente—, se puede incluso marcar la dirección. La radio no dice en cuál de los dos sentidos de esa dirección está la fuente; eso se averigua caminando. Con paciencia se llega a un portal, a una farola o a un poste concreto.

## Los remedios

Una vez encontrado el culpable, por orden de eficacia:

1. **Sustituirlo.** Un cargador ruidoso de cinco euros se cambia por uno decente y se acabó. Con las fuentes de las tiras LED ocurre igual. Es casi siempre lo más barato y lo más eficaz.
2. **Ferritas en sus cables**, lo más cerca posible del aparato y con varias vueltas. Funcionan por la misma razón que en la lección anterior: frenan la radiofrecuencia que sale por el exterior de los cables. Aquí se usan en sentido contrario: no para que la señal no entre, sino para que el ruido no salga.
3. **Alejar tu antena del ruido.** El ruido doméstico es fuerte muy cerca de los cables de las casas y se diluye deprisa al alejarse. Una antena en la azotea, alta y separada de las viviendas, recibe mucho menos que un hilo en el balcón, pegado a todos los cargadores del edificio. Es el segundo dividendo de la antena de la azotea: emite mejor y escucha más limpio.
4. **Un cable coaxial de buen blindaje y un balun** en la antena, para que la bajada no recoja el ruido del edificio por el camino.

Y cuando el aparato culpable es de otra persona, vale lo aprendido con Morientes: llamar a la puerta con buen tono, enseñar el problema con la radio portátil y ofrecer la solución, mejor que exigirla. Una ferrita o un cargador nuevo regalado sale más barato que un conflicto.

## El marco legal: derechos y deberes

La compatibilidad electromagnética no depende solo de la buena voluntad. Hay tres niveles de normas, y los tres pueden aparecer en el examen.

**Los aparatos.** Todo equipo eléctrico o electrónico que se vende en la Unión Europea debe cumplir las normas europeas de compatibilidad electromagnética: no emitir perturbaciones por encima de ciertos límites y soportar un nivel razonable de las ajenas. El **marcado CE** es la declaración del fabricante de que su producto las cumple. En la práctica, muchos aparatos muy baratos lo llevan sin cumplirlas, y de ahí viene buena parte del ruido.

**El radioaficionado.** Tiene un deber y un derecho, que son las dos caras de lo mismo:

- El **deber** de no causar interferencias perjudiciales a otros servicios, y de corregirlas si las causa. Es de lo que trata el artículo 32 del reglamento, que viste en la lección anterior.
- El **derecho** a que sus comunicaciones, en las bandas que tiene atribuidas, estén protegidas frente a las interferencias perjudiciales de otros.

Un matiz que conocerás a fondo en la sección 12: esa protección depende de la categoría con la que el servicio de aficionados tiene atribuida cada banda. Donde es *primario*, puede reclamar protección frente a las interferencias perjudiciales de otras estaciones. Donde es *secundario*, no puede reclamarla frente a los servicios primarios de esa misma banda, ni causarles interferencia.

**La Administración.** Cuando no hay acuerdo posible, quien investiga y resuelve es la Administración de telecomunicaciones (en la práctica, las Jefaturas Provinciales de Inspección de Telecomunicaciones, las mismas ante las que te examinarás). Si acudes a ella, tu caso será mucho más sólido si va acompañado de lo que ya sabes hacer: fechas, horas, frecuencias y medidas apuntadas en la libreta.

## Donde la gente se lía

- **«Con un receptor mejor oiré más.»** Si tu límite es el ruido de tu casa, no. Hay que bajar el ruido, no subir el precio del receptor.
- **«El ruido viene siempre de los vecinos.»** Lo primero es cortar el interruptor general de tu propia vivienda. Muy a menudo es tuyo.
- **«Si el aparato está apagado, no hace ruido.»** Muchas fuentes siguen funcionando con el aparato apagado. Hay que desenchufar.
- **«Lleva marcado CE, luego no puede interferir.»** El marcado es una declaración del fabricante, no una garantía de que el aparato concreto esté bien hecho.
- **«Como tengo licencia, nadie me puede interferir en ninguna banda.»** La protección depende de si la banda está atribuida a los aficionados a título primario o secundario.
- **«Mi walkie me sirve para buscar el ruido.»** Solo si el ruido está en VHF. Para el de onda corta hace falta un receptor que la reciba.

## Compruébalo tú

1. ¿Qué es el ruido de fondo y por qué limita lo que puedes escuchar?
2. Tu ruido de fondo en 40 metros sube 10 dB cuando el vecino enciende sus luces LED. ¿Cuántas veces más potente tiene que llegarte ahora una señal para oírla igual que antes?
3. En tu receptor aparece cada tarde, a las ocho, un zumbido que se repite a intervalos regulares a lo largo del dial, y que desaparece hacia medianoche. ¿Ruido natural o de un aparato? ¿En qué te basas?
4. Con una radio de onda corta a pilas en la mano, cortas el interruptor general de tu casa y el ruido desaparece. ¿Qué has averiguado y cuál es el paso siguiente?
5. Has localizado al culpable: el cargador de un portátil. Enumera dos remedios, del mejor al peor.
6. Has hablado dos veces con el dueño de un local cuya instalación te tapa la banda de 20 metros y no quiere hacer nada. ¿A quién puedes acudir, y qué te conviene llevar?

**Soluciones**

1. Es el nivel de ruido que hay en una frecuencia cuando no hay señal. Limita la escucha porque una señal solo se entiende si sobresale por encima de él: las más débiles que el ruido quedan enterradas, por bueno que sea el receptor.
2. **Diez veces** más potente: 10 dB equivalen a multiplicar la potencia por 10.
3. **De un aparato.** Tiene dibujo regular (un zumbido que se repite a intervalos) y tiene horario: empieza y termina a horas fijas, como algo que alguien enciende y apaga. El ruido natural es un soplido liso o chasquidos sueltos.
4. Que el ruido lo produce algo **de tu propia casa**. El paso siguiente es conectar de nuevo el general e ir cortando los interruptores del cuadro uno a uno para saber en qué circuito está, y luego desenchufar los aparatos de ese circuito de uno en uno.
5. Primero, **sustituirlo** por un cargador de mejor calidad. Segundo, poner **ferritas** en sus cables, con varias vueltas y cerca del cargador.
6. A la **Administración de telecomunicaciones** (la Jefatura Provincial de Inspección). Conviene llevar un registro de fechas, horas, frecuencias y medidas que documente la interferencia.

## En una frase

Lo que limita la escucha no es el receptor sino el ruido de fondo, y en una ciudad casi todo ese ruido sale de aparatos que conmutan corriente sin filtros suficientes; se localiza descartando —primero tu casa, luego circuito a circuito, luego aparato a aparato— y se arregla cambiando el culpable, con ferritas o alejando la antena, antes de recurrir a una Administración que ampara tu derecho a no ser interferido tanto como tu deber de no interferir.

Con esto termina la sección. El material siguiente es su resumen en formato de chuleta, para repasar antes del examen.
