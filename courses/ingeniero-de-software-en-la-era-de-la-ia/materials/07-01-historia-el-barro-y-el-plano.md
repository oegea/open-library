La oportunidad llegó en agosto, con membrete oficial y un plazo imposible.

La Confederación Hidrográfica abría un programa piloto: las comunidades de regantes que pudieran declarar sus consumos de forma telemática, con lecturas auditables, tendrían prioridad en las dotaciones del año siguiente y una línea de ayudas para modernización. Paca llamó antes de que Élia terminara de leer el correo.

—Los Alcores tiene que estar en ese piloto —dijo—. Y las otras cuatro comunidades vuestras, también. Si el agua se va a repartir mirando datos, mis datos van a estar impecables. ¿Cuándo lo tenéis?

El pliego técnico eran cuarenta páginas de formatos de intercambio, firmas, validaciones cruzadas y calendarios de remisión. La fecha límite del piloto: diez semanas. Élia hizo cuentas en la pizarra: con el equipo disponible y el ritmo histórico, aquello eran cinco meses.

—Pues que lo haga la Cuadrilla —dijo Bruno—. Para esto la hemos criado, ¿no?

Y así fue como Vega hizo su primer proyecto grande *agent-first*: humanos diseñando, decidiendo y revisando; agentes escribiendo la mayor parte del código, en paralelo, dentro del arnés. Nadie esperaba que fuera un camino recto. Nadie esperó tampoco lo que resultó ser: el mejor espejo que la empresa había tenido jamás de su propio código.

---

Las dos primeras semanas fueron casi eufóricas.

El grueso del trabajo nuevo tocaba el planificador y el dominio de medidas: precisamente las zonas que la reconquista del desván había dejado más limpias. Allí los módulos tenían fronteras claras, nombres honestos y tests rápidos; el `AGENTS.md` contaba las reglas de la casa; los documentos de diseño que habían escrito en primavera —incluido el de la hora de acequia— daban el contexto que ningún modelo podía adivinar. Sobre ese terreno, la Cuadrilla voló.

Nadia organizó el trabajo como había aprendido a organizarlo aquellos meses: nada de pedirle a un agente «hazme la integración con la Confederación» y esperar el milagro. Primero, una sesión de exploración: un agente leyendo el pliego y el código, produciendo un análisis de qué tocaba dónde, que Élia y Tomás corrigieron a mano —el análisis confundía dos tipos de contador, y solo Tomás lo sabía—. Luego, un plan por escrito, troceado en tareas que cabían en una tarde, cada una con su criterio de «hecho» verificable. Y solo entonces, ejecución: tres agentes en paralelo, cada uno en su copia de trabajo aislada, cada tarea con sus tests primero, y todo desembocando en pull requests que los humanos leían enteros, línea a línea, como leía Tomás.

Hasta le pusieron nombre a la liturgia de después de comer: *la revisión cruzada*. Un agente escribía; otro distinto, con instrucciones de ser desconfiado y con la spec en la mano, revisaba lo escrito y señalaba lo dudoso; y solo lo que sobrevivía a esa segunda mirada llegaba a la mesa de los humanos. «Dos máquinas discutiendo antes de molestarme a mí», resumió Tomás. «Como poner a dos aprendices a repasarse las soldaduras el uno al otro. No sustituye mi ojo. Me lo ahorra para donde hace falta.»

El viernes de la segunda semana, el módulo de declaraciones estaba al sesenta por ciento y los tests contaban la historia en verde. Élia miró el tablero y dijo en voz alta lo que todos pensaban:

—A este ritmo llegamos.

No llegaron a este ritmo. Porque la tercera semana, el proyecto entró en el módulo de informes.

---

El módulo de informes era la última gran mancha naranja del mapa. Lo habían dejado para el final de la reconquista precisamente porque nadie quería entrar: era el barrio viejo de Azud, el sitio donde vivía el código de 2022, el año en que Vega era tres personas con un cliente y ninguna hora para limpiar. Generaba los PDF mensuales, los históricos, las exportaciones. Funcionaba —llevaba años funcionando— y por dentro era exactamente lo que la palabra «funcionar» permite esconder: un fichero de dos mil líneas llamado `report_utils.py`, fechas en tres formatos, lógica de negocio trenzada con maquetación de PDF, y una función llamada `process_data_v2` cuya versión uno nadie encontró jamás.

La Confederación exigía que las declaraciones enlazaran con los históricos auditables. Había que tocar el barrio viejo. Y la Cuadrilla, que en el planificador había volado, en `report_utils.py` se hundió en el barro delante de todos.

No fue un fallo escandaloso. Fue peor: fue una degradación *plausible*. El primer agente que entró produjo un cambio que pasaba los tests —los cuatro tests que había— y que rompía sutilmente la exportación trimestral, porque en aquel fichero la palabra `total` significaba tres cosas distintas según la línea, y el agente eligió, con toda la razón estadística del mundo, la que no era. El segundo agente, mandado a arreglar lo del primero, propuso refactorizar un tramo… y su refactor, elegante sobre el papel, asumía que `period` era un rango de fechas cuando a veces era una clave de caché con formato de fecha. El tercero directamente se perdió: gastó su sesión entera dando vueltas por el fichero, cargando contexto y más contexto, hasta diluirse en generalidades. La revisión cruzada señalaba dudas por todas partes, que era su manera de decir que allí dentro no había suelo firme para nadie.

