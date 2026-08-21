La teoría dejó establecido que la estimación humana está sesgada de fábrica y que la corrección es la vista externa. Esta ampliación baja al taller: qué prácticas concretas se derivan de eso, qué hay detrás del debate #NoEstimates, y — lo más útil — cómo traducir curvas a conversaciones que negocio pueda usar.

## 1. Por qué la estimación relativa no es una moda

Las prácticas ágiles de estimación (puntos de historia, tallas de camiseta, comparar «esto es como aquello») suelen presentarse como liturgia. Su justificación real es psicológica y estadística:

- **Comparamos mejor que medimos.** El juicio humano es más fiable en términos relativos («esta tarea es más grande que aquella») que absolutos («esta tarea son 34 horas»). La estimación relativa apuesta por el tipo de juicio en el que somos menos malos.
- **El punto de historia es una unidad de clase de referencia.** Si el equipo trocea el trabajo en ítems comparables y mide cuántos completa por semana, ha construido — sin llamarla así — la distribución que alimenta el Monte Carlo de la teoría. «Yesterday's weather» (asumir que esta semana rendirás lo que rendiste las anteriores) es reference class forecasting artesanal.
- **La agregación de juicios independientes funciona — si es independiente.** El planning poker (estimar en secreto, revelar a la vez) no es un juego: evita que la primera cifra dicha ancle a las demás. El anclaje es de los sesgos mejor documentados, y la revelación simultánea es su antídoto estructural. (La sección 9 generalizará este truco a todas las decisiones de grupo.)

La trampa conocida: en cuanto los puntos de historia salen del equipo y se convierten en métrica de rendimiento («este equipo hace 40 puntos, aquel 60»), dejan de medir — se inflan, se negocian, se corrompen. Es la ley de Goodhart, protagonista de la sección 8; quédate ahora con la regla práctica: **los puntos existen para alimentar la previsión del equipo, no para compararlo ni evaluarlo**.

## 2. El debate #NoEstimates, contado sin bandos

Hacia 2013, un sector de la comunidad (Woody Zuill, Vasco Duarte, entre otros) empezó a defender que muchas estimaciones no valen lo que cuestan: horas de ceremonia para producir números que nadie usa bien, que se convierten en compromisos, que castigan la honestidad. La contrapropuesta: trocear pequeño, contar ítems terminados (*throughput*) y proyectar con datos — es decir, sustituir el juicio prospectivo por la medición retrospectiva.

Lo defendible de cada lado, sin tribalismo:

- **A favor del espíritu #NoEstimates:** si tus ítems son razonablemente pequeños y parecidos, contar funciona igual o mejor que puntuar — el Monte Carlo de la teoría usa throughput, no puntos — y elimina horas de ritual y una superficie entera de gaming. Los datos de Jørgensen muestran además que décadas de inversión en «estimar mejor» han movido poco la aguja del sobrecoste.
- **A favor de estimar:** la conversación de estimación descubre malentendidos («¿cómo que 13? ¿tú qué estás entendiendo por esta historia?») que valen más que el número resultante; algunas decisiones (¿construimos esto o no?) necesitan orden de magnitud *antes* de que exista historial; y «no estimamos» degenera fácilmente en «no nos comprometemos a nada», que negocio traduce — con razón — como opacidad.
- **La síntesis práctica** que muchos equipos maduros alcanzan: estimar en grueso lo grande (¿semanas, meses, trimestres?) para decidir si entrar; trocear pequeño lo decidido; proyectar con throughput real; y no volver a discutir si aquella historia era un 5 o un 8, porque a la curva le da igual.

## 3. La cola larga: por qué «probablemente el martes» significa «quizá en mayo»

Un detalle técnico de la teoría que merece ampliarse, porque cambia la intuición: los plazos reales siguen distribuciones **lognormales** (Little, 2006) — asimétricas, con cola larga hacia el retraso. Esto tiene consecuencias que la intuición gaussiana no ve:

