Bienvenida, bienvenido. Este curso trata sobre ti: sobre qué significa ser ingeniero o ingeniera de software en la era en que las máquinas escriben código. No es un tutorial de una herramienta —aunque saldrás sabiendo usar varias en serio— ni un sermón sobre el futuro —aunque nos atreveremos a imaginarlo, avisando siempre de que imaginamos—. Es un intento de responder, con rigor y sin pánico, a las preguntas que este oficio se está haciendo ahora mismo: qué cambia de verdad, qué permanece, qué principios de siempre valen más que nunca, y cómo se monta, con las manos, un flujo de desarrollo con agentes del que puedas estar orgulloso — y del que puedas responder.

Si eres junior y las palabras «agente», «harness engineering» o «evals» te suenan a niebla, estás en el punto de partida exacto para el que se diseñó el curso: todo término se define la primera vez que aparece, en negrita, con una definición sencilla y su matiz. Si llevas años en esto y usas asistentes de IA a diario, también hay sitio para ti, y no de cortesía: hemos procurado que cada sección tenga al menos un «esto no lo sabía» — el origen exacto de un término que todo el mundo usa mal, un dato de un estudio serio que contradice el ruido, un patrón que todavía no habías sistematizado.

## Qué vas a encontrar en cada sección

El curso avanza por secciones temáticas con un ritmo fijo, pensado para que la teoría nunca llegue antes que la necesidad:

1. **Una historia.** El curso narra, capítulo a capítulo, una única historia de ficción: la de **Vega Riegos**, una empresa de nueve personas cuyo software gobierna el riego de comunidades de regantes reales — válvulas, acequias, agua que no vuelve —, y que una madrugada de marzo descubre en su repositorio un commit que ningún humano escribió. Cada episodio te pone delante de un problema antes de darle nombre; la historia continúa de sección en sección, los personajes crecen, y te recomendamos leerla en orden, como la novela por entregas que es. Todo lo técnico que ocurre en ella —los tests intermitentes, los merges automáticos, los ataques, las migraciones— es real: son las cosas que pasan, y que te pasarán.
2. **La teoría.** Tras cada episodio, un capítulo explica con rigor lo que la historia mostró: definiciones precisas, datos con número y fuente —nunca «dicen que»—, ejemplos de código en **JavaScript** y **Python** cuando aportan, y citas textuales con autor y obra. Cada teoría cierra con «Para llevar» y «Para profundizar».
3. **Una ampliación**, solo en las secciones donde de verdad aporta: el nivel extra de detalle práctico, los matices, los rincones donde más aprenden quienes ya conocían el tema.
4. **Un examen.** Tipo test, con una particularidad heredada de la filosofía de esta plataforma: lo importante no es la nota sino la **explicación** de cada respuesta. Úsalos como herramienta de aprendizaje, no como juicio.

Una advertencia de método que es también una promesa: este curso no se queda en el plano teórico. Cuando termines, habrás escrito un agente funcional con tus manos, sabrás construir su arnés —permisos, sandbox, contexto, verificación—, tendrás plantillas reales de AGENTS.md y de suites de evaluación, y podrás irte a tu Claude Code, tu Codex o tu OpenCode y montar un flujo de desarrollo avanzado de verdad, con multiagente, revisión cruzada y políticas de equipo escritas como código. Esa exigencia práctica fue condición de nacimiento del curso, y la vas a notar.

## Hecho con inteligencia artificial, y dicho claramente

Este curso ha sido redactado con ayuda de inteligencia artificial, bajo dirección y revisión humanas, y está marcado como tal en la plataforma. En un curso cualquiera, esta transparencia sería una cortesía; en *este* curso es casi un examen de coherencia: vas a pasarte diez secciones leyendo que la época exige responsabilizarse de lo que las máquinas ayudan a producir, verificar las fuentes y decir la verdad sobre el proceso. Empezamos aplicándonoslo.

