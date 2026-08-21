Esta sección trata de la maquinaria que convierte trabajo en aprendizaje — y de por qué a veces la misma maquinaria fabrica lo contrario: defensividad, teatro y rumiación. La semana de Sofía contiene los tres niveles del asunto: el feedback entre personas (la charla con Marc), el feedback del equipo sobre sí mismo (la retro), y el feedback de la organización sobre sus propias reglas (la pregunta de Víctor por el objetivo de velocity). La ciencia distingue los tres niveles con precisión, y en cada uno tiene algo importante — y a menudo contraintuitivo — que decir.

## 1. La física del asunto: bucles de control y retardo

Empecemos por lo abstracto, porque ilumina todo lo demás. La **cibernética** — fundada por Norbert Wiener (*Cybernetics: Or Control and Communication in the Animal and the Machine*, 1948; la reedición de MIT Press está en acceso abierto) — estudió formalmente los sistemas que se autorregulan comparando su salida con un objetivo y corrigiendo: el **bucle de retroalimentación negativa**. El termostato de Aitor. Dos propiedades de estos bucles son leyes de ingeniería con siglo de uso:

1. **El retardo degrada el control.** Un sistema que recibe la señal de error tarde corrige tarde, sobrecorrige, y puede entrar en oscilación (la dinámica de sistemas de Forrester y Sterman lo demuestra formalmente; el «beer game» del MIT es su demostración jugable). La ducha con el grifo lento: quema-hielo-quema.
2. **La corrección barata exige señal frecuente.** Cuanto antes llega el error, más pequeña es la desviación acumulada y más barato corregir.

Todo el andamiaje técnico del agile es esta física aplicada: los **tests** convierten «¿funciona?» de una pregunta mensual en una de segundos; la **integración continua** convierte «¿encaja con lo de los demás?» de un infierno trimestral en una señal diaria; el **despliegue frecuente** convierte «¿lo quiere alguien?» de una apuesta anual en un dato quincenal; la retro convierte «¿estamos trabajando bien?» en una señal mensual. Cuando en la sección 2 dijimos que el valor de iterar es «enterarse antes», estábamos describiendo reducción de retardo en el bucle. Y nota bene para 2026: los agentes de código han acortado espectacularmente el bucle de *generación* — y ni un segundo el de *verificación* ni el de *«¿esto lo quiere alguien?»*. Acelerar un bucle interno dejando lentos los externos produce exactamente lo que la cibernética predice: un sistema que oscila más rápido alrededor del sitio equivocado.

## 2. Feedback entre personas: el meta-análisis que debería ser obligatorio

Y ahora, la cifra que reordenó la charla de Sofía. **Kluger y DeNisi (1996, *Psychological Bulletin*)** hicieron el meta-análisis definitivo de las **intervenciones de feedback**: 607 tamaños de efecto, 23.663 observaciones, un siglo de literatura. Resultados:

- Efecto medio: el feedback mejora el rendimiento, **d = 0,41**. Hasta aquí, lo esperable.
- El hallazgo escondido: **en más de un tercio de las intervenciones (≈38%), el feedback empeoró el rendimiento.** No se explica por azar muestral, y — esto es lo contraintuitivo — no depende del signo: hay elogio que hunde y crítica que levanta.

Su **Feedback Intervention Theory (FIT)** explica el patrón con una variable: **a qué nivel dirige la atención el mensaje**. La atención es finita y jerárquica: puede estar en los detalles de la tarea, en el proceso de la tarea, o en el **yo**. El feedback sobre tarea y proceso («este cálculo ignora el caso X»; «aprobar en tandas de cuatro minutos hace indetectable este tipo de fallo») mantiene los recursos cognitivos donde el trabajo mejora. El feedback que apunta al yo — negativo («eres descuidado») **o positivo** («eres brillante») — desvía los recursos a la autoevaluación: defensa, comparación, rumiación. Corolarios verificados en el propio meta-análisis: el elogio a la persona no mejora el rendimiento; el feedback que incluye solución o estrategia concreta sí; y el feedback comparativo — rankings — está entre lo peor medido. (En educación, Hattie y Timperley, 2007, llegaron a una arquitectura compatible: el feedback eficaz responde «¿a dónde voy? ¿cómo voy? ¿qué sigue?» — tres preguntas de tarea, ninguna de identidad.)

