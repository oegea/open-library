La teoría de esta sección miró hacia delante; esta ampliación hace lo contrario: consolidar. A lo largo del curso, el flujo de desarrollo agéntico se ha ido montando pieza a pieza, cada una en su sección y con su porqué. Aquí está entero, en una sola página: el manual de campo de cómo queda, **a día de hoy**, un flujo de este tipo hecho con criterio. Dos avisos. Primero: esto es una foto del presente, y el presente de esta disciplina se mueve — los detalles caducarán; los principios que los sostienen (el reparto determinista, la teoría poseída, la verificación, la posesión de las piezas) son la parte que no. Segundo: es un máximo, no un mínimo — adopta cada pieza cuando su problema aparezca, no antes. La regla de la solución más simple posible aplica también al propio flujo.

## El suelo: una vez por repositorio

Lo que se monta una vez y trabaja siempre:

1. **El contexto** — un `AGENTS.md` corto y denso: comandos literales, convenciones que el código no evidencia, vallas de Chesterton señalizadas con su porqué y su enlace, límites. `CLAUDE.md` = `@AGENTS.md`. Los acuerdos de más altura (cómo se hace DDD aquí, qué frontera es sagrada) en el mismo sistema: reglas en AGENTS.md o skills, porqués en ADRs. *(Secciones 5 y 7.)*
2. **El reparto determinista** — todo lo que una regla fija pueda comprobar, a mecanismos que corren siempre y para todos, humanos incluidos: la suite en pre-commit o CI, el linter y los tipos como bloqueo, escáner de secretos, auditoría de dependencias, análisis estático. Nada de eso se le pide al agente por prompt: se le impone por infraestructura — y su salida, cuando detecta algo, entra como contexto para que el agente lo repare. *(Sección 5.)*
3. **Permisos y jaula** — la política en humano primero («leer casi todo, proponer todo, ejecutar lo listado, mergear jamás»), traducida a la configuración de tu herramienta; sandbox o contenedor para lo arriesgado, sin credenciales al alcance y con la red en lista blanca — un vértice de la trifecta negado estructuralmente, mínimo. *(Secciones 5 y 9.)*
4. **Sentidos rápidos y honestos** — una suite rápida (decenas de segundos) para el bucle, la completa para el CI, y cero tests flaky: un sentido que miente es un incidente en incubación. *(Sección 5.)*
5. **El equipo empaquetado** — los prompts buenos como comandos slash versionados; el saber-hacer modular como skills; un subagente revisor con mandato adversarial y las reglas de la casa cargadas. *(Sección 7.)*

Si solo puedes hacer una cosa esta semana: el AGENTS.md y la caza de flakys. Es el 20% que rinde el 80%.

## El ciclo: cada tarea

**Explorar** — el agente lee y produce análisis; tú lo corriges con la teoría que solo tú tienes. **Planificar** — tareas de una tarde, cada una con criterio de «hecho» *ejecutable*; cuando la naturaleza de la tarea lo permita, los tests primero: un objetivo verificable convierte al agente de generador de plausibilidades en optimizador contra una función objetivo. **Ejecutar** — contexto deliberado: `/clear` entre tareas ajenas, `/compact` en los valles de las largas; worktrees si hay piezas independientes en paralelo. **Revisar** — en tres anillos: el determinista ya corrió solo (linter, tests, escáneres — bloquean); el semántico lo hace el revisor con juicio — conformidad con la spec, el AGENTS.md y los ADRs — e informa, no decide; y el último eres tú, leyéndolo todo, porque no se committea lo que no se sabría explicar. *(Secciones 3 y 7.)*

## Escalar: cuándo salir del ciclo simple

- **Multiagente** cuando concurran independencia real de las piezas, protección del contexto (tareas de mucha lectura) o necesidad de juicio independiente (revisión). Nunca porque sí: delegar tiene sobrecoste de briefing y consolidación, y el trabajo pequeño o secuencial lo gana un solo agente bien llevado. *(Sección 7.)*
- **Loop engineering** cuando el trabajo exceda una sesión *y* se descomponga en unidades verificables: inicializador + turnos amnésicos, `features.json` con criterios ejecutables, notas entre turnos, git como memoria y checkpoint, y el bucle exterior como script determinista tuyo. *(Sección 7, ampliación.)*
- **Evals** cuando un prompt sea pieza operativa de producción: escenarios reales curados × propiedades × N ejecuciones, en CI, disparadas por cambios de prompt *y* de modelo. En proporción al riesgo — y recuerda qué no las merece. *(Sección 6.)*

## Las esclusas: lo que no se delega hoy

Merge a la rama principal y despliegues (el botón no existe en el mundo del agente); decisiones de alcance y de arquitectura (se deciden con ADR, no se descubren en un diff); la interpretación del dominio — lo que Paca sabe —; y la firma, en todas sus formas: nadie responde de lo que no comprende, y la máquina no responde de nada. La autonomía es un dial por tarea — riesgo × verificabilidad —, no una ideología. *(Secciones 9 y 10.)*

## Afinado fino, hoy por hoy

Recomendaciones de práctica actual, con su fecha de caducidad asumida: no todos los pasos necesitan el mismo modelo — el criterio general es reservar el más capaz para planificar y revisar, y usar el rápido y barato para lo mecánico y de gran volumen, con tus evals como árbitro de qué se degrada; ponles topes a los bucles (vueltas, presupuesto) para que el fallo sea «paró y contó» y no «pensó toda la noche»; registra lo que tus agentes hacen (un JSONL barato hoy vale una cronología el día del incidente); prefiere sesiones y PRs pequeños — una idea por PR también es cortesía con tu revisor de silicio —; y revisa el flujo mismo en las retros: qué se sobre-delegó, qué faltó de contexto, qué barrera faltaba. El flujo es una pieza más de la casa, y se mantiene como todas.

## Para llevar

- Suelo (una vez): contexto versionado, reparto determinista, permisos y jaula, sentidos honestos, equipo empaquetado. Ciclo (siempre): explorar → planificar con «hecho» ejecutable → ejecutar con contexto deliberado → revisar en tres anillos.
- Escala solo cuando el problema lo pida: multiagente por independencia/contexto/juicio; loop engineering cuando no quepa en una sesión; evals cuando el prompt sea producción.
- Las esclusas humanas no son nostalgia: merge, alcance, dominio y firma se quedan del lado de quien responde.
- Esta página caduca; sus principios no. Cuando una herramienta nueva te deslumbre, tráela aquí y pregúntale: ¿qué me hace poseer, qué me hace entender, qué me deja verificar? Las respuestas te dirán si es progreso o solo brillo.
