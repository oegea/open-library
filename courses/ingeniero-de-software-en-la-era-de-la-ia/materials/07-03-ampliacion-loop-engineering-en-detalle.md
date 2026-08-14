La teoría presentó el loop engineering en un párrafo; esta ampliación lo baja al nivel de ficheros y turnos, porque es la técnica de 2026 con mejor ratio entre lo potente que es y lo poco que se conoce bien. El escenario: un proyecto que excede cualquier sesión — días de trabajo, decenas de features — y la restricción de fondo que ya conoces: cada sesión de agente despierta amnésica. Las guías de Anthropic sobre arneses de larga duración, de donde sale este patrón, lo comparan con «ingenieros trabajando por turnos»: el problema a resolver no es la inteligencia de cada turno, sino la **transferencia entre turnos**. Todo lo que sigue es ingeniería de esa transferencia.

## Las piezas sobre el terreno

**El fichero de features** es el corazón del patrón: la lista completa del trabajo, en un formato estructurado que cada turno lee al despertar y actualiza al dormir. Real y minimalista:

```json
// features.json — el turno lee esto ANTES de tocar nada
[
  {"id": "F-07", "estado": "hecha",
   "que": "Validación del formato F-3 de la Confederación",
   "verificacion": "make test-all pasa incluyendo tests/confederacion/"},
  {"id": "F-08", "estado": "en_curso",
   "que": "Exportación de lecturas auditables por rango de fechas",
   "verificacion": "el caso tests/exportacion/test_rangos.py pasa",
   "notas": "el generador de CSV existente NO maneja zonas horarias:
             usar informes_v2/fechas.py, ver ADR-001"},
  {"id": "F-09", "estado": "pendiente",
   "que": "Firma digital del paquete de declaración",
   "verificacion": "make verificar-firma sobre un paquete de ejemplo"}
]
```

Fíjate en las tres decisiones de diseño. Cada feature lleva su **criterio de verificación ejecutable** — el turno no decide si algo «parece hecho»; lo comprueba, y solo entonces cambia el estado (la regla de la sección 5: sin comprobación ejecutable, «parece terminado» es la única señal). El campo `notas` transporta las **trampas descubiertas** — el conocimiento que el turno anterior pagó caro y que el siguiente heredaría gratis. Y los estados son pocos y sin ambigüedad: pendiente, en curso, hecha. Este fichero es, literalmente, la teoría del proyecto en su versión de mínimos: qué se está construyendo, qué significa terminado, qué se aprendió.

**El agente inicializador** corre una sola vez, al principio: monta el esqueleto del proyecto, las convenciones, el arnés (tests, linter, comandos en el AGENTS.md) y el `features.json` inicial a partir de la spec. Su producto no es código de features: es *el terreno* en el que los turnos posteriores no tendrán que decidir nada estructural. Separarlo del trabajo de features no es capricho: las decisiones de estructura exigen ver el conjunto, y son exactamente lo que no quieres que cada turno amnésico reinvente.

**El agente programador** es el turno repetido, y su prompt es un bucle exterior escrito en prosa. Esqueleto real:

```markdown
Eres el turno de trabajo de este proyecto. Protocolo:
1. Lee AGENTS.md, features.json y NOTAS.md. No te saltes este paso.
2. Ejecuta `make test-fast`. Si algo falla, arreglarlo ES tu tarea de hoy.
3. Si no, toma la primera feature "en_curso", o la primera "pendiente".
4. Impleméntala. Commits pequeños y frecuentes con mensajes descriptivos.
5. Ejecuta su criterio de verificación. Solo si pasa, márcala "hecha".
6. Antes de terminar: actualiza features.json, añade a NOTAS.md lo que
   el siguiente turno necesita saber (trampas, decisiones, dudas), y
   deja el árbol limpio y committeado.
```

El paso 2 merece subrayado: **cada turno empieza verificando el mundo, no creyendo el fichero**. Si el turno anterior dejó algo roto, el estado real manda sobre el estado escrito — es el mismo principio del capítulo 9: papel que no se puede auditar, papel que no vale.