**Estado de la evidencia: sólido** — sigue siendo la referencia estándar treinta años después, sin refutación del patrón central. Y sus aplicaciones al oficio son inmediatas:

- **Code review:** «esta función no maneja el timeout» (tarea) contra «no te preocupaste de los timeouts» (yo). La misma información, direcciones opuestas, efectos opuestos. Las guías de review que prohíben el «tú» no son corrección política: son FIT aplicada.
- **La técnica sándwich, diagnosticada:** el pan del sándwich («eres de los que más aporta… tú vales mucho») es feedback al yo por partida doble — activa la autoevaluación *antes* de llegar al contenido de tarea, que llega con la persiana ya bajada. Por eso «sabe raro»: es estructuralmente contraproducente.
- **Retros e incidentes:** «el pipeline no valida X» aprende; «QA no estuvo fina» defiende. La sección 10 construirá sobre esto la cultura del postmortem.
- **Feedback automatizado:** linters, agentes revisores, dashboards — conviene diseñarlos deliberadamente en modo tarea («esta consulta N+1 …») y jamás en modo comparación de personas. Una IA que redacta «evaluaciones de rendimiento» individuales está industrializando la peor categoría del meta-análisis.

## 3. El debrief: la práctica de equipo con mejor evidencia del curso

Si hubiera que apostar todo el curso a una sola práctica con una sola cifra, sería esta. **Tannenbaum y Cerasoli (2013, *Human Factors*)** meta-analizaron los **debriefs** — revisiones estructuradas tras la acción, la familia a la que pertenecen las retrospectivas y los after-action reviews militares y sanitarios —:

> "Findings from 46 samples (N = 2,136) indicate that on average, debriefs improve effectiveness over a control group by approximately 25% (d = .67)."
> **[traducción propia]** «Los resultados de 46 muestras (N=2.136) indican que, en promedio, los debriefs mejoran la eficacia respecto a un grupo de control en aproximadamente un 25% (d=0,67).»

Un 20-25% de mejora de rendimiento, d=0,67 — efecto medio-grande — consistente en equipos e individuos, en entornos simulados y reales, médicos y no médicos. Para calibrar: pocas intervenciones organizativas de cualquier tipo alcanzan ese tamaño con ese respaldo. **La retrospectiva no es la ceremonia prescindible de los viernes: es, posiblemente, la práctica con más evidencia de todas las que hace un equipo ágil** — el principio 12 del manifiesto («a intervalos regulares, el equipo reflexiona sobre cómo ser más eficaz y ajusta su comportamiento») resulta ser el que mejor ha envejecido empíricamente.

Con una condición que el mismo meta-análisis subraya: el efecto lo producen los debriefs **bien conducidos** — con **alineamiento** (los participantes correctos, sobre el trabajo real), **estructura** (no una charla amorfa: datos, secuencia, preguntas) y **facilitación** (alguien cuida el proceso). La retro muda de enero — tablero en blanco, «¿alguien tiene algo?» — no era un debrief: era la ausencia de uno con la sala reservada. Lo que Sofía montó en febrero (datos primero, escritura en silencio, ronda, acuerdos accionables) es la versión que el meta-análisis mide.

Dos piezas completan la práctica. La **Directiva Prima** de Norm Kerth (*Project Retrospectives*, 2001) — el A4 de la pared — no es amnistía sino **tecnología de encuadre**: al asumir que cada uno hizo lo mejor que pudo *con lo que había*, desplaza la pregunta de «quién» a «qué había» — que es la única pregunta con información dentro; y de paso mantiene el feedback en nivel de tarea (FIT otra vez: la Directiva es un compromiso colectivo de no apuntar al yo). Y el **PDSA** le da el apellido histórico: el ciclo **Plan-Do-Study-Act** viene de Walter Shewhart (1939) y lo difundió W. Edwards Deming, que insistía en «Study» y no «Check» — porque *check* sugiere inspeccionar contra lo esperado, y *study* sugiere **aprender de lo ocurrido**, incluida la sorpresa (la genealogía completa está documentada por Moen y Norman, en abierto en deming.org). Una retro es un PDSA institucionalizado: el sprint fue el Do; la retro es el Study; los acuerdos son el Act; el siguiente sprint, el nuevo Plan. Cuando la Scrum Guide habla de «inspect and adapt», está hablando Shewhart con vocabulario de 2020.

