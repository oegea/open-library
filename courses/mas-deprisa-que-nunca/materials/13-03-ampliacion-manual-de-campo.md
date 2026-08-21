La teoría dio la evidencia y las proyecciones; esta ampliación es deliberadamente práctica: cómo se traduce todo el curso a la mesa de trabajo de alguien que convive con agentes — hoy, no en la especulación. Está organizada como reglas de campo, cada una con su genealogía en el curso, para que no sean liturgia sino mecanismo (ya sabes lo que le pasa a la liturgia).

## 1. Reglas de campo para el flujo humano-IA

**Regla del dueño (secciones 4 y 7).** Cada unidad de trabajo con destino a producción tiene una persona que la firma entera — que entiende el problema, dirige a los agentes que participen, verifica el resultado y responde de él. Los agentes trabajan por tareas; las personas responden por resultados. Corolario práctico: si nadie puede explicar un cambio, el cambio no está listo, pasen los tests que pasen — el módulo de Bruno pasaba los tests.

**Regla de la cola (sección 7).** La capacidad de verificación gobierna el ritmo de generación, no al revés. Límite explícito a los PRs pendientes de revisión humana; cuando el límite se llena, los agentes esperan fuera. Una cola de verificación desbordada no es un problema de esfuerzo de los revisores: es una decisión de diseño pendiente.

**Regla del lote (secciones 3 y 7).** Los agentes tientan con el cambio grande («ya que estoy, refactorizo todo»); la verificabilidad exige lo contrario. Cambios pequeños, de propósito único, con descripción que explique el porqué. El prompt es parte del artefacto: guardarlo en la descripción del PR es documentación gratis del intento.

**Regla de la frontera (sección 13, Dell'Acqua).** Mantén un mapa vivo — explícito, del equipo, actualizado en retro — de dónde el agente es fiable y dónde produce «casi correcto» convincente en *vuestro* dominio y *vuestra* codebase. Las tareas en zona roja llevan verificación reforzada o se hacen a mano. El mapa caduca con cada versión de modelo: revisarlo es mantenimiento, como las dependencias.

**Regla del guardarraíl (sección 8).** Todo indicador de adopción de IA viaja con su contramétrica: throughput con churn temprano y duplicación; velocidad de review con tasa de escape de defectos; % de código generado con… nada, mejor no midas eso, no hay outcome del que sea proxy. Y el test del Becario Fantasma como auditoría periódica del panel.

**Regla del fusible (sección 10).** Presupuesto de error acordado en frío; si se supera, el ritmo de los agentes baja automáticamente. Las defensas no se suspenden bajo presión — se refuerzan; toda excepción, por escrito y con caducidad. La 1:40 de Marc no se prohíbe con carteles: se hace estructuralmente improbable.

**Regla de la hipótesis (sección 3).** Los agentes abaratan construir, no saber si algo debía construirse: con generación barata, la feature factory alcanza velocidades inéditas. Antes de lanzar agentes a una épica, el preregistro de siempre: qué creemos, cómo sabremos que es falso, quién evalúa. Un agente ejecutando una mala idea con brillantez es el desperdicio más pulido de la historia.

## 2. El bucle de aprendizaje propio: que no te lo coman

La evidencia de la sección 13 (Lee, Prather, Gerlich) señala el riesgo silencioso: la descarga cognitiva sin plan devuelve profesionales que aprueban sin poder revisar. Contramedidas individuales, todas versiones de la práctica deliberada (sección 6):

- **Horas de banco.** Trabajo regular sin agente, elegido a propósito en el borde de tu capacidad. No es ludismo: es mantener calibrado el instrumento con el que verificas todo lo demás. Si no sabes qué aspecto tiene el trabajo mal hecho, no puedes reconocerlo.
- **Predicción antes de generación.** Antes de pedirle algo no trivial al agente, escribe (una línea) qué esperas que haga y por dónde fallaría. Comparar tu predicción con el resultado es un ciclo de práctica deliberada gratis — y tu registro personal de dónde está la frontera.
- **Lee código en serio, cada semana.** La comprensión es el 58% del oficio (Xia) y es exactamente el músculo que la generación no ejercita. El código de los agentes de tu equipo es material de lectura tan legítimo como el de tus compañeros — y revisarlo *como docencia* (¿qué haría yo distinto y por qué?) en lugar de como trámite es la diferencia entre atrofia y ventaja.
- **Si eres senior: tu rol docente acaba de revalorizarse.** La revisión-como-enseñanza, el pairing, la pregunta socrática — todo lo que transfiere criterio — es ahora la función de mayor apalancamiento de la organización, porque el criterio es la restricción (Goldratt aplicado a personas). Y si eres junior: busca activamente las empresas que fabrican escaleras — pregunta en la entrevista cómo aprende la gente allí, qué se hace sin agentes y por qué; la respuesta te dice si en cinco años serás alguien con criterio o alguien con historial de aprobaciones.

## 3. La conversación con dirección: el argumento en tres actos

Tarde o temprano te tocará la reunión donde se decide «la estrategia de IA», y este curso entero es tu material. La estructura que funciona (probada por Nadia a lo largo de trece secciones):

1. **Concede lo verdadero.** La IA es real, las ganancias son reales (cita Peng, Cui — con sus contextos), negarlo destruye tu credibilidad. El objetivo no es frenar: es cobrar de verdad las ganancias en lugar de contabilizarlas dos veces (una en la percepción, otra en el retrabajo).
2. **Muestra el sistema.** Amdahl (qué fracción del lead time era generar), la cola de verificación con números propios, DORA 2024-25 (velocidad local contra estabilidad), y — si existe — vuestra propia telemetría de churn y retrabajo. Los datos de casa valen diez veces más que cualquier paper: consíguelos antes de la reunión.
3. **Propón el diseño, no la queja.** Límites de cola, dueños de historia, guardarraíles, fusible, pipeline de juniors como inversión — cada pieza con su porqué y su métrica de éxito. La diferencia entre «esto va demasiado rápido» (queja, pierde siempre) y «así cobramos la velocidad sin pagarla dos veces» (diseño, a veces gana) es todo el juego.

## 4. Lo que no sabemos (lista honesta, para revisar cada año)

Cerramos como corresponde: con la ignorancia inventariada. A fecha de este curso, no hay evidencia sólida sobre: el efecto a largo plazo (>3 años) de la asistencia intensiva sobre la pericia de quien la usa; la economía real de los agentes plenamente autónomos en codebases grandes (los benchmarks están quemados y los estudios de campo, empezando); el diseño óptimo de equipos mixtos humanos-agentes (todo lo que se vende como tal es extrapolación, incluida la de este curso); y si Jevons compensará o no la recomposición del empleo. Quien te venda certeza sobre cualquiera de estos puntos te está vendiendo — repasa la sección 0.2 — un relato con formato de dato. La ventaja del método que has aprendido es que no necesita certeza: necesita hipótesis, bucles cortos y la honestidad de mirar el resultado. Con eso se navega cualquier década, incluida esta.

## Para profundizar

- Willison, S. — serie sobre programar con agentes (práctica de campo honesta y continua): https://simonwillison.net/tags/ai-assisted-programming/
- Anthropic Economic Index — datos abiertos de uso real: https://huggingface.co/datasets/Anthropic/EconomicIndex
- DORA — capacidades y guías (CC BY 4.0): https://dora.dev/
- Y el propio Cuaderno del curso: relee la sección 0.2 una vez al año. Es la única herramienta de esta lista que no caduca.
