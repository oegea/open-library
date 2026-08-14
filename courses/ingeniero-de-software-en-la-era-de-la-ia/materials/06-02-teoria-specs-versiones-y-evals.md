Dos semanas de partes incompletos, y ningún sistema lo detectó: lo detectó Andrés el de los caquis. La avería del capítulo no fue de código — fue de categoría: el equipo trataba como «una redacción» lo que era una pieza operativa. Esta teoría desarrolla la lección en tres capas: el prompt como artefacto de ingeniería, las specs como contrato, y las evals — cómo se prueba con rigor un componente que nunca responde dos veces igual. Es, de todo el curso, la sección donde los principios atemporales aplican con menos traducción: versionar, revisar, probar. Solo cambia a qué.

## El prompt es una pieza, y las piezas se versionan

Empecemos por el diagnóstico de Tomás, que cabe en una lista: el prompt del parte diario era una pieza operativa crítica **sin control de versiones, sin revisión, sin pruebas y sin vuelta atrás**. Cada una de esas cuatro carencias tiene ochenta años de solución conocida; ninguna se estaba aplicando, porque la pieza «no parecía software». Definamos entonces qué es un **prompt operativo**: texto que se ejecuta en producción, cuya salida consumen usuarios o sistemas, y cuya modificación cambia el comportamiento del producto. Con esa definición delante, la conclusión es inmediata y no admite mucha discusión:

- **Se versiona en git**, junto al código que lo usa — no en un Google Doc, no en un panel de un proveedor (rima con la sección 8: los prompts son de las piezas que se *poseen*). Historial, diff, blame, revert: todo lo que Bruno no tenía el día que escribió encima de la versión buena.
- **Se revisa por pull request**, como cualquier cambio de producción. La revisión de un prompt es distinta a la de código — se revisa la intención, la ambigüedad, los casos límite del lenguaje — pero el mecanismo es el mismo, y con él viene lo que de verdad faltó aquel jueves: un segundo par de ojos y un momento explícito de «esto va a producción».
- **Se prueba** — y aquí está la novedad genuina, porque probar una pieza no determinista exige técnica propia. A eso vamos, porque es el corazón de la sección. Pero antes, una parada en el territorio vecino.

## Spec-driven development: el contrato antes que el código

Si el prompt merece disciplina de artefacto, el paso siguiente es preguntarse por el artefacto anterior al prompt: la **especificación**. En 2025 cristalizó un movimiento — **spec-driven development** (SDD, desarrollo dirigido por especificaciones) — que propone invertir el flujo habitual con agentes: en lugar de pedirle código a la máquina y refinar a base de conversación, se escribe primero una spec estructurada y el agente deriva de ella el plan y el código. La herramienta emblema es **Spec Kit** (GitHub, código abierto, MIT), cuyo anuncio lo formula así, traducción propia: «empiezas con una spec. Es un contrato sobre cómo debe comportarse tu código, y se convierte en la fuente de verdad»; su flujo son comandos que encadenan artefactos — `/speckit.constitution` (los principios del proyecto), `/speckit.specify` (el qué y el porqué), `/speckit.plan` (el cómo técnico), `/speckit.tasks` (el troceo) y `/speckit.implement` (la ejecución). **Kiro**, el entorno de AWS, empaqueta la misma idea en tres ficheros por funcionalidad: `requirements.md`, `design.md`, `tasks.md`.

Te debemos el debate honesto, porque lo hay. La crítica más citada es la de Colin Eberhardt (Scott Logic, 2025), que tras usar SDD a fondo concluyó, traducción propia: «al final, mucho tiempo dedicado a revisar markdown… no vi ningún beneficio cualitativo que justificara la sobrecarga» — en su experimento, miles de líneas de markdown para unos cientos de líneas de código que aun así llegaron con un bug simple y evidente; su etiqueta, «waterfall reinventado», duele porque señala un riesgo real: burocratizar la conversación con la máquina y redescubrir que las specs exhaustivas por adelantado fallan por las mismas razones por las que fallaron en los años noventa — el entendimiento llega *haciendo*. La síntesis sensata, y la que este curso suscribe, es que la spec vale exactamente lo que valga el contexto que el agente no podría deducir: para una tarea de una tarde, una spec de tres páginas es teatro; para el proyecto grande que verás en la próxima sección — cuarenta páginas de pliego oficial, criterios verificables, varias semanas y varios agentes en paralelo — el análisis y el plan escritos serán precisamente lo que permita volar. No es una metodología nueva: es la vieja pregunta de cuánta especificación merece cada tarea, con un lector nuevo que hace caso de lo que pone.

## Evals: tests de regresión para lo no determinista