## 4. El doble bucle: Argyris y la pregunta por la temperatura

La retro de marzo cruzó una frontera que tiene teoría propia. **Chris Argyris** (con Donald Schön, *Organizational Learning*, 1978) distinguió:

- **Aprendizaje de bucle simple** (*single-loop*): detectar el error y corregir la acción, **dentro de las variables rectoras dadas** — objetivos, políticas, supuestos intocados. El termostato: hace frío → calefacción.
- **Aprendizaje de doble bucle** (*double-loop*): cuestionar y modificar **las variables rectoras mismas**. ¿Quién fijó esta temperatura? ¿Sigue teniendo sentido?

Las organizaciones, observó Argyris, hacen el simple constantemente y el doble casi nunca — y no por estupidez, sino por **rutinas defensivas**: el doble bucle amenaza objetivos que alguien con poder eligió, y cuestionarlos se siente (a menudo con razón) como riesgo interpersonal — nótese cómo esto engancha con la seguridad psicológica de la sección 5: **el doble bucle es exactamente el tipo de riesgo que solo los equipos seguros pueden permitirse**. La retro del Petirrojo lo ilustra milimétricamente: seis meses de bucle simple (revisar mejor, frenar la cola: goteras) hasta que Bruno pudo pronunciar «velocity» (la lluvia) — y solo porque había Directiva en la pared, datos sobre la mesa y un CTO dispuesto a jugar con las reglas de todos.

Argyris tiene otra pieza dolorosamente pertinente para este público: **"Teaching Smart People How to Learn"** (*Harvard Business Review*, 1991). Tesis: los profesionales más brillantes son a menudo los peores aprendiendo, porque casi nunca fracasan — y al no haber practicado el fracaso, cuando llega activan el **razonamiento defensivo**: la culpa está fuera, el criterio ajeno es el equivocado, la crítica es política. Cuanto más alto el rendimiento histórico, más frágil el aprendizaje. Si has visto a un ingeniero excelente responder a una review dura, o a un CTO responder a una curva de Monte Carlo, sabes que Argyris describía fauna real. El antídoto no es humildad genérica sino estructura: datos despersonalizados, encuadres tipo Directiva, y líderes que **modelan** el doble bucle en público — el «con lo que sabía en ese momento» de Víctor vale, como señal cultural, más que la acción que salga de la retro.

**Estado de la evidencia:** Argyris es teoría rica en casos, no experimentación (escalón caso/teoría de la escalera); su valor es conceptual y diagnóstico. Los debriefs (sección anterior) le ponen los números que él no tenía.

## 5. Práctica deliberada: el feedback como motor del aprendizaje individual, con su tamaño real

Cierre con el bucle individual: ¿cómo se aprende un oficio? La respuesta famosa es la **práctica deliberada** de **Ericsson, Krampe y Tesch-Römer (1993)**: la pericia se construye con práctica *diseñada para mejorar* — en el borde de la capacidad, con **feedback inmediato e informativo** y repetición — no con la mera acumulación de horas. De ahí salió, vía divulgación, la «regla de las 10.000 horas», y toca aplicarle la vara del curso:

- **Macnamara, Hambrick y Oswald (2014, *Psychological Science*, meta-análisis):** la práctica deliberada explica de media el **12%** de la varianza del rendimiento — 26% en juegos, 21% en música, 18% en deportes… y **menos del 1% en profesiones**. Importante, no todopoderoso.
- **Macnamara y Maitra (2019, *Royal Society Open Science*):** la réplica del estudio original de los violinistas no reprodujo el patrón (los «mejores» no practicaban más que los «buenos»).