**Git como memoria y como checkpoints.** Commits pequeños y frecuentes convierten el historial en dos cosas a la vez: la cronología fiable de lo que de verdad pasó (que ningún resumen puede falsificar) y una escalera de puntos de restauración — un turno que se mete en un callejón sin salida se resuelve con `git reset` al último punto bueno, no con arqueología. La regla del árbol limpio al terminar cada turno es la que hace ambas cosas posibles.

**Las notas estructuradas** (`NOTAS.md`) son el diario entre turnos: no lo que se hizo (eso está en git) sino lo que se *aprendió* — «el simulador tarda 90 s en arrancar: no lo relances por test», «la librería X miente en su documentación sobre Y». Es el cuaderno de asombros del proyecto, escrito por mentes efímeras para sus sucesoras. Y la **compactación** (`/compact` y equivalentes) gestiona la memoria *dentro* de cada turno largo: resumir el historial en los valles entre subtareas, conservando decisiones y descartando volcados.

## El bucle exterior es un script tuyo

Queda la pregunta operativa: ¿quién lanza los turnos? Y la respuesta cierra el círculo con la regla del reparto de la sección 5: **el bucle exterior es código determinista tuyo**, no otro agente. Los agentes de terminal tienen modo no interactivo pensado exactamente para esto — en Claude Code, `claude -p "<prompt>"` ejecuta una sesión completa desde un script y termina —, así que el andamiaje entero cabe en un bucle de shell de diez líneas:

```bash
while grep -q '"estado": "pendiente"' features.json; do
  claude -p "$(cat prompts/turno.md)" || break   # un turno amnésico
  make test-fast || break                        # el mundo, verificado
  git diff --quiet || break                      # árbol limpio o paramos
done
```

Los detalles finos (flags de permisos, límites por turno) dependen de tu herramienta y su versión — lo estable es la arquitectura: un script determinista que lanza turnos no deterministas, verifica el mundo entre turno y turno con comprobaciones que no opinan, y se detiene ante cualquier anomalía en vez de improvisar. El juicio vive dentro de cada turno; el control del bucle, fuera y en código. Si en la sección 10 se habla de «operar sistemas de agentes», este script de diez líneas es su semilla.

## Por qué funciona, y cuándo no usarlo

El patrón funciona porque convierte el problema difícil (mantener coherencia en un contexto que no cabe en ninguna ventana) en uno resuelto (persistir estado en ficheros y verificar con herramientas). Cada pieza ataca una amnesia concreta: el fichero de features, la amnesia de *qué toca*; las notas, la de *qué se aprendió*; git, la de *qué pasó*; el AGENTS.md, la de *cómo se trabaja aquí*; la verificación ejecutable, la de *qué significa bien*. Nada de esto es exótico: es gestión de proyectos clásica — backlog, definition of done, diario de obra — implementada para trabajadores que duermen cada pocas horas y despiertan sin recuerdos. Que las técnicas de coordinar humanos y las de coordinar agentes converjan no es casualidad: ambas gestionan inteligencias con memoria limitada y contexto parcial.

Y el criterio de no-uso, para que la herramienta no se te convierta en martillo: este andamiaje cuesta montarlo y mantenerlo. Para una tarea de una tarde es burocracia pura — el flujo simple de la teoría (explorar, planificar, ejecutar, revisar en una sesión) la cubre mejor. El umbral razonable: cuando el trabajo no cabe en una sesión *y* tiene descomposición natural en unidades verificables, el patrón paga; si no se dan ambas, no. Es la misma economía de las evals en la sección 6 — inversión proporcional al tamaño y al riesgo, y la honestidad de admitir que la mayoría de las tareas siguen siendo de una sesión.

## Para llevar

- Loop engineering = diseñar el bucle exterior que envuelve muchas sesiones amnésicas: inicializador (una vez: terreno y arnés) + programador (turnos: leer estado → verificar mundo → una feature → verificar → persistir estado).
- El fichero de features lleva criterio de verificación ejecutable por entrada; los estados los cambian las comprobaciones, no las sensaciones.
- Git es memoria y checkpoint: commits pequeños, árbol limpio al final de cada turno, reset antes que arqueología.
- Las notas estructuradas transportan lo aprendido; la compactación gestiona la memoria dentro del turno.
- Es gestión de proyectos clásica para mentes efímeras — y solo compensa cuando el trabajo excede una sesión y se descompone en unidades verificables. Para lo demás, el flujo simple.