—Parad las máquinas —dijo Tomás el miércoles, y no lo decía en broma—. Todas fuera de ese módulo. Venid a ver esto, que hoy hay clase.

Proyectó los tres pull requests fallidos, uno al lado de otro.

—¿Veis lo que yo veo? Los tres errores son *nuestros*. —Fue señalando—. Este: una palabra que significa tres cosas. Este: un dato que miente sobre su tipo. Este: un fichero tan grande que no cabe en la cabeza de nadie, y resulta que en la suya tampoco. La máquina no ha metido el barro. El barro estaba. La máquina solo se ha hundido más rápido que nosotros, porque camina más deprisa y no sabe dónde pisamos nosotros de memoria. —Se volvió hacia el equipo—. En el planificador vuela porque el planificador tiene *plano*. Aquí se hunde porque aquí solo hay costumbre. Y la costumbre no se puede poner en un fichero de contexto.

Nadia miraba los tres PR con una sensación extraña, casi de gratitud.

—¿Sabéis lo que es esto? —dijo—. Es la auditoría de arquitectura más barata de la historia. Llevábamos años sospechando que el módulo de informes era deuda. Ahora tenemos la medida exacta: es el sitio donde nuestros agentes pierden el norte. La legibilidad ha dejado de ser una opinión. Se puede *observar*.

Élia tomó la decisión esa misma tarde, y la tomó como había aprendido a tomarlas aquel año: por escrito. Abrieron un documento corto, numerado —el primero de una serie que ya no pararía—, con cuatro apartados: contexto, decisión, alternativas descartadas, consecuencias. *Decisión: no se refactoriza el módulo de informes entero (no hay tiempo y el riesgo es alto). Se estrangula: la funcionalidad nueva de auditoría se construye en un módulo aparte, con frontera limpia, y el módulo viejo se irá vaciando función a función, cada una con sus tests de caracterización antes de moverla. Los agentes trabajan solo en el módulo nuevo y en las funciones ya caracterizadas.*

—¿Y esto por qué lo escribimos, si lo hemos decidido los cuatro en una tarde? —preguntó Bruno, bolígrafo en mano.

—Porque dentro de un año no nos acordaremos de por qué —dijo Élia—. Y porque no lo escribimos solo para nosotros. —Señaló con la cabeza el tablero de la Cuadrilla—. Ellos también lo van a leer. Es la primera vez en la historia de este oficio que la documentación tiene un lector infatigable que hace caso de lo que pone. Pienso aprovecharlo.

---

Entregaron a tiempo. La octava semana, con margen, las cinco comunidades de Vega declararon sus consumos al piloto de la Confederación, y los datos de Paca fueron —ella se encargó de contárselo a media provincia— los primeros en entrar impecables a la primera validación.

La retro del proyecto fue larga, y Nadia la resumió en el corcho con dos columnas que después fotografió para el cuaderno:

**Donde había plano** (fronteras claras, nombres honestos, tests rápidos, contexto escrito): *la Cuadrilla multiplicó al equipo. Semanas de trabajo en días.*

**Donde había barro** (el fichero de dos mil líneas, palabras con tres significados, saber que solo vivía en cabezas): *la Cuadrilla se hundió — igual que nosotros, pero más rápido y con más seguridad en sí misma.*

Y debajo, la conclusión que le parecía la más importante desde la de marzo:

*Día 199. Todo lo que siempre nos contaron sobre escribir código limpio para el compañero que vendrá después era verdad, pero ahora tiene un giro nuevo: el compañero ya está aquí, lee a mil páginas por minuto, trabaja de noche y se cree todo lo que el código le dice. La arquitectura ya no es solo cortesía con los humanos. Es la interfaz de la automatización. El plano vale más que la pala.*

Aquella noche, mientras cerraban, Élia se quedó mirando el gráfico de costes del proyecto en el panel de facturación de Corvus —porque los modelos que usaba la Cuadrilla seguían corriendo, en parte, por las tuberías de Corvus, resto del viejo contrato— y frunció el ceño.

—Oye —dijo—. ¿Habéis visto el correo de Corvus? «Cambios importantes en tu plan». Lo manda un tal… —amplió la firma— «VP of Customer Success». Antes firmaba Íker.

Tomás recogió su chaqueta con un suspiro de veterano.

—Cuando cambia el que firma —dijo—, cambia el precio. Mañana lo leemos con café.

---

*En la teoría de esta sección: por qué el código legible se ha convertido, literalmente, en la interfaz de la automatización — la evidencia de que los agentes rinden donde la arquitectura es limpia y fracasan donde no; cómo montar el flujo de trabajo completo que Vega usó (explorar → planificar → ejecutar → revisar, agentes en paralelo, revisión cruzada writer/reviewer); y los ADR: la memoria escrita de las decisiones, ahora con un lector que nunca se cansa.*