**Estado: matizado.** Lo que sobrevive bien — y es lo que este capítulo necesita — es el *mecanismo*: **el aprendizaje se acelera con feedback rápido, específico y sobre la tarea**, practicando en el borde de lo que uno sabe. Lo que no sobrevive es el determinismo de las horas. La traducción al oficio: el pairing, la review exigente en modo tarea, y el trabajar ligeramente por encima del propio nivel con red (tests, entornos seguros) son máquinas de práctica deliberada integradas en el flujo — y la razón por la que un año en un equipo con buenos bucles enseña más que cinco en uno sin ellos. Con la advertencia de 2026 que la sección 13 desarrollará: si el agente hace todas las partes difíciles, el humano practica cero horas en el borde de su capacidad — el bucle de aprendizaje individual es el más fácil de romper sin darse cuenta, porque su señal de error tarda años en llegar.

## Para llevar

- El retardo degrada el control (cibernética): tests, CI, despliegue frecuente y retros son reducción de retardo en bucles distintos. Acelerar solo la generación de código (agentes) sin acelerar verificación y validación produce oscilación rápida alrededor del sitio equivocado.
- El feedback medio ayuda (d=0,41) y el 38% de las veces empeora (Kluger & DeNisi): la variable es la dirección — tarea/proceso mejora, yo (elogio incluido) empeora, rankings lo peor. El sándwich es estructuralmente contraproducente; las guías de review sin «tú» son ciencia aplicada.
- El debrief estructurado mejora el rendimiento ~20-25% (d=0,67, Tannenbaum & Cerasoli): la retro bien hecha — datos, estructura, facilitación, Directiva Prima — es posiblemente la práctica ágil con mejor evidencia. La retro muda no es una retro.
- La retro es un PDSA (Shewhart→Deming): *Study*, no *Check* — aprender de lo ocurrido, no inspeccionar contra lo esperado.
- Bucle simple corrige acciones; doble bucle cuestiona las variables rectoras (Argyris). Las organizaciones evitan el doble porque amenaza objetivos con dueño — hace falta seguridad psicológica, encuadre y líderes que lo modelen. Los profesionales brillantes son los más defensivos ante el fallo: estructura antes que carácter.
- La práctica deliberada explica menos de lo que dice su leyenda (12% de varianza; <1% en profesiones), pero su mecanismo — feedback rápido, específico, en el borde de la capacidad — es el motor real del aprendizaje del oficio. Protege las horas de práctica en el borde: son las primeras que la automatización se lleva.

## Para profundizar

- Kluger, A. & DeNisi, A. (1996). "The effects of feedback interventions on performance" — PDF: https://mrbartonmaths.com/resourcesnew/8.%20Research/Marking%20and%20Feedback/The%20effects%20of%20feedback%20interventions.pdf
- Tannenbaum, S. & Cerasoli, C. (2013). "Do Team and Individual Debriefs Enhance Performance?" — abstract: https://pubmed.ncbi.nlm.nih.gov/23516804/ · Guía práctica del propio Tannenbaum: https://cdn.ymaws.com/www.odnetwork.org/resource/resmgr/2013_education/tannenbaum_using_debriefs_ha.pdf
- Moen, R. & Norman, C. — historia del PDSA: https://deming.org/wp-content/uploads/2020/06/PDSA_History_Ron_Moen.pdf
- Argyris — single/double loop y Model I/II, exposición abierta: https://infed.org/mobi/chris-argyris-theories-of-action-double-loop-learning-and-organizational-learning/ · "Teaching Smart People How to Learn" (HBR 1991, paywall): https://hbr.org/1991/05/teaching-smart-people-how-to-learn
- Prime Directive (Kerth): https://retrospectivewiki.org/index.php?title=The_Prime_Directive
- Macnamara et al. (2014), meta-análisis de práctica deliberada — PDF: https://hhs.purdue.edu/skill-learning-and-performance-lab/wp-content/uploads/sites/43/2024/08/macnamara-et-al-2014-deliberate-practice-and-performance-in-music-games-sports-education-and-professions-a-meta-analysis.pdf · Réplica 2019 (open access): https://royalsocietypublishing.org/doi/10.1098/rsos.190327
- Wiener, N. — *Cybernetics* (open access, MIT Press): https://direct.mit.edu/books/oa-monograph/4581
