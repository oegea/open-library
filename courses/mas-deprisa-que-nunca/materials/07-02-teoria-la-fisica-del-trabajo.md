Lo que el Petirrojo descubrió con su experimento no es psicología ni cultura: es matemática aplicada — la misma que gobierna el tráfico, las fábricas y los routers. El trabajo del conocimiento fluye por un sistema de colas, y los sistemas de colas obedecen leyes tan poco negociables como la gravedad. Esta sección presenta esas leyes (con simulaciones que puedes ejecutar), la evidencia empírica sobre sus versiones humanas — interrupciones, multitarea, fragmentación — y el corolario estratégico que el Cuaderno le dejó pendiente a Nadia: la restricción se mueve.

## 1. La ley de Little: el teorema más útil que aprenderás este año

**John D. C. Little** demostró en 1961 un teorema de una elegancia brutal (la exposición pedagógica canónica, en abierto: Little y Graves, "Little's Law", 2008):

> **L = λ · W** — el número medio de ítems en un sistema (L) es igual a su tasa de salida (λ) por el tiempo medio que cada ítem pasa dentro (W).

Reordenado en la forma que usó Nadia: **W = L / λ** — *el tiempo medio de travesía es el trabajo en curso dividido por el throughput*. Con 34 ítems dentro y 8 saliendo por semana: W = 34/8 ≈ 4,3 semanas de espera media para cualquier cosa que entre, **independientemente de su urgencia**. La fuerza del teorema está en su generalidad: no asume distribuciones, no asume disciplina de cola, no asume nada salvo estabilidad a largo plazo. Es contabilidad pura: si hay mucho dentro y sale poco, cada cosa pasa mucho tiempo dentro.

De aquí, el fundamento matemático del **límite de WIP** (*work in progress*): a igualdad de throughput, **la única forma de reducir el tiempo de entrega es reducir lo que está en curso**. No es una preferencia estética de Kanban: es un teorema. Y explica el resultado «paradójico» del experimento — terminar más empezando menos — que deja de ser paradójico al ver qué hace el exceso de WIP con el throughput mismo: cada ítem abierto cuesta cambio de contexto (§3), envejecimiento (conflictos de merge, contexto olvidado, código de debajo que cambia) y coordinación. El WIP no es inventario neutro: es inventario *que se pudre*.

## 2. La curva de Kingman: por qué el 100% de utilización es un atasco

Segunda ley, menos conocida y más subversiva. En cualquier sistema con **variabilidad** — y el trabajo del conocimiento es variabilidad pura: tareas de tamaños distintos que llegan cuando llegan — el tiempo de espera en cola no crece linealmente con la utilización del servidor: crece como **ρ/(1−ρ)**, donde ρ es la utilización (aproximación de **Kingman**, 1961; el tratamiento de texto está en cualquier manual de teoría de colas). La forma de la curva lo es todo:

- Al 50% de utilización, el factor de espera es 1.
- Al 80%, es 4.
- Al 90%, es 9.
- Al 95%, es 19. Y hacia el 100%, la espera tiende a **infinito**.

Un equipo (o una persona, o una cola de review) planificado al 100% de su capacidad no es un equipo eficiente: es un sistema donde cualquier variación — la tarea que se complica, la urgencia del miércoles — no tiene dónde absorberse y se convierte en cola para todo lo demás. «Un atasco con la autoestima alta.» Compruébalo en veinte líneas:

```python
import random

def simula_cola(utilizacion, horas=200_000):
    """Un 'servidor' (el equipo revisando). Llegadas y servicios variables."""
    t_libre, esperas = 0.0, []
    reloj = 0.0
    while reloj < horas:
        reloj += random.expovariate(utilizacion)      # llegada de trabajo
        servicio = random.expovariate(1.0)             # duración variable
        inicio = max(reloj, t_libre)
        esperas.append(inicio - reloj)                 # cuánto esperó en cola
        t_libre = inicio + servicio
    return sum(esperas) / len(esperas)

for u in (0.5, 0.7, 0.8, 0.9, 0.95, 0.99):
    print(f"utilización {u:.0%} → espera media {simula_cola(u):6.1f}x "
          f"{'█' * int(min(simula_cola(u), 60))}")
```