Y llegamos al corazón. El problema técnico del parte de las siete era genuinamente nuevo para el equipo: ¿cómo pruebas un componente cuya salida es distinta cada vez? La respuesta de Nadia en la pizarra — no compruebas *la* salida, compruebas *propiedades* de la salida, muchas veces — define exactamente lo que el sector llama **evals** (evaluaciones): tests de regresión para sistemas no deterministas, donde el veredicto no es «la salida es igual a X» sino «la salida cumple las propiedades P, en N ejecuciones, sobre M escenarios».

Conviene decir en voz alta que esto **no** es una técnica exótica nacida con los LLM: es la tradición estadística y por propiedades del testing de toda la vida, aplicada a una pieza nueva. La pirámide de tests (Mike Cohn, popularizada por Martin Fowler y Ham Vocke en martinfowler.com) nos enseñó a poner muchos tests baratos abajo y pocos caros arriba; el **property-based testing** (QuickCheck, Claessen y Hughes, 2000) nos enseñó a comprobar propiedades sobre entradas generadas en vez de casos fijos; el **mutation testing** (idea de los años setenta; hoy PIT, Stryker) nos enseñó a medir si nuestros tests detectan de verdad los fallos sembrando fallos a propósito. Si has usado Hypothesis en Python o fast-check en JavaScript, ya has escrito tests que no comprueban una salida exacta:

```python
from hypothesis import given, strategies as st

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_caudal_medio_esta_entre_min_y_max(lecturas):
    if lecturas:
        m = caudal_medio(lecturas)
        assert min(lecturas) <= m <= max(lecturas)   # propiedad, no valor exacto
```

Una eval de LLM es este mismo gesto mental con dos vueltas de tuerca: las entradas no se generan al azar sino que se **curan** (escenarios reales, cuanto más incómodos mejor), y como el no determinismo está en el componente y no en la entrada, cada escenario se ejecuta varias veces y se mira la tasa de cumplimiento. La suite de Bruno y Nadia, en pseudoestructura:

```python
# evals/parte_diario/escenarios/noche_ramal_norte.yaml
telemetria: capturas/2026-06-30.json       # una noche real, con la avería aburrida
reglas:
  - toda incidencia de presión registrada se menciona        # determinista
  - los datos marcados como dudosos se describen como dudosos # determinista
  - no se promete ninguna acción sin ticket asociado          # determinista
  - longitud <= 900 caracteres                                # determinista
  - tono claro y sin alarmismo                                # juez LLM, rúbrica v3
ejecuciones: 5
umbral: 5/5 en reglas deterministas, 4/5 en tono
```

Cuarenta y dos escenarios así, ejecutados por el CI en cada cambio del prompt (o del modelo — apúntalo: cambiar de modelo también es un despliegue), convierten «me pareció más limpio» en un check verde o rojo. Las **reglas deterministas** — se menciona X, no se promete Y, longitud, formato — son código normal (regex, parsers, asserts) y deben ser la mayoría: baratas, rápidas, sin ambigüedad. Para lo que las reglas no saben medir — claridad, tono — se usa el **LLM-as-judge** (modelo como juez): otra llamada a un modelo con una rúbrica que puntúa la salida. Funciona, y hay que usarlo con los ojos abiertos, porque la investigación le tiene tomadas las medidas: Zheng et al. (NeurIPS 2023), el estudio canónico, documenta sus sesgos — de posición (prefiere la primera opción que lee), de verbosidad (prefiere respuestas largas), de auto-mejora (prefiere salidas de su propia familia de modelos) — y Shankar et al. (*Who Validates the Validators?*, 2024) añade dos avisos finos: los criterios humanos derivan («criteria drift»: al ver más salidas, cambias de opinión sobre qué era «bueno»), y — traducción propia — «los evaluadores generados por LLM simplemente heredan todos los problemas de los LLM que evalúan». Reglas prácticas que se derivan: el juez puntúa con rúbrica escrita y versionada (la de Vega iba en git, como todo), se calibra contra juicios humanos de vez en cuando, y jamás es la única línea de defensa — lo crítico va en reglas deterministas.

En cuanto a herramientas: **promptfoo** (open source, MIT — hoy mantenido bajo el paraguas de OpenAI, sigue siendo MIT) es el estándar de facto para montar exactamente la suite descrita con un YAML declarativo, y **openai/evals** (MIT) es el framework histórico de referencia. Pero la herramienta es lo de menos: una suite de evals es un bucle, unos asserts y un YAML de escenarios — sesenta líneas de tu lenguaje favorito, como el agente de la sección 4. Lo difícil, como siempre en testing, es curar los escenarios y definir las propiedades. Hamel Husain, en el ensayo de referencia sobre el tema (*Your AI Product Needs Evals*, 2024), señala tras auditar decenas de productos que los que fracasan «casi siempre comparten una causa raíz: no haber construido un sistema robusto de evaluación» — y añade el consejo operativo más subestimado del campo: elimina toda fricción para *mirar los datos*, porque los escenarios buenos salen de las salidas reales que alguien se molestó en leer.

