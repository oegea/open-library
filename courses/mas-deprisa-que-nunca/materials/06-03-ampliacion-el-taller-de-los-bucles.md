La teoría dio los mecanismos; esta ampliación es el banco de trabajo: cómo se traduce la evidencia en formatos concretos, qué antipatrones delatan un bucle roto, y qué papel puede (y no puede) jugar la IA en todo ello.

## 1. Anatomía de un debrief que cumple las condiciones del meta-análisis

Tannenbaum y Cerasoli encontraron el +20-25% en debriefs con alineamiento, estructura y facilitación. Desmontado en piezas operativas:

- **Datos antes que opiniones.** La retro empieza con hechos que nadie discute: el registro de incidencias, el gráfico de flujo, los acuerdos de la retro anterior y su estado. Esto no es burocracia: es anclar la conversación en nivel de tarea (FIT) y desactivar la lotería de memorias selectivas. Regla práctica: si una retro empieza con «¿cómo os habéis sentido?» sin un solo dato delante, acabará donde apunte el que hable más fuerte.
- **Escritura en silencio antes de hablar.** Ya viste el porqué en la sección 5 (hidden profiles, anclaje): lo que se escribe simultáneamente no se contamina de lo que dijo el primero. Cinco-ocho minutos de silencio incómodo compran media hora de contenido real.
- **Ronda con orden pensado.** Los de menos estatus o menos antigüedad primero — no por cortesía, sino porque hablan distinto después de oír al senior (y el senior no cambia por oírlos a ellos).
- **Pocas acciones, con dueño y con fecha.** El antipatrón universal: retros que generan ocho «deberíamos» y cero cambios. Mejor una acción que se hace que cinco que se acumulan como culpa. Y la primera «dato» de la retro siguiente es qué pasó con las acciones de esta — el bucle solo existe si se cierra.
- **Facilitación real.** Alguien — rotativo, no siempre el manager — cuida el proceso: corta las espirales, protege los turnos, reformula los ataques al yo en preguntas de tarea («¿qué habría hecho falta para…?» es la herramienta multiusos). Facilitar es un oficio aprendible, y los repositorios abiertos de formatos (el Retromat de Corinna Baldauf; la Open Practice Library, CC BY) son el catálogo — con la advertencia de que el formato es el 20%: las condiciones del meta-análisis son el 80.

Cadencia y variedad: la evidencia no fija frecuencia, pero la lógica de Gersick (los equipos revisan cuando el calendario obliga) y la del retardo (bucles cortos corrigen barato) apuntan a regular y frecuente — y contra la fatiga de la repetición, variar el formato y, sobre todo, variar el *alcance*: de vez en cuando, una retro de doble bucle explícita («¿siguen teniendo sentido nuestros objetivos/acuerdos/métricas?»), que es la que casi nadie agenda.

## 2. Fórmulas de feedback interpersonal que respetan la FIT

Para el uno-a-uno y la review, tres estructuras que mantienen el misil apuntando a la tarea:

- **Situación-Comportamiento-Impacto (SBI):** «En la review de ayer [situación], el PR se aprobó en cuatro minutos con 800 líneas [comportamiento observable]; el caso de la codificación rara pasó a producción y costó una tarde de retrabajo [impacto]». Sin adjetivos de persona, sin intenciones adivinadas («es que no te importa la calidad» es telepatía, no feedback).
- **La petición explícita:** el feedback sin dirección de futuro es solo queja con formato. «¿Qué haría falta para que esto se cace antes?» — y escuchar de verdad la respuesta, que en el caso de Marc contenía el diagnóstico entero (la cola infinita, los tests del agente validando al agente).
- **El elogio también en modo tarea:** «la descripción de este PR — el contexto de las 8:05 con guantes — le ahorró media hora a quien lo revisó» enseña y refuerza; «eres un crack» activa la maquinaria del yo con signo positivo, que el meta-análisis muestra igualmente estéril. Elogiar bien es tan técnico como criticar bien.

Y una nota sobre frecuencia que conecta con la sección 8: el feedback continuo y cercano a la tarea hace *innecesaria* buena parte de la maquinaria de evaluación formal — que, como verás, tiene sus propios problemas de medición devastadores (más de la mitad de un rating — 62% y 53% según muestra — es ruido del evaluador). El orden correcto es: mucho feedback de tarea, poca ceremonia de juicio.

## 3. Antipatrones de bucle, catálogo de campo

- **La retro-válvula:** el equipo se desahoga, se siente mejor, no cambia nada. Señal: cero acciones completadas en tres retros. Es un bucle abierto — sensación de feedback sin corrección — y a medio plazo cría cinismo («¿para qué decir nada?»).
- **La retro-tribunal:** se buscan responsables con nombre. Señal: la gente prepara defensas antes de entrar. Viola la Directiva y garantiza que la información importante (el fantasma de Duna) no aparezca.
- **El bucle secuestrado:** las acciones de la retro son siempre para otros («que plataforma arregle…», «que dirección decida…»). Un equipo que solo produce acciones ajenas ha renunciado a su agencia — o no la tiene, que es información para el doble bucle.
- **El termostato pintado:** existe la ceremonia, existe el tablero, y las decisiones reales se toman en otra sala. Es la versión de bucle del cargo cult (sección 9): la forma sin el mecanismo.
- **La métrica-anestesia:** «la retro dice que todo bien» porque las métricas que se miran no captan lo que duele. Recordar el termómetro de Edmondson: elegir qué datos abren la retro es elegir qué conversaciones son posibles.

## 4. La IA en los bucles: dónde suma y dónde anestesia

Los agentes ya saben preparar retros: resumir el sprint, agrupar los post-its por temas, redactar las acciones, hasta detectar patrones en seis meses de registros que ningún humano releería. Uso encantado: todo lo que sea **abaratar la parte de datos y estructura** (dos de las tres condiciones del meta-análisis) es bucle mejorado. Dos cautelas con base en lo ya visto:

1. **La tercera condición no se delega.** El efecto del debrief pasa por la conversación humana — el momento en que Duna decide hablar, la pregunta que Sofía sostiene, el silencio que precede a «velocity». Un resumen perfecto de IA *en lugar de* esa conversación es un termostato pintado con mejor tipografía. La IA prepara la sala; la sala la ocupan personas.
2. **Cuidado con el doble bucle delegado.** Los modelos son excelentes proponiendo correcciones de primer bucle (acciones dentro del marco) y estructuralmente tímidos con el segundo (cuestionar el marco que su prompt da por sentado). Si la retro la «conduce» una IA, la pregunta por la temperatura — quién fijó este objetivo y por qué — tenderá a no aparecer. Agéndala tú.

## Para profundizar

- Retromat (catálogo de actividades de retro, en español): https://retromat.org/es/
- Open Practice Library (CC BY): https://openpracticelibrary.com/
- Derby, E. & Larsen, D. — *Agile Retrospectives* (libro de pago, el manual clásico del oficio de facilitar retros).
- Google re:Work — guías de feedback y one-on-ones (gratuitas): https://rework.withgoogle.com/
