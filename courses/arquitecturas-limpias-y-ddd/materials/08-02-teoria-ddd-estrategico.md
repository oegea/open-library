Todo el curso hasta aquí ha sido, sin decirlo, la mitad *táctica* del Domain-Driven Design: value objects, entidades, agregados, repositorios — los ladrillos. Esta sección presenta la mitad que Eric Evans consideraba más importante, la **estratégica**, y que la industria tardó una década en valorar en su justa medida: el lenguaje ubicuo, los bounded contexts y los mapas de contexto. Es la mitad que explica por qué murió Fénix con arquitectura moderna, y la que convierte la lámina plastificada de Marta de chuleta personal en plano de sistema.

## La tesis de Evans

El libro azul (*Domain-Driven Design: Tackling Complexity in the Heart of Software*, 2003) abre con una afirmación que reordena las prioridades de la profesión: la complejidad más dura del software no está en la tecnología, sino en el **dominio** — en el negocio mismo, sus conceptos, sus reglas, sus excepciones. Y de ahí la consecuencia: si lo difícil es el dominio, el activo central de un proyecto es el **modelo** que el equipo construye de ese dominio, y ese modelo se construye — no hay otra vía — **conversando con quienes lo conocen**: los expertos del dominio. Marta es la experta de dominio de Meridian. La media hora que Fénix le dedicó en dos años es la autopsia completa del proyecto.

## Lenguaje ubicuo: una palabra, un significado, en todas partes

La herramienta central del DDD estratégico es engañosamente simple. Del *DDD Reference* (Evans, 2015, CC BY 4.0; traducción propia):

> «Usa el modelo como columna vertebral de un lenguaje. Compromete al equipo a ejercitar ese lenguaje sin descanso en toda la comunicación dentro del equipo y en el código. Usa el mismo lenguaje en los diagramas, la escritura y especialmente el habla. [...] Reconoce que un cambio en el lenguaje ubicuo es un cambio en el modelo.»

Desmenucemos, porque cada pieza corrige un desastre conocido:

- **El mismo lenguaje en el habla Y en el código.** No dos idiomas con traductor — el negocio dice «abono» y el código dice `NegativeAmountAdjustment` —, sino uno: si Marta dice «compromiso pendiente de aplicar», existe una clase o un estado que se llama así, y viceversa. La razón es brutal por económica: **cada traducción es un sitio donde mentir sin saberlo**. ATLAS traducía «abono» a «importe negativo en la próxima factura» y esa traducción defectuosa costó años de hojas de cálculo paralelas.
- **Ejercitado sin descanso.** El lenguaje se construye y se vigila en cada conversación. Cuando un programador dice «bueno, en la base de datos eso es un flag en la tabla de ajustes», el lenguaje se está rompiendo; cuando alguien pregunta «¿"aplicar" y "liquidar" son lo mismo?» y la respuesta genera una discusión de veinte minutos entre Marta y contabilidad, el lenguaje está *funcionando* — acaba de descubrirse un pliegue del dominio que el modelo no conocía. Esas discusiones incómodas son el trabajo, no una distracción del trabajo.
- **Cambio de lenguaje = cambio de modelo = cambio de código.** Si el equipo descubre que «abono» eran tres conceptos, el código se refactoriza para decir tres cosas. Un glosario que evoluciona separado del código es un glosario muerto en dos meses; el diccionario de verdad es el propio código con sus tests — por eso importaba tanto (sección 7) que los tests se leyeran como frases de negocio.

La conexión con la sección 1 que cierra un círculo del curso: la regla «una palabra, un concepto» de los buenos nombres era la semilla de esto. El lenguaje ubicuo es aquella regla elevada de convención de equipo a **contrato entre departamentos**.

## Bounded contexts: las palabras tienen país

