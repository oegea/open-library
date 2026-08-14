Si de este curso solo pudieras llevarte una sección, sería esta. No porque las demás sobren, sino porque esta contiene la idea que ordena todas las demás: la razón por la que el riego fantasma no fue un accidente de inteligencia artificial sino algo mucho más viejo, y la razón por la que tu oficio, en la era en que las máquinas escriben código, vale más y no menos. La idea tiene cuarenta años, cabe en una frase y casi nadie que programa la conoce: **programar no es producir código; es construir una teoría.**

## Naur, 1985: el texto que explica el 14 de marzo

Peter Naur fue uno de los grandes de la primera generación: coeditor del informe de la OTAN que viste en la sección 1, editor del informe del lenguaje ALGOL 60, premio Turing 2005. En 1985 publicó un ensayo breve titulado *Programming as Theory Building* («Programar como construcción de una teoría») que durante décadas circuló casi en secreto, fotocopiado entre iniciados, hasta que la era de los agentes lo volvió urgente. Su tesis, en sus palabras:

> «programming properly should be regarded as an activity by which the programmers form or achieve a certain kind of insight, a theory, of the matters at hand»
> («programar debería entenderse propiamente como una actividad mediante la cual los programadores forman o alcanzan cierto tipo de comprensión, una teoría, de los asuntos entre manos» — traducción propia. Naur, *Programming as Theory Building*, 1985.)

¿Qué es esa «teoría»? No es la documentación, ni los comentarios, ni el diseño escrito. Es el conocimiento vivo que tiene quien construyó el sistema: saber cómo se corresponde cada parte del código con el mundo real al que sirve, *por qué* está hecho así y no de otra manera, y cómo habría que modificarlo para que siguiera teniendo sentido. Naur toma la noción de teoría del filósofo Gilbert Ryle: tener una teoría no es poder recitar hechos, es *poder hacer* — explicar, justificar, responder a lo imprevisto. El programa de Vega calculaba offsets solares; la teoría era saber que aquellas fechas sin zona horaria *representaban un acuerdo de 1974 anclado al amanecer*, y que por eso normalizarlas a UTC — la corrección de manual — era destruirlas. El código decía `schedule_offsets.py`. La teoría decía «hora de acequia». Entre lo uno y lo otro media exactamente el incidente del capítulo 1.

Naur extrae consecuencias que en 1985 sonaban filosóficas y en 2026 son operativas. La primera: los programas mueren, y no mueren cuando se borra el código:

> «The death of a program happens when the programmer team possessing its theory is dissolved… Revival of a program is the rebuilding of its theory by a new programmer team.»
> («La muerte de un programa ocurre cuando se disuelve el equipo de programadores que posee su teoría… La resurrección de un programa es la reconstrucción de su teoría por un nuevo equipo.» — traducción propia.)

Azud murió, en el sentido de Naur, el día que Joel se marchó a Berlín con la teoría de los offsets en la cabeza. Siguió *ejecutándose* dos años más — los programas muertos se ejecutan perfectamente —, pero ya nadie podía modificarlo con seguridad, y la prueba llegó la primera vez que alguien (una máquina, da igual) lo modificó con total competencia técnica y total ignorancia de la teoría. La segunda consecuencia es más dura:

> «program revival, that is reestablishing the theory of a program merely from the documentation, is strictly impossible.»
> («la resurrección de un programa, es decir, restablecer su teoría meramente a partir de la documentación, es estrictamente imposible.» — traducción propia.)

«Estrictamente imposible» — Naur no era hombre de hipérboles. La documentación ayuda, los tests ayudan, el código ayuda; pero la teoría solo se reconstruye *trabajando*: explorando el sistema, proponiendo cambios, equivocándose, hablando con quien sabe — que es literalmente lo que el equipo hace en el capítulo con su mapa de cajas verdes y naranjas, y lo que Nadia y Tomás hacen en la mesa camilla de Paca. Fíjate en que la fuente decisiva de la teoría de Azud no estaba en ningún repositorio: estaba en un acta de 1974 y en la cabeza de una regante de sesenta y tres años. La teoría de un sistema siempre excede su texto. Y la tercera consecuencia, la que Naur escribió contra la industria de su época y parece escrita contra la nuestra:

> «the notion of the programmer as an easily replaceable component… has to be abandoned.»
> («la noción del programador como componente fácilmente reemplazable… debe abandonarse.» — traducción propia.)

Ahora haz la pregunta de 2026: si programar es construir teoría, ¿qué construye una máquina que genera código? Respuesta incómoda y central: **código sin teoría, a escala industrial**. El LLM produce texto competente; la comprensión de por qué ese texto es correcto *aquí*, en *tu* sistema, con *tus* acuerdos de 1974 — esa no viene incluida. Alguien tiene que ponerla. Si nadie la pone, estás fabricando programas muertos de nacimiento: sistemas que se ejecutan sin que ningún humano posea su teoría. Eso era Vega antes del 14 de marzo. La pregunta que Élia escribe en la pared — *¿quién posee la teoría de este sistema?* — es la pregunta de Naur, y es la pregunta que deberías hacerle a cada repositorio del que seas responsable. Si la respuesta es «nadie», no tienes un sistema: tienes un incidente esperando fecha.

## Spolsky: las abstracciones tienen fugas

Segunda pieza del corazón. En 2002, Joel Spolsky formuló en su blog la **ley de las abstracciones con fugas**:

> «All non-trivial abstractions, to some degree, are leaky.»
> («Todas las abstracciones no triviales, en algún grado, tienen fugas.» — traducción propia. Spolsky, *The Law of Leaky Abstractions*, joelonsoftware.com, 2002.)

Una abstracción «tiene fugas» cuando el detalle que prometía ocultarte reaparece y te exige entenderlo: el ORM que te ahorra el SQL hasta que una consulta tarda veinte segundos; el recolector de basura que te ahorra la memoria hasta que las pausas te matan el servicio; la red «transparente» hasta que se parte. Y la conclusión de Spolsky, que es la que nos importa:

> «the abstractions save us time working, but they don't save us time learning.»
> («las abstracciones nos ahorran tiempo de trabajo, pero no nos ahorran tiempo de aprendizaje.» — traducción propia.)

Aplícalo a la abstracción más ambiciosa jamás desplegada sobre este oficio: «describe lo que quieres y la máquina lo programa». Es una abstracción magnífica y profundamente no trivial — luego, por la ley, tiene fugas. ¿Por dónde fuga? Por todas las costuras que ya conoces: cuando el código generado es sutilmente incorrecto y hay que *leerlo de verdad* para verlo; cuando el modelo elige el patrón estadísticamente canónico que tu dominio contradice (el commit UTC *es* una fuga de esta abstracción, de manual); cuando el error está en una capa que el prompt no nombra. En cada fuga, la factura del aprendizaje que la abstracción parecía perdonarte llega entera y con recargo. El junior que nunca aprendió lo que la IA le ahorra no tiene una carrera más ligera: tiene una deuda que vence el peor día posible.

## La valla de Chesterton, versión repositorio

Tercera pieza, la más corta. G. K. Chesterton propuso (en *The Thing*, 1929) un principio para reformadores: si te encuentras una valla en mitad de un camino y no entiendes para qué está, la actitud correcta no es quitarla — es *averiguar por qué la pusieron*, y solo entonces ganarte el derecho a quitarla. En software la **valla de Chesterton** es ese código raro que «claramente sobra»: el `sleep(200)` sin comentario, la condición imposible, las fechas sin zona horaria de Joel. El commit del Autopilot fue un derribo de valla de libro: encontró una rareza, no pudo saber que era un acuerdo de 1974 con forma de rareza, y la «arregló». Y aquí está el matiz que hace 2026 diferente: un humano prudente, ante la valla, *siente* la incertidumbre y pregunta — recuerda a Tomás: «puede que preguntando antes en el canal de Slack, y ahí está toda la diferencia». Un LLM no siente que le falta contexto: **la ausencia de información no le produce duda, le produce fluidez**. Responde igual de seguro sepa o no sepa. Por eso los sistemas con agentes bien diseñados — lo verás en las secciones 5 y 7 — convierten la pregunta en mecanismo: vallas señalizadas en ficheros de contexto («esto no se toca sin leer tal documento»), políticas que exigen justificación, revisión humana donde la teoría es densa. La prudencia, que en humanos es una virtud, en sistemas agénticos tiene que ser una pieza de ingeniería.