- **La moda engaña.** El resultado *más probable* de una tarea puede ser «3 días» y su *media* ser 6, porque la cola (el 10% de veces que se lía y son 20 días) pesa mucho. Cuando alguien estima «lo normal es que sean 3 días», suele estar reportando la moda — el escenario en que nada se tuerce — y las carteras de proyectos no viven de modas, viven de medias y percentiles.
- **Las sumas heredan la cola.** Un plan de 10 tareas «de 3 días» no dura 30 días: la probabilidad de que *ninguna* de las diez caiga en su cola es baja. Por eso los proyectos compuestos se retrasan más que sus piezas, sin que nadie haya estimado ninguna pieza de mala fe.
- **Percentiles, no promesas.** La única forma coherente de comprometerse sobre una distribución con cola es elegir percentil: P50 si ambas partes aceptan retrasarse una de cada dos veces; P85 o P95 para compromisos duros. Elegir percentil es una decisión *de negocio* (¿cuánto vale llegar seguro vs. llegar pronto?), y esa es precisamente la conversación que la fecha-punto impide tener.

## 4. Cómo hablar de fechas con quien necesita fechas

Marga tiene parte de razón: «un cliente no puede recibir una curva». La solución no es esconder la curva, sino traducirla. Tres patrones que funcionan:

1. **Compromiso por percentil con lenguaje de compromiso.** Al cliente no se le enseña el histograma: se le dice «lo tendréis el 20 de mayo» — habiendo elegido internamente el P85 — y se gestiona el margen. Lo deshonesto no es dar una fecha; es dar el P12 como si fuera una fecha.
2. **Alcance flexible, fecha fija.** Si la fecha es innegociable (una feria, un cambio normativo), la variable de ajuste es el alcance: se ordena el trabajo por valor y se garantiza que *lo que haya el 15 de marzo funciona*, aunque no sea todo. Es el principio agile de entregar incrementos utilizables convertido en herramienta de negociación — y suele descubrirse que el 40% del alcance prometido nadie lo necesitaba con urgencia (la sección 3 le pone números a esa sospecha).
3. **Re-pronóstico continuo y visible.** La curva no se calcula una vez: se recalcula cada semana con el throughput real, y la fecha proyectada se publica con su tendencia. Un plazo que se degrada avisando con diez semanas de antelación es un problema gestionable; el mismo plazo descubierto la víspera es una crisis. Gran parte del valor de los ciclos cortos está exactamente aquí: no en ir más deprisa, sino en **enterarse antes**.

Nota para la era de los agentes: la tentación de 2026 es pedirle la estimación a la IA, que la produce al instante, desglosada y con confianza encantadora. El desglose es genuinamente útil (barre la superficie de lo conocido mejor que una tarde de reunión); la *fecha* que sale de él hereda todos los sesgos de la vista interna — el modelo construye el mismo escenario optimista, solo que más rápido y mejor redactado — y no conoce la cola de *tu* historial: los datos de Ondara en tres formatos, la validación clínica, el flequillo del RGPD. La regla no cambia: desglosa quien quiera, **pronostica el historial**.

## Para profundizar

- Little, T. (2006). "Schedule Estimation and Uncertainty Surrounding the Cone of Uncertainty", *IEEE Software*, 23(3) — de pago; el hallazgo lognormal está resumido en la teoría.
- Moløkken, K. & Jørgensen, M. (2003). "A Review of Surveys on Software Effort Estimation" — ficha: https://www.semanticscholar.org/paper/ad0c063b126390dbac8ebeab9b1b95b3cf58d6f9
- Flyvbjerg, B. (2006). "From Nobel Prize to Project Management: Getting Risks Right" — arXiv: https://arxiv.org/abs/1302.3642 (reference class forecasting aplicado)
- Sobre anclaje y agregación de juicios: Moore, D. & Healy, P., "The Trouble with Overconfidence" — copia del autor: https://learnmoore.org/mooredata/HOC.pdf