Vivimos un momento extraño y fascinante: **crear nunca ha sido tan fácil, y precisamente por eso la responsabilidad de crear bien nunca ha sido tan grande.** Cuando producir mil páginas cuesta una tarde, la tentación es inundar el mundo de páginas que nadie ha pensado de verdad. Este curso intenta ser lo contrario. Cada fuente citada existe y ha sido consultada; cada cita textual indica autor, obra y origen, y cuando la traducción es nuestra, se dice; cuando un dato no pudo verificarse en su fuente primaria, se presenta con esa cautela o no se presenta; y lo especulativo —hay una sección entera dedicada al futuro— va marcado como especulación, sin excepciones. Las ideas de Peter Naur, Lisanne Bainbridge, Fred Brooks, Grace Hopper, Edsger Dijkstra, Nancy Leveson, Simon Willison y tantos otros se presentan como suyas, con nombre y obra, no como si fueran nuestras. La IA se ha usado como lo que es: una herramienta extraordinaria para investigar, ordenar y redactar — no para suplantar a quienes descubrieron estas ideas, ni para ahorrarnos el deber de verificar.

Si encuentras un error, será nuestro, no de las fuentes. Y agradeceremos que nos lo digas.

## Créditos y agradecimientos

Este curso se apoya, con gratitud, en material abierto o de libre acceso legítimo. Las fuentes principales:

- El **informe de la OTAN de 1968** sobre ingeniería del software (eds. Naur y Randell), preservado en abierto por Brian Randell, y el archivo **EWD de Dijkstra** (Universidad de Texas).
- **Peter Naur**, *Programming as Theory Building* (1985), y **Lisanne Bainbridge**, *Ironies of Automation* (1983) — los dos textos que sostienen el corazón del curso.
- **Nancy Leveson y Clark Turner**, por la investigación del Therac-25 (1993), memoria imprescindible del oficio.
- **Simon Willison** (simonwillison.net), cuyo registro público de esta era —del nombre «prompt injection» a la «trifecta letal»— es un servicio a la profesión.
- Las guías de ingeniería abiertas de **Anthropic** (agentes, contexto, arneses) y la documentación de **Claude Code**, junto con los estándares abiertos **MCP** y **AGENTS.md**.
- Los estudios de **METR**, los informes **DORA**, la encuesta de **Stack Overflow** y el proyecto **OWASP GenAI** (CC BY-SA) — los datos serios detrás de las afirmaciones.
- **Joel Spolsky**, **Martin Fowler** y su bliki, **Michael Nygard** (ADRs), **Hamel Husain** (evals), **Mitchell Hashimoto**, **Addy Osmani**, **Birgitta Böckeler**, **Dex Horthy** (12-Factor Agents, CC BY-SA) y **Andrej Karpathy**, por divulgar en abierto.
- El **Código Ético de la ACM**, que se puede reproducir sin cambios, y que deberías leer aunque abandones este curso en el capítulo dos.

La bibliografía completa, con enlaces y licencias, te espera en el capítulo de cierre.

## Un regalo

Este curso es gratuito y quiere ser, sencillamente, un regalo: de los que lo hicieron a quien lo recibe, y de la comunidad que construyó estas ideas —durante setenta años, a base de aciertos, incendios y papers— a la generación que las va a necesitar. No te pedimos nada a cambio, pero si quieres pagar algo, paga esto: entiende lo que uses, responde de lo que firmes, y cuando sepas algo que otro necesita, regálalo también.

Empezamos. Es de madrugada en una comunidad de regantes del sureste. Ocho válvulas motorizadas acaban de girar sobre sus ejes sin que nadie se lo pida, el agua de todos corre hacia parcelas que no la esperaban, y en el repositorio de una pequeña empresa hay un commit reciente, pulcro, con todos los checks en verde, que ningún ser humano ha escrito. Que ningún ser humano ha *leído*.

Todavía no lo saben, pero esa es la parte importante.