## Bainbridge: las ironías de la automatización

Cuarta pieza, y la más profética. En 1983 — cuarenta años antes de Copilot — la psicóloga Lisanne Bainbridge publicó *Ironies of Automation*, un artículo académico breve sobre plantas industriales automatizadas que describe con precisión inquietante el mundo del desarrollo asistido por IA. Primera ironía: automatizar no elimina al humano, lo reubica en lo peor:

> «the designer who tries to eliminate the operator still leaves the operator to do the tasks which the designer cannot think how to automate»
> («el diseñador que intenta eliminar al operario sigue dejándole al operario las tareas que el diseñador no sabe cómo automatizar» — traducción propia. Bainbridge, *Ironies of Automation*, Automatica 19(6), 1983.)

Es decir: la máquina se queda lo fácil y te deja lo difícil. El agente escribe el 80% rutinario; a ti te llega el 20% donde el agente fracasó — que es, por construcción, lo más enrevesado. Segunda ironía: justo cuando más te necesitan, menos en forma estás, porque «las destrezas físicas se deterioran cuando no se usan» y quien supervisa una automatización practica cada vez menos la habilidad que la supervisión exige. Tercera:

> «The human monitor has been given an impossible task.»
> («Al supervisor humano se le ha encomendado una tarea imposible.» — traducción propia.)

Vigilar pasivamente un sistema que casi siempre acierta es psicológicamente insostenible: la atención se degrada, la confianza se instala, y el fallo — infrecuente por diseño — te encuentra dormido. ¿Te suena? Es la descripción exacta de revisar pull requests de un agente que lleva doscientos aciertos seguidos. El «Accept All» de Karpathy no es pereza: es la tercera ironía operando sobre un humano normal. Y la cuarta ironía, la que Bainbridge llamó quizá la definitiva, invierte toda la intuición del ahorro:

> «Perhaps the final irony is that it is the most successful automated systems, with rare need for manual intervention, which may need the greatest investment in human operator training.»
> («Quizá la ironía final sea que son los sistemas automatizados de más éxito, los que rara vez necesitan intervención manual, los que pueden requerir la mayor inversión en formación del operario humano.» — traducción propia.)

Cuanto mejor es tu automatización, *más* — no menos — tienes que invertir en la competencia de los humanos que la rodean. Es el argumento de este curso entero, dicho por una psicóloga industrial en 1983. La industria aeronáutica lo aprendió con sangre y por eso los pilotos de aviones ultraautomatizados pasan por simulador con más frecuencia, no menos. Nuestro gremio lo está aprendiendo ahora mismo.

## La atrofia: qué dice la evidencia de 2025

¿Es real el deterioro, o es nostalgia de veteranos? Hay datos tempranos y apuntan todos en la dirección de Bainbridge. Un estudio de Microsoft Research y Carnegie Mellon presentado en CHI 2025 (319 trabajadores del conocimiento) encontró exactamente la relación que la teoría predice:

> «Higher confidence in GenAI is associated with less critical thinking, while higher self-confidence is associated with more critical thinking.»
> («Una mayor confianza en la IA generativa se asocia con menos pensamiento crítico, mientras que una mayor confianza en uno mismo se asocia con más pensamiento crítico.» — traducción propia. Lee, Sarkar et al., CHI 2025.)

Cuanto más te fías de la herramienta, menos verificas; cuanto más te fías de *ti*, más la corriges. En paralelo, Simkute et al. han trasladado formalmente las ironías de Bainbridge a la IA generativa (*Ironies of Generative AI*, arXiv:2402.11364), y desde la trinchera práctica Addy Osmani (ingeniero de Google, en su ensayo sobre la atrofia de destrezas, 2025) lo resume en forma de coste compuesto: «cada vez que dejamos que la IA resuelva un problema que podríamos haber resuelto nosotros, cambiamos comprensión a largo plazo por productividad a corto plazo» (traducción propia). Ninguno de estos autores concluye «no uses IA» — todos la usan. Concluyen algo más exigente: **el uso que no ejercita la comprensión es un préstamo contra tu competencia futura**, y hay que decidir conscientemente cuándo merece la pena pedirlo.

## Poseer la teoría en 2026: qué significa exactamente