Ejecútalo: verás la espera explotar de forma no lineal en el último tramo — el tramo donde viven casi todas las organizaciones, porque «tener a la gente ociosa» parece desperdicio. La lección de la teoría de colas es la contraria: **el margen no es desperdicio; es la capacidad de responder**. Con dos corolarios prácticos: no planificar sprints al 100% de la capacidad (la variabilidad necesita hueco o se convierte en incumplimiento), y — la cuenta de Nadia — una cola alimentada por encima de su capacidad de vaciado (22 PRs/día contra 9) no está «apretada»: está **matemáticamente divergente**, y ninguna exhortación la arregla. O llega menos, o sale más, o crece para siempre.

Este es, dicho sea de paso, el análisis correcto del fenómeno central de la era de los agentes: la IA multiplicó λ de llegada a la cola de verificación humana sin tocar su capacidad de servicio. El resultado — colas de review desbordadas, aprobación degenerando en ritual — no es un fallo moral de los revisores: es Kingman operando exactamente como opera. La sección 13 lo retomará con los datos de DORA.

## 3. Lotes pequeños, y el precio medido de la multitarea

Tercera ley de la física del flujo: **el tamaño del lote**. Entregar en lotes grandes (la release trimestral, el PR de 3.000 líneas, la migración de un golpe) infla todas las variables malas a la vez: más WIP (Little: más espera), más variabilidad (Kingman: más cola), feedback más tardío (sección 6: corrección más cara) y riesgo concentrado. La formalización aplicada al desarrollo de producto es de **Donald Reinertsen** (*The Principles of Product Development Flow*, 2009 — un practicante traduciendo la matemática estándar, y de los buenos): las colas invisibles del trabajo del conocimiento son el mayor coste de desarrollo, y el tamaño de lote es la palanca más infravalorada. El PR pequeño no es una manía de revisores tiquismiquis: es teoría de colas.

¿Y la multitarea humana? Aquí la evidencia es experimental y robusta:

- **Rubinstein, Meyer y Evans (2001, *JEP: Human Perception and Performance*)**: cambiar de tarea impone **costes de cambio** medibles que crecen con la complejidad de las tareas — el «residuo atencional» de la tarea anterior contamina la siguiente. (La cifra divulgada «pierdes el 40% del tiempo» es una síntesis de la APA, no del paper: cítala como estimación divulgativa.)
- **Gloria Mark et al. (CHI 2005, "No Task Left Behind?")**, observación de campo: el trabajo del conocimiento está brutalmente fragmentado — ~11,5 minutos de media por «esfera de trabajo» antes de cambiar; el 57% de las esferas se interrumpe; y tras una interrupción con desvío, retomar la tarea original cuesta **de media 25 minutos y 26 segundos**. (La cifra viral «23 minutos y 15 segundos» no existe en ningún paper — procede de una entrevista de 2006; el dato real es este.)
- **Mark, Gudith y Klocke (CHI 2008)**, experimento: la gente interrumpida *termina antes* — comprime — pero paga en **estrés, frustración y presión temporal** significativamente mayores. La interrupción no siempre roba tiempo: roba salud y calidad de decisión.
- **Meyer et al. (2017, *IEEE TSE*)**, monitorización de developers profesionales: fragmentación extrema — **0,3 a 2 minutos por actividad** antes de cambiar; y **Parnin y Rugaber (2011)**, con 10.000 sesiones de programación: solo **una de cada diez** tareas de programación interrumpidas se retoma en menos de un minuto — reconstruir el contexto mental cuesta.
- Y el marco del día completo: **Xia et al. (2018, *IEEE TSE*, 78 profesionales, ~3.148 horas)**: los developers dedican **~58% del tiempo a comprensión de programas** (leer, navegar, buscar) — escribir código es una fracción minoritaria de la jornada. El activo que las interrupciones destruyen — el modelo mental cargado — es, literalmente, donde se va más de la mitad del trabajo.

