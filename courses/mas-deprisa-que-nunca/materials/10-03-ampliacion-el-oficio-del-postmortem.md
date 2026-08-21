La teoría dio los marcos; esta ampliación baja al documento concreto: cómo se escribe y facilita un postmortem que aprende de verdad, qué trampas de lenguaje lo arruinan, y dos temas que casi ningún manual toca — la segunda víctima y la difusión del informe.

## 1. La plantilla mínima (y por qué cada pieza)

Un postmortem útil cabe en estas secciones, en este orden:

1. **Resumen e impacto.** Qué pasó, a quién afectó, cuánto duró, qué NO pasó (en Aurelia: «ninguna dosis incorrecta administrada» — el dato que ancla la gravedad real, ni inflada ni minimizada).
2. **Cronología factual.** La pieza central. Hechos con hora, sin adjetivos ni intenciones: qué se hizo, qué se vio, qué dijo cada sistema. Empieza *antes* del disparador técnico — la cronología de Aurelia empezaba en una comida del 30 de junio — porque el incidente casi nunca empieza cuando empieza.
3. **Causas contribuyentes** (plural deliberado). No «causa raíz»: la metáfora de la raíz única es cómoda y falsa — Reason enseñó que los accidentes son alineaciones de agujeros en muchas lonchas, y buscar «LA causa» suele terminar en la última loncha, que es donde estaba el humano. La pregunta guía: ¿qué condiciones hicieron que las acciones de cada cual *tuvieran sentido en su momento*?
4. **Lo que funcionó.** Safety-II en el documento: el protocolo de papel de Rosa, la guardia que escaló bien, el runbook que sí existía. Se refuerza lo que se nombra.
5. **Acciones**, cada una con dueño, fecha y — esto falta siempre — **tipo**: parche puntual, cambio de defensa, o cambio de política. Un postmortem cuyas acciones son todas parches puntuales no aprendió nada del sistema.
6. **Difusión**: quién debe leer esto y cómo sabremos que lo leyó.

Regla de oro transversal: **cero nombres propios en el cuerpo** (roles, no personas: «la guardia», «quien aprobó») — con la excepción inteligente que usó Aurelia: los agradecimientos, que sí llevan nombres.

## 2. El lenguaje contrafactual: la trampa que arruina postmortems buenos

Hay una familia de frases que convierte cualquier análisis en juicio disimulado, y conviene aprender a detectarla al oído:

- *«Debería haber comprobado…»*, *«¿por qué no miró…?»*, *«bastaba con…»*, *«era obvio que…»*

Todas comparten estructura: comparan lo que alguien hizo con lo que **el narrador, sabiendo ya el final**, habría hecho. Es el **sesgo retrospectivo** (*hindsight bias*) institucionalizado: una vez conocido el desenlace, el camino hacia él parece haber estado señalizado — pero quien decidía a la 1:40 no vivía en tu presente, vivía en su niebla. El lenguaje contrafactual no produce información (describe un universo que no ocurrió) y sí produce defensividad (es feedback al yo con sintaxis de análisis). La sustitución sistemática: cambiar «¿por qué no X?» por **«¿qué hacía que Y pareciera lo correcto?»** — que es la única pregunta cuya respuesta describe el sistema real. Facilitar un postmortem es, en buena parte, cazar contrafactuales al vuelo y reformularlos.

## 3. La segunda víctima

El término viene de la medicina (Albert Wu lo acuñó en 2000 para los clínicos involucrados en errores con daño): el profesional que estuvo en el extremo del incidente sufre su propio proceso — culpa, vergüenza, rumiación, miedo, a veces abandono de la profesión. El mensaje de Marc («si hay que rodar una cabeza que sea la mía, pero que sea rápido») es de manual. Lo que la organización haga en las 48 horas siguientes marca la diferencia:

- **Nombrarlo pronto y en privado**: «esto le pasa a cualquiera que estuviera en tu silla con tu cadena; no estás solo en esto» — dicho por alguien con autoridad, antes del postmortem.
- **No apartarlo del análisis**: la tentación protectora («tómate unos días, ya lo vemos nosotros») lo confirma como culpable ante sí mismo; su relato de primera mano es además el dato más valioso del análisis.
- **Cerrar el ciclo en público**: la línea cero de Víctor en la pared hizo por Marc más que cualquier conversación privada — reasignó la causalidad delante de todos los que importaban.

Una cultura que cuida a sus segundas víctimas no es blanda: está protegiendo su cadena de suministro de verdad. La gente que ha visto a la organización triturar a un compañero tras un incidente reporta menos, para siempre. Es el termómetro de Edmondson con memoria larga.

## 4. Difusión: el postmortem como activo (y el caso de enviárselo al cliente)

El instinto corporativo trata el postmortem como material radiactivo: circulación mínima, legal revisando adjetivos. El coste de ese instinto es que cada equipo aprende solo de sus propios incidentes — un desperdicio directo del activo más caro que produce una organización (sus fallos ya pagados). Las prácticas que multiplican el retorno: repositorio interno de postmortems buscable; lectura de los mejores en onboarding (enseñan el sistema real mejor que cualquier wiki); y revisión periódica de patrones transversales (¿cuántos incidentes de este año tienen «excepción bajo presión» en su cronología?).

¿Y enviarlo al cliente, como hizo Aurelia con Ondara? No es tan radical como parece: es práctica establecida de los buenos proveedores de infraestructura (los public postmortems de los grandes proveedores cloud son género propio) y la lógica la dio Encarna: la confianza que sobrevive a los incidentes no es la que ignora qué hay detrás, sino la que lo conoce. Condiciones para que funcione: el informe debe ser el de verdad (un postmortem-nota-de-prensa se detecta a la legua y destruye lo que pretendía construir), la cronología debe demostrar comprensión profunda, y las acciones deben ser verificables desde fuera. La respuesta de Rosa — «ahora sé qué mirar cuando algo falle, y sé que me lo contaréis» — es la definición operativa de la confianza recalibrada.

## 5. El fusible, con números

El «presupuesto de error» de Aurelia merece verse con cifras porque es el mecanismo anti-normalización más elegante que existe. Se acuerda de antemano: *toleramos hasta un 8% de despliegues con remedio (change failure rate) en ventana móvil de un mes; si se supera, el ritmo baja automáticamente — se pausan los despliegues nocturnos y el 20% de la capacidad va a estabilidad — hasta volver bajo el umbral.* Lo elegante:

- **Despersonaliza el conflicto eterno** velocidad-contra-prudencia: nadie tiene que ganar la discusión de «hay que frenar» contra la demo del viernes — el fusible salta solo, como se acordó en frío.
- **Invierte la normalización de la desviación**: en lugar de que cada violación del margen cree un margen nuevo (deriva), cada violación activa una corrección (homeostasis). Es el termostato de la sección 6 aplicado al riesgo.
- **Hace visible el precio del crunch antes del incidente**: la quincena de Albor habría fundido el fusible el miércoles 8 — cinco días antes de la 1:40 — con una conversación de presupuesto en lugar de un domingo de guardia.

## Para profundizar

- Howie: The Post-Incident Guide (gratuita): https://howie-guide.pagerduty.com/
- Etsy Debriefing Facilitation Guide (repositorio abierto): https://github.com/etsy/DebriefingFacilitationGuide
- Wu, A. (2000). "Medical error: the second victim" — *BMJ* 320:726-727 (texto libre en PMC).
- SRE Workbook, capítulo ampliado de postmortems (gratuito): https://sre.google/workbook/postmortem-culture/