Y entonces, el problema de la historia: «abono» significa, legítimamente, tres cosas. ¿Quién gana? La respuesta de Evans es el concepto más importante de todo el DDD — según el propio Evans, que lo ha dicho en conferencias: si solo pudiera salvar una idea del libro, sería esta. Del *DDD Reference*:

> «Delimita explícitamente el contexto dentro del cual un modelo aplica. [...] Mantén el modelo estrictamente consistente dentro de esos límites, y no te distraigas ni te confundas por cuestiones de fuera.»

Un **bounded context** (contexto delimitado) es una frontera — de significado primero, de software después — dentro de la cual cada palabra del lenguaje ubicuo tiene **un** significado preciso. La jugada mental que libera: **no existe el modelo único de la empresa.** «Abono» no tiene una definición verdadera que descubrir; tiene tres definiciones verdaderas *en tres contextos*: en el contexto de **acuerdos comerciales**, es un compromiso con ciclo de vida (pactado → comunicado → aplicado); en el de **facturación**, un documento rectificativo con numeración legal; en el ATLAS histórico, un apaño que ninguno de los dos países reconoce como suyo. La pelea por «la definición correcta» — la guerra fría de departamentos que describía el faro — es un error de planteamiento: la paz no viene de que un bando gane, sino de **dibujar la frontera** y que cada modelo sea soberano en su territorio.

El intento contrario tiene nombre y cicatrices: el **modelo único corporativo** (*enterprise model*), la clase `Cliente` que intenta servir a ventas, contabilidad, logística y soporte a la vez. Acaba siendo la unión de todos los atributos y la intersección de ningún significado: cuarenta campos, la mitad nulos según quién la use, y cada departamento leyendo en ella una cosa distinta — el malentendido institucionalizado. Silvia tachando semanas de diagramas al descubrir que su única clase `Cliente` eran tres es el momento exacto en que descubrió los bounded contexts, con el libro en la mesa y el presupuesto agotado.

Para el software, la frontera de contexto se materializa donde ya lo has visto todo el curso: los **módulos**. La arquitectura destino organiza el código en `src/modules/{contexto}/`, cada uno con sus capas completas (`domain/application/infrastructure`): el módulo ES el bounded context hecho carpeta, con su lenguaje, sus entidades y sus reglas dentro de su frontera. Dos módulos pueden tener, cada uno, una clase con el mismo nombre y distinto contenido — `Abono` en `acuerdos/` y `Abono` en `facturacion/` — y eso no es duplicación: es soberanía. La duplicación sería forzar una sola clase a mentir en dos países.

¿Y cómo se decide por dónde cortar? Las señales prácticas, todas presentes en la historia: **donde el lenguaje cambia** (la misma palabra muta de significado al cruzar un pasillo: frontera), **donde cambian los expertos** (Marta es la autoridad de un lado; contabilidad de Vesta, del otro), **donde cambian los ritmos y motivos de cambio** (los acuerdos comerciales cambian con la negociación; la facturación, con la ley — el SRP de la sección 3, a escala de sistema). El corte técnico («el módulo de base de datos», «el módulo de APIs») nunca es un bounded context: los contextos cortan por el *significado*, no por la tecnología.

## Context mapping: las aduanas

Los contextos no viven aislados: los acuerdos comerciales *producen* rectificativas en facturación. El tercer instrumento estratégico es el **context map**: el dibujo honesto de qué contextos existen, quién habla con quién, y — crucial — **en qué términos**. Del *DDD Reference*: «Identifica cada modelo en juego y define su bounded context. [...] Describe los puntos de contacto entre los modelos, esbozando la traducción explícita para cualquier comunicación.»

La traducción explícita tiene su patrón estrella, el que la pizarra de Júlia pedía con su flecha «¿traducción?»: la **anticorruption layer** (capa anticorrupción, ACL) — una pieza de software cuyo único trabajo es traducir entre dos contextos para que el modelo de uno no se contamine con el del otro. En Meridian: cuando el contexto de acuerdos aplica un compromiso, una aduana lo traduce a lo que facturación entiende (una orden de rectificativa con sus datos legales); ninguno de los dos modelos conoce el vocabulario del otro. La lámina plastificada de Marta *era* una anticorruption layer ejecutada a mano por una persona durante quince años — la definición más conmovedora posible del patrón, y la medida exacta de lo que cuesta no escribirla en código.