Sobre la multitarea entre *proyectos*: la regla célebre de Weinberg (~20% de pérdida por proyecto simultáneo adicional) es **heurística de consultor sin estudio detrás — anécdota, dígase así**; la evidencia real (Vasilescu et al., 2016, con datos masivos de GitHub) muestra el patrón matizado: más proyectos se asocia a más output agregado, pero el **cambio rápido y frecuente** entre ellos se asocia a menor productividad por proyecto. El problema no es tener dos cosas; es alternarlas cada veinte minutos.

De toda esta pila sale la justificación empírica de las prácticas del experimento: **una historia por persona** (minimizar residuo atencional), **mañanas de fabricante** — la formulación clásica es el ensayo de Paul Graham "Maker's Schedule, Manager's Schedule" (2009): el que hace necesita bloques de media jornada; una sola reunión «rompe la tarde en dos trozos, cada uno demasiado pequeño para hacer nada difícil» — y **daily corta a hora fija** (concentrar la sincronización en un punto barato en lugar de repartirla en interrupciones caras).

## 4. Slack: el margen como inversión, con su curva

Si el 100% de utilización es un atasco, ¿cuánto margen es sano? La evidencia organizativa dibuja una **U invertida**: **Nohria y Gulati (1996, *Academy of Management Journal*, 264 departamentos)** encontraron que demasiado poco *slack* organizacional mata la experimentación (no hay con qué probar nada) y demasiado relaja la disciplina; el óptimo está en un punto intermedio. **Tom DeMarco** (*Slack*, 2001 — ensayo de practicante) lo formuló para el software: la eficiencia total y la capacidad de cambio son un trade-off; la organización 100% ocupada no puede cambiar, porque cambiar consume exactamente el recurso que no tiene: atención no comprometida.

Y el caso célebre, con su verdad incómoda: el **20% time de Google** existió como política informal (la carta de salida a bolsa de 2004 lo presume; de ahí salieron AdSense y Gmail según la leyenda corporativa), pero nunca fue un derecho formal: hacia 2013 requería aprobación y fue descrito por la prensa como «muerto en la práctica» — Marissa Mayer llegó a llamarlo «120% time». Úsese como lo que es: evidencia de que el slack institucionalizado produce cosas *y* de que es frágil — lo primero que se recorta cuando alguien mira la utilización con ojos de Taylor.

Para un equipo, el slack operativo tiene formas concretas: no comprometer el 100% de la capacidad del sprint, presupuesto explícito para mejora y deuda (la sección 10 volverá), y — la versión de esta era — **no rellenar automáticamente con más tareas el hueco que abren los agentes**. Si la IA te devuelve el 30% del tiempo y lo conviertes todo en más tickets, has elegido el punto malo de la U invertida a máxima velocidad.

## 5. Amdahl y Goldratt: la restricción se mueve

Cierre estratégico, que es la nota que el Cuaderno le dejó a Nadia. **Gene Amdahl** (1967) formuló para los procesadores un límite que gobierna cualquier sistema: **la aceleración total está limitada por la fracción no acelerada**. Si aceleras infinitamente una fase que era el 30% del tiempo total, el sistema se acelera como máximo un factor 1,43 (1/0,7) — un recorte de en torno al 30% del tiempo total, y ni un minuto más. Escribir código es una fracción del lead time de una feature — y una fracción minoritaria de la jornada del developer (Xia: la comprensión domina) —, así que **«programar 10× más rápido» nunca pudo significar «entregar 10× más rápido»**: la promesa violaba a Amdahl desde el día uno. Lo que sí hace acelerar una fase es **desplazar el cuello de botella** — de generar a revisar, de revisar a decidir, de decidir a validar con usuarios.