Juntemos las cuatro piezas en una tesis, que es la tesis del curso: como la máquina produce código sin teoría (Naur), como la abstracción que la envuelve fuga (Spolsky), como está estadísticamente sesgada contra tus rarezas legítimas (Chesterton) y como su éxito degrada por defecto la vigilancia humana (Bainbridge) — **entender los sistemas por dentro, y no de oído, vale hoy más que en cualquier momento anterior de la historia del oficio**. No a pesar de la IA: *a causa* de ella. El conocimiento que la máquina no puede tener — la correspondencia entre tu código y tu mundo — es exactamente el que se vuelve escaso, y lo escaso que es imprescindible se vuelve valioso. Parece que cualquiera puede hacer software ahora. En un mundo inundado de software que se escribe solo, la diferencia entre quien puede responder de un sistema y quien solo puede generarlo se convierte en *la* diferencia profesional.

Poseer la teoría de un sistema, en términos operativos — y esto vale para código tuyo, heredado o generado esta mañana —, es poder hacer estas cuatro cosas: **explicar** cualquier parte y su porqué a un compañero (o a Paca) sin leer el código en voz alta; **predecir** qué efectos tendrá un cambio antes de ejecutarlo; **justificar** cada rareza — cada valla — o saber señalar exactamente qué no sabes; y **modificar** el sistema de forma que el cambio parezca crecido desde dentro, no atornillado desde fuera. Contra ese estándar tienes que medir tu relación con el código que tus agentes escriban: no «¿funciona?», sino «¿podría yo firmarlo?» — palabra que, como verás en la sección 9, acabará siendo literal. Y una advertencia final de honestidad intelectual: reconstruir teoría cuesta lo que cuesta — al equipo de Vega le costó semanas de mapa, arqueología y visitas a una mesa camilla. La sección que viene no va de evitar ese coste: va de cómo los agentes, bien sujetos, pueden por fin ayudarte a pagarlo.

## Para llevar

- Programar es construir una teoría: la comprensión viva de cómo el código se corresponde con el mundo y por qué. El código es el producto; la teoría es el activo (Naur, 1985).
- Un programa muere cuando nadie posee su teoría, aunque siga ejecutándose; y la teoría no se resucita desde la documentación: se reconstruye trabajando. La pregunta «¿quién posee la teoría de este sistema?» separa los sistemas vivos de los incidentes con fecha pendiente.
- Los LLM generan código sin teoría a escala industrial. La teoría hay que ponerla: ese es el trabajo que no se puede delegar, y su precio está subiendo.
- Las abstracciones ahorran trabajo, no aprendizaje (Spolsky); las vallas raras del código suelen ser acuerdos del mundo con forma de rareza (Chesterton), y un LLM no siente la duda que salvaría la valla — la prudencia hay que dársela por ingeniería.
- Bainbridge (1983): la automatización te deja lo difícil, atrofia lo que no ejercitas, convierte la supervisión en tarea imposible — y cuanto mejor funciona, más formación humana exige. La evidencia de 2025 (CHI, Microsoft/CMU) confirma la dirección.
- Criterio operativo de posesión de teoría: explicar, predecir, justificar, modificar. Aplícaselo a todo código del que respondas, lo haya escrito quien lo haya escrito.

## Para profundizar

- P. Naur, *Programming as Theory Building* (1985) — circula libre en la web (el escaneo de la Universidad de Wisconsin es el habitual); veinte páginas que reordenan el oficio. La lectura más importante de este curso.
- L. Bainbridge, *Ironies of Automation* (Automatica, 1983) — PDF libre; corto, seco y profético.
- J. Spolsky, *The Law of Leaky Abstractions* (joelonsoftware.com, 2002) — quince minutos, vigencia indefinida.
- Lee, Sarkar et al., *The Impact of Generative AI on Critical Thinking* (CHI 2025, Microsoft Research/CMU) — el estudio de la confianza y el pensamiento crítico.
- Simkute et al., *Ironies of Generative AI* (arXiv:2402.11364) — Bainbridge formalmente trasladada a nuestra década.
- A. Osmani, *Avoiding Skill Atrophy in the Age of AI* (addyosmani.com/Substack, 2025) — la versión práctica, con tácticas concretas para no oxidarse.