El catálogo completo de relaciones entre contextos (quién manda, quién se adapta) queda para la ampliación; el principio rector cabe aquí: **las fronteras y sus traducciones se dibujan explícitamente o existen implícitamente y mal.** Un sistema sin context map también tiene relaciones entre contextos — en forma de malentendidos, hojas de cálculo y dos días trimestrales de cuadre manual.

## Por qué esto era la mitad que faltaba

Ahora se puede formular la autopsia completa de Fénix, y con ella la tesis de la sección:

- Fénix tenía (a medias) la mitad táctica: capas, patrones, código limpio. Le faltaba entera la estratégica: ni lenguaje compartido (veinte meses sin hablar con el negocio), ni contextos (un modelo único que copiaba a limpio los malentendidos de ATLAS), ni mapa (las quince mil verdades no tenían a quién preguntarse).
- El Monstruo, sin una sola capa limpia, *contenía* — mal expresado, sin fronteras — el conocimiento real. Por eso ganaba: en la única competición que importa, la del significado, el código horrible con conocimiento le gana siempre al código precioso sin él.
- La frase final del faro es la síntesis de todo el curso, y conviene llevársela literal: **el sistema acaba pareciéndose a las conversaciones que lo construyeron.** Es la versión para humanos de la ley de Conway (Melvin Conway, 1968: las organizaciones diseñan sistemas que copian sus estructuras de comunicación — el paper original, *How Do Committees Invent?*, está libre en su web). La arquitectura limpia hace barato cambiar el código; solo las conversaciones hacen *verdadero* el código. Se necesitan las dos, en ese orden de importancia.

## Para llevar

- DDD estratégico: la complejidad dura es el dominio; el activo central es el modelo; el modelo se construye conversando con los expertos (Marta > cualquier framework).
- Lenguaje ubicuo: una palabra, un significado, en el habla y en el código, sin traductores intermedios; cada traducción implícita es un sitio donde mentir sin saberlo. Cambio de lenguaje = cambio de código.
- Bounded context: la frontera dentro de la cual el modelo es consistente. No existe el modelo único: «abono» puede ser legítimamente tres cosas en tres contextos. Módulo = contexto hecho carpeta; mismo nombre en dos módulos ≠ duplicación, = soberanía.
- Señales de frontera: cambia el lenguaje, cambian los expertos, cambian los motivos de cambio. Nunca se corta por tecnología.
- Context map + anticorruption layer: las relaciones y traducciones entre contextos, explícitas y en código — o implícitas, manuales y pagadas en horas de alguien (la lámina de Marta).
- Ley de Conway: el sistema copia las conversaciones que lo construyeron. Fénix modeló un silencio. La deuda de conversaciones no la paga el código.

## Para profundizar

- Eric Evans, *DDD Reference* (CC BY 4.0) — entradas *Ubiquitous Language*, *Bounded Context*, *Context Map*: el destilado canónico, gratuito.
- Abel Avram & Floyd Marinescu, *Domain-Driven Design Quickly* (InfoQ, minilibro gratuito) — resumen honesto del libro azul, buen segundo paso.
- Martin Fowler, *BoundedContext* y *UbiquitousLanguage* en su bliki (gratuitos).
- Eric Evans, *Domain-Driven Design* (2003) — el libro azul completo; de pago; los capítulos estratégicos (parte IV) son los que releen los veteranos.
- ddd-crew (github.com/ddd-crew) — plantillas abiertas (CC) para talleres de context mapping y bounded context canvas: la versión moderna y facilitada de la mañana de pizarra de Júlia.