## Qué merece evals — y qué no

Y ahora, el aviso contra el péndulo, porque esta sección podría dejarte con ganas de evaluar hasta el saludo. No. La inversión en evals sigue la misma economía que la inversión en tests, y la pregunta es idéntica: **¿cuál es el coste de una regresión no detectada, y cuántas veces se modifica la pieza?** El parte de las siete puntúa alto en ambas — salida diaria a ochocientos regantes, prompt que se retoca a menudo — y por eso merece sus cuarenta y dos escenarios. En cambio, el fichero de contexto de tu agente de desarrollo — tu AGENTS.md o CLAUDE.md — normalmente **no** merece una suite de evals: su «regresión» la detectas tú mismo a los diez minutos de trabajar con el agente, el coste de un fallo es una molestia local y reversible, y montarle un arnés de prompt-testing sería el equivalente exacto de escribir tests unitarios para tu `.bashrc` — posible, y probablemente una pérdida de tiempo con esteroides. Entre ambos extremos, gradúa: un prompt interno que usa tu equipo cada día merece quizá cinco escenarios de humo; el que decide qué información recibe un cliente merece la suite entera. El criterio de siempre — probar en proporción al riesgo — no ha cambiado; solo ha cambiado la lista de piezas a las que aplicarlo. Y esa es, en el fondo, la lección completa del capítulo: la época no exige inventar principios nuevos, exige no dejar de aplicar los viejos a las piezas que no lo parecen.

## Para llevar

- Un prompt en producción es una pieza operativa: git, pull request, pruebas y vuelta atrás. «No parece código» es exactamente como se cuelan las regresiones de dos semanas.
- Cambiar un prompt — o el modelo de debajo — es un despliegue, y se trata como tal.
- Spec-driven development: la spec vale lo que valga el contexto que el agente no puede deducir. Útil en proyectos grandes y verificables; teatro burocrático en tareas de una tarde (el debate Eberhardt es lectura honesta).
- Evals = tests de regresión de lo no determinista: escenarios reales curados × propiedades verificables × N ejecuciones. Mayoría de reglas deterministas; LLM-as-judge solo para lo que las reglas no alcanzan, con rúbrica versionada y conociendo sus sesgos (posición, verbosidad, auto-preferencia).
- Es la tradición de siempre con pieza nueva: pirámide de tests, property-based (Hypothesis, fast-check), mutation testing. Si sabes probar lo estadístico, sabes evaluar LLMs.
- Invierte en evals en proporción al riesgo: el parte de las siete, sí; prompt-testear tu CLAUDE.md, no.

## Para profundizar

- H. Husain, *Your AI Product Needs Evals* (hamel.dev, 2024) — el ensayo de referencia; práctico, con niveles (asserts / evaluación humana y de modelo / A-B).
- Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* (NeurIPS 2023) — los sesgos del juez, medidos.
- Shankar et al., *Who Validates the Validators?* (2024) — criteria drift y los límites de la evaluación asistida.
- GitHub Spec Kit (github.com/github/spec-kit, MIT) y la crítica de C. Eberhardt en el blog de Scott Logic (2025) — las dos caras del SDD, léelas juntas.
- promptfoo (promptfoo.dev, MIT) — para montar tu primera suite esta misma tarde.
- Hypothesis (Python) y fast-check (JavaScript) — property-based testing; el músculo mental que las evals reutilizan.
- Y para escribir mejor la pieza que estás versionando y probando: la guía de prompt engineering de la documentación de Anthropic (platform.claude.com) y su tutorial interactivo abierto (github.com/anthropics/prompt-eng-interactive-tutorial), la *Prompt Engineering Guide* de DAIR.AI (promptingguide.ai, open source — con sección de prompting adversarial incluida), y el repaso con base investigadora de Lilian Weng, *Prompt Engineering* (lilianweng.github.io, 2023). Un prompt bien construido necesita menos evals que lo salven.
- Ejercicio: elige el prompt más crítico que tengas en producción (si no tienes, el resumen automático que estés a punto de montar). Escribe cinco escenarios y tres reglas deterministas. Córrelo diez veces. Lo que descubras en la ejecución 7 es la razón de esta sección.
