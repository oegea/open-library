La teoría dio las leyes; esta ampliación da el panel de instrumentos: las cuatro métricas de flujo que un equipo puede empezar a mirar mañana, el diagrama que las contiene todas, y el criterio económico — coste del retraso — que convierte la priorización de arte adivinatorio en aritmética discutible.

## 1. Las cuatro métricas de flujo

Todo lo que el Petirrojo midió cabe en cuatro números, y conviene fijar el vocabulario porque en la calle se mezclan:

- **Throughput**: ítems *terminados* por unidad de tiempo (terminado = en producción, verificado; no «en review»). El λ de Little.
- **WIP**: ítems empezados y no terminados. El L de Little. Incluye — esto se olvida siempre — todo lo que espera en colas internas: «esperando review» es WIP, por mucho que nadie lo esté tocando. *Especialmente* porque nadie lo está tocando.
- **Lead time / tiempo de ciclo**: lo que tarda un ítem desde que se empieza (o desde que se pide, según definas el sistema — define y no cambies) hasta que está terminado. El W. No un promedio para enmarcar: una **distribución** — recuerda la lognormal de la sección 2: reporta percentiles («el 85% de nuestras historias sale en ≤9 días»), que además alimentan directamente el Monte Carlo de previsión.
- **Envejecimiento del WIP** (*aging*): cuánto lleva abierto cada ítem *ahora mismo*. Es la métrica de alerta temprana: el lead time es forense (habla de lo ya terminado); el aging señala hoy la tarjeta que lleva 12 días atascada en un sistema cuyo P85 es 9. La daily del Petirrojo «mirando las colas y no las caras» es, en la práctica, una revisión de aging.

Con esas cuatro, el **diagrama de flujo acumulado** (CFD): apilar por día cuántos ítems hay en cada estado. Se lee de un vistazo: la distancia vertical entre bandas es el WIP de esa fase; la horizontal, el lead time aproximado; una banda que engorda es una cola creciendo — la de «esperando review» de Aurelia se habría visto engordar semanas antes de que Aitor imprimiera su pantallazo. Veinte líneas de script sobre el export de cualquier tracker lo dibujan; pocas inversiones de una tarde rinden más.

Dos advertencias que anticipan la sección 8: primero, estas métricas describen **el sistema**, no a las personas — en cuanto alguien las use para comparar individuos o equipos, se corromperán (y verás exactamente cómo). Segundo, optimizar el flujo de salida no dice nada del *valor* de lo que sale: un CFD precioso puede estar midiendo una feature factory perfectamente engrasada. Flujo y outcome son ortogonales; hacen falta los dos paneles.

## 2. Coste del retraso: la economía que falta en tu priorización

Reinertsen insiste en que la mayoría de organizaciones no puede responder la pregunta más básica de su economía de producto: *¿cuánto cuesta un mes de retraso de esta iniciativa?* Sin ese número, las decisiones de secuencia se toman por volumen de voz. El **coste del retraso** (*cost of delay*, CoD) lo hace explícito: cuánto valor se deja de capturar (o cuánto coste se sigue pagando) por unidad de tiempo que algo no está entregado — la integración que ahorra 40 horas/mes de trabajo manual tiene un CoD tangible; la feature ligada a la renovación de Ondara, uno enorme y con fecha de caducidad; el rediseño estético, uno cercano a cero.

Y para secuenciar con capacidad limitada (que es siempre), la regla **CD3** (*Cost of Delay Divided by Duration*): prioriza por coste del retraso **dividido por duración**. La intuición: entre una iniciativa que pierde 10.000€/mes y dura 1 mes, y otra que pierde 30.000€/mes y dura 6, la primera primero — liberas su valor rápido y la cola total sufre menos. Es la misma lógica de «lotes pequeños primero» de la teoría, monetizada. (WSJF, la versión de algún framework de escalado, es esto con más ceremonia.)

La honestidad de rigor: los números de CoD serán estimaciones gruesas, con toda la falacia de planificación de la sección 2 encima. No importa tanto como parece: el valor del ejercicio no está en la precisión sino en (a) hacer **comparables** las opciones con un criterio explícito y discutible — «demuéstrame que tu iniciativa pierde más por mes que la mía» es una conversación infinitamente mejor que «lo pide un cliente importante» — y (b) descubrir las iniciativas con CoD cercano a cero que viven en el roadmap por inercia. La estantería de trofeos de la sección 3 estaba llena de CD3 minúsculos que nadie había calculado.

## 3. Pull, no push: la mecánica que sostiene todo

Última pieza conceptual: la diferencia entre sistemas **push** (el trabajo se empuja hacia dentro cuando alguien lo decide: la «cosita urgente» del miércoles entrando porque sí) y **pull** (el trabajo entra solo cuando hay capacidad liberada: alguien termina algo y *tira* del siguiente ítem). El límite de WIP es el mecanismo que convierte un tablero push en uno pull — y su efecto más valioso, como descubrió Marga, no es logístico sino político: **hace que meter algo exija decidir qué no avanza**, con el precio a la vista. Un sistema pull es un sistema donde la sobrecarga es una decisión visible en lugar de un accidente distribuido.

La genealogía viene de la fabricación — el *kanban* de Toyota, tarjetas físicas limitando inventario entre estaciones — y su traducción al trabajo del conocimiento (David Anderson, 2004-2010) fue una **analogía deliberada**, no una copia: aquí lo que se limita no son piezas sino atención. La historia completa de esa traducción, y de quién publica sus guías con qué licencias, pertenece a la sección 12; quédate ahora con el mecanismo: **deja de empezar, empieza a terminar** — la frase-resumen de toda esta sección, y probablemente de la física entera del trabajo.

## Para profundizar

- Vacanti, D. — *Actionable Agile Metrics for Predictability* (libro de pago; el tratamiento de referencia de lead time, aging y previsión probabilística por percentiles).
- Reinertsen, D. — *The Principles of Product Development Flow* (libro de pago; coste del retraso y economía de colas).
- La Kanban Guide (Coleman & Vacanti, gratuita, Creative Commons): https://kanbanguides.org/ — el vocabulario de flujo en 12 páginas.
- Anderson, D. — "A Brief History of Kanban for Knowledge Work": https://djaa.com/brief-history-kanban-knowledge-work/