La gestión de ese desplazamiento tiene doctrina: la **teoría de las restricciones** de Eliyahu Goldratt (*The Goal*, 1984): (1) identifica la restricción del sistema; (2) explótala (que no pare, que no procese basura); (3) **subordina todo lo demás a ella** — de nada sirve que las no-restricciones produzcan más de lo que la restricción traga: solo fabrican inventario (¡los 22 contra 9!); (4) eleva la restricción; (5) **vuelve al paso 1, porque la restricción se ha movido**. El experimento del Petirrojo es este algoritmo ejecutado sin saberlo: identificaron la review como restricción, subordinaron la generación de los agentes a ella (límite de cola), la explotaron mejor (dueños con contexto: verificación al doble de velocidad) — y el siguiente cuello ya asoma, porque siempre asoma: cuando entregar deja de ser el problema, el problema pasa a ser decidir qué entregar. Que es exactamente el viaje que este curso lleva desde la sección 3.

## Para llevar

- Ley de Little: W = L/λ. Con 34 cosas en curso y 8 saliendo por semana, todo tarda un mes, sea cual sea su urgencia. Limitar el WIP no es estética Kanban: es el único camino matemático a entregar antes sin producir más.
- Curva de Kingman: con variabilidad, la espera explota de forma no lineal al acercarse la utilización al 100%. El margen no es desperdicio: es capacidad de respuesta. Y una cola alimentada por encima de su capacidad (agentes 22/día, humanos 9/día) diverge: se arregla con diseño, no con broncas.
- Lotes pequeños abaratan todo a la vez: menos WIP, menos variabilidad, feedback antes, riesgo repartido. El PR pequeño es teoría de colas aplicada.
- La fragmentación medida es brutal (25m26s para retomar tras interrupción con desvío — no «23m15s», cifra sin paper; 0,3-2 min por actividad; solo 1 de 10 tareas de programación se retoma en <1 min) y el ~58% de la jornada es comprensión: proteger bloques de fabricante y minimizar tareas paralelas ataca el mayor coste real del trabajo.
- El slack sigue una U invertida (Nohria & Gulati): sin margen no hay experimentación ni cambio; el hueco que abre la IA es una decisión de inversión, no un vacío a rellenar con tickets.
- Amdahl: acelerar una fase acota poco el total y desplaza la restricción. Goldratt: identifícala, subordina todo a ella, y cuando la muevas — vuelve a empezar. En 2026 la restricción ya no es teclear: es verificar y decidir.

## Para profundizar

- Little, J. & Graves, S. (2008). "Little's Law" — PDF: https://web.eng.ucsd.edu/~massimo/ECE158A/Handouts_files/Little.pdf · Retrospectiva del 50 aniversario: https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf
- Mark, G., González, V. & Harris, J. (CHI 2005). "No Task Left Behind?" — PDF: https://ics.uci.edu/~gmark/CHI2005.pdf · Mark, Gudith & Klocke (CHI 2008): https://ics.uci.edu/~gmark/chi08-mark.pdf
- Rubinstein, Meyer & Evans (2001) — PDF de la APA: https://www.apa.org/pubs/journals/releases/xhp274763.pdf
- Meyer et al. (2017). "The Work Life of Developers" — PDF: https://gwern.net/doc/psychology/writing/2017-meyer.pdf · Xia et al. (2018), comprensión ~58%: https://baolingfeng.github.io/papers/tsecomprehension.pdf
- Graham, P. (2009). "Maker's Schedule, Manager's Schedule": https://www.paulgraham.com/makersschedule.html
- Reinertsen, D. — *The Principles of Product Development Flow* (libro de pago; la matemática subyacente es Little y Kingman, arriba).
- MIT OCW 15.871, *Introduction to System Dynamics* (CC BY-NC-SA) — para los bucles y retardos con rigor: https://ocw.mit.edu/courses/15-871-introduction-to-system-dynamics-fall-2013/
