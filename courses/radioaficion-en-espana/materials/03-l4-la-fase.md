De una onda importan tres cosas: lo deprisa que oscila, lo grande que es y por dónde va. Las dos primeras ya las tienes: frecuencia y amplitud. Esta lección, corta, es la tercera.

Al terminar sabrás qué es la fase de una onda, cómo se mide en grados, qué significa que dos ondas vayan en fase, en oposición de fase, adelantadas o retrasadas, y por qué dos señales idénticas pueden sumarse hasta dar el doble o anularse hasta dar cero. Ahora parecerá un detalle; más adelante resultará ser el secreto de las antenas.

## En qué punto del ciclo estás

> **Fase:** el punto del ciclo en el que se encuentra una onda en un instante dado.

Para indicar ese punto se usa la misma medida que para las vueltas de una rueda: los grados. Recuerda que la senoide sale de algo que gira; un ciclo completo es una vuelta completa, y una vuelta son **360 grados (360°)**.

| Punto del ciclo | Fase |
|---|---|
| Inicio (cruza el cero subiendo) | 0° |
| Cresta | 90° (un cuarto de ciclo) |
| Cruza el cero bajando | 180° (medio ciclo) |
| Valle | 270° (tres cuartos de ciclo) |
| Fin del ciclo, que es el inicio del siguiente | 360° |

La fase de una sola onda, por sí misma, sirve de poco. Cobra sentido al **comparar dos ondas de la misma frecuencia**. Piensa en dos niños en dos columpios iguales, que tardan lo mismo en ir y volver:

- Si se columpian a la par —los dos delante a la vez, los dos detrás a la vez—, van **en fase**. La diferencia de fase entre ellos es de 0°.
- Si uno está delante cuando el otro está detrás, van **en oposición de fase** (o *en contrafase*). La diferencia es de medio ciclo: 180°.
- Entre un caso y otro caben todas las situaciones intermedias. Si uno llega a su punto más alto justo cuando el otro pasa por el centro, están **desfasados** un cuarto de ciclo: 90°.

### Adelantada y retrasada

Cuando dos ondas van desfasadas, hay que decir además cuál va por delante:

> Si una onda llega a su cresta **antes** que la otra, se dice que va **adelantada**; la otra va **retrasada**. Un cuarto de ciclo de ventaja son 90° de adelanto.

Es lo mismo que en los columpios: el niño que llega primero arriba va adelantado. Estas dos palabras te harán falta muy pronto. En las secciones 4 y 5 verás que hay componentes —los condensadores y las bobinas— que hacen que la corriente no vaya a la par de la tensión, sino un cuarto de ciclo adelantada o retrasada respecto a ella.

### Qué pasa cuando dos ondas se juntan

Lo interesante llega cuando dos ondas de la misma frecuencia llegan a la vez al mismo sitio: por ejemplo, dos señales de radio a la misma antena. Lo que la antena recibe es la suma de las dos, instante a instante. Y el resultado depende por completo de su fase:

- **En fase**, las crestas coinciden con las crestas y los valles con los valles. Las dos ondas se refuerzan: el resultado es una onda mayor. Si son iguales, del doble de amplitud.
- **En oposición de fase**, la cresta de una coincide con el valle de la otra. En cada instante, lo que una empuja hacia un lado, la otra lo empuja hacia el contrario. Si son iguales, **se anulan por completo**: el resultado es cero.

![Dos casos, uno encima del otro. Arriba, dos ondas iguales en fase: sus crestas coinciden y su suma es una onda del doble de altura. Abajo, dos ondas iguales en oposición de fase, a 180 grados: la cresta de una coincide con el valle de la otra y su suma es una línea recta en el cero; se anulan.](https://raw.githubusercontent.com/oegea/open-library/main/media/radioaficion/s03-fase.svg)

—¿Dos señales que juntas dan… nada? —preguntó Marina.

—Dos señales que juntas dan nada —confirmó Vicente—. O el doble. Según cómo lleguen. Apúntatelo, porque de ahí sale que una antena envíe más señal hacia un lado que hacia otro, y de ahí sale que una emisora lejana suba y baje de volumen ella sola. Lo verás en su momento.

No hace falta más por ahora. Quédate con la idea: **dos ondas de la misma frecuencia pueden reforzarse o anularse, y lo que decide una cosa u otra es su diferencia de fase.** Volverá en las secciones 4 y 5 (condensadores y bobinas), en la 8 (antenas) y en la 9 (propagación).

## Donde la gente se lía

- **Confundir fase y frecuencia.** Dos ondas pueden tener exactamente la misma frecuencia e ir desfasadas, como dos columpios iguales que no van a la par. La frecuencia dice cada cuánto se repiten; la fase, en qué punto de la repetición está cada una.
- **«Dos señales juntas siempre dan más señal.»** Solo si llegan en fase. En oposición de fase dan menos, y si son iguales, nada.
- **«Desfasadas 360° es lo más desfasadas que pueden estar.»** Trescientos sesenta grados es una vuelta completa: vuelven a ir a la par. Lo más opuesto posible son 180°.

## Compruébalo tú

1. ¿Qué diferencia de fase, en grados, corresponde a medio ciclo? ¿Y a un cuarto de ciclo?
2. Dos ondas iguales, de la misma frecuencia y 5 V de pico, se suman en fase. ¿Qué valor de pico tiene el resultado? ¿Y si se suman en oposición de fase?
3. Una onda está en su cresta en el mismo instante en que otra, de la misma frecuencia, cruza el cero subiendo. ¿Qué diferencia de fase hay entre ellas? ¿Cuál de las dos va adelantada?
4. ¿En qué fase del ciclo está una onda cuando pasa por su valle?
5. A una antena llegan dos copias de la misma señal por dos caminos distintos. Unas veces la señal recibida es muy fuerte y otras casi desaparece. ¿Qué está cambiando?

**Soluciones**

1. Un ciclo son 360°: medio ciclo son **180°** (la oposición de fase) y un cuarto de ciclo, **90°**.
2. En fase se refuerzan: **10 V** de pico. En oposición de fase se anulan: **0 V**.
3. La cresta está a 90° del inicio del ciclo, así que van desfasadas **90°**. Va **adelantada** la que ya está en la cresta: la otra todavía tardará un cuarto de ciclo en llegar a la suya.
4. En **270°**: tres cuartos de ciclo.
5. La **diferencia de fase** con la que llegan las dos copias. Cuando llegan en fase se refuerzan; cuando llegan en oposición, se anulan. (Es la causa de que las emisoras lejanas suban y bajen de volumen solas; lo verás en la sección 9.)

## En una frase

La fase dice en qué punto de su ciclo está una onda, en grados (360° el ciclo entero); dos ondas de la misma frecuencia pueden ir en fase, en oposición (180°) o una adelantada respecto a otra, y al sumarse se refuerzan o se anulan según esa diferencia.

Ya sabes describir del todo una onda dentro de un cable: su ritmo, su tamaño y su fase. En la lección siguiente la onda sale del cable, y aparece la medida que da nombre a todas las bandas: la longitud de onda.
