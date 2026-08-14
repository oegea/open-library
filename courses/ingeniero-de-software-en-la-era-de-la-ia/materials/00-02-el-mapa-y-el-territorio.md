Antes de entrar en materia, el mapa. Este capítulo te cuenta cómo está construido el curso por dentro —sus tres eras, sus diez secciones, su tesis— para que en todo momento sepas dónde estás y por qué. Léelo ahora en cinco minutos y vuelve a él cuando quieras orientarte: para eso están los mapas.

## Las tres eras

La historia que este curso cuenta —la grande, no la de Vega Riegos— se deja resumir en tres eras, definidas por la pregunta de *a quién le hablamos cuando programamos*:

**Programar la máquina.** Desde las tarjetas perforadas hasta ayer por la tarde: el humano piensa la solución y la traduce, con ayuda de capas crecientes de abstracción —ensambladores, compiladores, lenguajes de alto nivel, frameworks—, a instrucciones que una máquina ejecuta. Setenta años de esta era nos dieron el oficio entero: los principios, las cicatrices y una constante histórica que verás en la primera sección — cada nueva capa llegó acompañada del anuncio de que los programadores ya no haríamos falta.

**Programar con la máquina.** La era que se abrió cuando los modelos de lenguaje aprendieron a escribir código: el autocompletado que sugiere, el chat que explica y bosqueja, el par que nunca se cansa. El humano sigue dirigiendo cada paso, pero ya no teclea solo. Aquí es donde la mayoría de la profesión vive hoy.

**Programar a la máquina que programa.** La era que está empezando: agentes que persiguen objetivos usando herramientas —leen tu repositorio, editan, ejecutan tests, abren pull requests— y humanos cuyo trabajo se desplaza a decidir qué se construye, darles contexto y límites, verificar lo que producen y responder del resultado. No es ciencia ficción: es el commit nocturno que precede a la madrugada del 14 de marzo, con el que arranca nuestra historia. Esta era no elimina las dos anteriores — se apoya en ellas, y castiga con dureza a quien pretenda saltárselas.

La tesis del curso, que irás viendo argumentada pieza a pieza, es que el tránsito entre eras repite un patrón: **la automatización sube el nivel de abstracción y desplaza el criterio humano — no lo elimina.** Y que, en consecuencia, entender los sistemas por dentro, poseer su teoría y poder responder de ellos vale hoy más que nunca, no menos.

## El itinerario, sección a sección

- **S1 — El oficio que siempre estuvo muriéndose.** Setenta años de «fin del programador»: compiladores, 4GL, CASE, no-code. La vacuna histórica contra el pánico y contra la negación.
- **S2 — De autocompletar a agentes.** Qué es de verdad un modelo de lenguaje —tokens, contexto, muestreo, no determinismo— y qué dice la evidencia seria, no el marketing, sobre lo que estas herramientas aceleran y lo que no.
- **S3 — La teoría está en tu cabeza.** El corazón del curso: programar es construir una teoría (Naur), las abstracciones tienen fugas, la automatización tiene ironías (Bainbridge), y por qué comprender vale más que nunca.
- **S4 — Anatomía de un agente.** Se acabó la niebla: escribimos un agente funcional en unas decenas de líneas, en Python y JavaScript. Aquí arranca la parte práctica fuerte, que ya no se detiene.
- **S5 — El arnés.** Harness engineering: la jaula, los permisos, AGENTS.md, los feedback loops. Todo lo que rodea al modelo — y que, a diferencia del modelo, se posee.
- **S6 — Specs, versiones y evals.** Los principios atemporales aplicados a las piezas que no parecen software: el prompt como artefacto versionado, y cómo se prueba lo que nunca responde dos veces igual.
- **S7 — Diseñar para humanos es diseñar para agentes.** El flujo de trabajo completo: explorar, planificar, ejecutar, revisar; multiagente, loop engineering, ADRs, y los acuerdos de equipo como código.
- **S8 — Soberanía.** Ser dueños del flujo: lock-in, coste de salida, qué poseer y qué alquilar, estándares abiertos, y el criterio que lo resume todo: desconfía del acoplamiento que no puedes inspeccionar.
- **S9 — Quien firma, responde.** La sección grave: Therac-25, prompt injection y la trifecta letal, la cadena de suministro, el estado legal del código generado, y la ética del oficio.
- **S10 — El futuro imaginado.** Extrapolación honesta y optimista —flotas, ingeniería de sistemas de agentes, el ingeniero de producto—, con cada frontera entre hecho e imaginación marcada. Y el material para seguir formándote cuando esto acabe.

Detrás del orden hay un arco deliberado: primero entender (S1–S3: de dónde venimos, qué es esta tecnología, qué no se puede delegar), luego construir (S4–S7: el agente, el arnés, las evals, el flujo), y por último ser dueños y responsables (S8–S10: soberanía, responsabilidad, futuro). Comprender, construir, responder. Si en mitad del curso te preguntas por qué estás leyendo algo, la respuesta estará en esa progresión.

## Las reglas de la casa

Tres compromisos que este curso mantiene contigo de principio a fin, y que te invitamos a auditar:

1. **Los datos llevan fuente.** Cuando leas un porcentaje, un año o una cita, sabrás de dónde sale. Si alguna vez decimos «se suele afirmar» es porque no pudimos verificarlo, y lo sabrás.
2. **Lo especulativo va marcado.** La mayor parte del curso describe el presente y el pasado verificables. Cuando extrapolamos —sobre todo en la sección 10— lo decimos explícitamente, cada vez. Distinguir hecho de conjetura es una destreza profesional, y un curso que la exige debe practicarla.
3. **Lo práctico es real.** Los ficheros de ejemplo son completos, los comandos existen, el código se ejecuta. Nada de pseudocódigo decorativo ni recetas de humo.

## Cómo sacarle el máximo partido

**Lee en orden**, al menos la primera vez: la historia es continua y la teoría se apoya en lo anterior. **Teclea lo que se pueda teclear** — el agente de la sección 4, el AGENTS.md de la 5, la mini-suite de evals de la 6: una hora de manos enseña más que tres de lectura. Y una recomendación que en la historia encontrarás convertida en personaje: lleva un **cuaderno de asombros** — un sitio, papel o fichero, donde apuntes con fecha cada cosa que no entiendas del todo, para volver a por ella. La premisa entera de este curso es que la diferencia profesional de esta época está entre quienes se perdonan no entender lo que usan y quienes van a mirar dentro. El cuaderno es la herramienta más barata que existe para estar en el segundo grupo.

Y ahora sí. Marzo. Una acequia centenaria con válvulas motorizadas. Un test que falla una de cada quince veces. Y una máquina paciente, competente y completamente ignorante de un acuerdo firmado en 1974, a punto de hacer exactamente lo que le enseñaron.
