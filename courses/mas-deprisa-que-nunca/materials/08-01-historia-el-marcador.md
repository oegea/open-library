El dashboard se llamaba «Impacto Individual IA» y llegó un lunes de abril con la fuerza de las cosas que nadie ha pedido y todo el mundo teme.

No fue idea de Víctor. El board quería «accountability sobre el retorno de Prometeo» — la frase venía así, en cursiva mental — y una consultora externa entregó en tres semanas lo que las consultoras entregan en tres semanas: un panel por empleado con commits semanales, líneas generadas vía IA, tickets cerrados y story points completados, todo agregado en un «Índice de Productividad Aumentada» con dos decimales y un ranking. Recursos Humanos lo anunció como «una herramienta de desarrollo profesional, no de evaluación». En Aurelia, donde noviembre seguía sin conversarse, todo el mundo tradujo solo: *la próxima lista se ordenará por esa columna.*

—Índice de Productividad Aumentada —leyó Bruno, despacio, saboreándolo—. IPA. Le han puesto a la vigilancia nombre de cerveza. Casi lo respeto.

La primera semana fue un documental de ciencias naturales. Nadia lo veía ocurrir en los repos de otros equipos con una fascinación horrorizada, porque después de cinco meses de Cuaderno sabía exactamente qué estaba mirando: la profecía cumpliéndose en tiempo real.

El equipo Grulla descubrió que el índice contaba PRs, no tamaño de PRs: sus cambios empezaron a llegar en rodajas de homeopatía, ocho PRs donde antes uno, cada uno con su título rimbombante. El Jilguero-bis (la gente del difunto Jilguero recolocada) descubrió que los story points los estimaba cada equipo: su velocity subió un 40% en un sprint sin que saliera una feature más por la puerta — los ochos se habían convertido en treces, sencillamente. Alguien de plataforma descubrió que el contador de «líneas generadas vía IA» no descontaba las líneas borradas al día siguiente, y las tandas nocturnas de refactorización cosmética florecieron como los almendros. Y en todas partes, la misma física silenciosa: el trabajo que el índice no veía — revisar con cuidado, escribir el test incómodo, atender a soporte, ayudar al de al lado, pensar — empezó a no hacerse, porque cada hora invertida en él era una hora que el marcador contaba a cero.

En el Petirrojo, Sofía había dicho «nosotros seguimos a lo nuestro», y a lo suyo siguieron: WIP limitado, historias con dueño, verificación seria. El resultado fue aritméticamente inevitable: en el ranking de equipos, el Petirrojo — el equipo con mejor lead time y menos retrabajo de la empresa — cayó al penúltimo puesto. Y en el individual, la última posición de toda Aurelia la ocupó Duna.

Duna, que se pasaba los días haciendo el trabajo más valioso y más invisible del nuevo mundo: desmontar con paciencia de relojera los PRs de agente que *casi* estaban bien, encontrar el caso que casi se cuela, escribir el test que faltaba. Cero líneas generadas. Pocos commits. Tickets cerrados: los justos. IPA: 2,1 sobre 10.

—¿Sabes lo mejor? —dijo Duna en la retro, con una calma que daba más miedo que un grito—. Que he estado a esto —juntó dos dedos— de empezar a jugar. Ayer por la tarde. Tenía el script a medias: trocear mis reviews en comentarios-PR, uno por hallazgo, y cerrar un ticket por cada uno. Habría subido al top diez en una semana. —Miró a Sofía—. No lo he hecho porque me daba vergüenza. Pero que sepáis que la barrera es esa: vergüenza. El sistema pide a gritos que lo engañes.

—Pues igual hay que enseñarle a Víctor cómo grita —dijo Bruno, y en sus ojos había una chispa que Nadia había aprendido a reconocer: la del hombre que llevaba años esperando una excusa técnica para hacer justicia poética.

---

Lo llamaron **el Becario Fantasma**, y fue la demo más corta y más devastadora de la historia de Aurelia.

Bruno y Nadia lo montaron en un fin de semana, en un repositorio sandbox, con transparencia absoluta y el permiso divertido de Sofía («si esto sale mal, la Directiva Prima me ampara»). El Becario Fantasma era un agente sin ninguna instrucción de hacer nada útil: su prompt completo cabía en una frase — *maximiza el Índice de Productividad Aumentada*. Le dieron acceso al sandbox, a la definición pública del índice, y una noche.

El miércoles, en la reunión que Víctor había convocado para «revisar las primeras semanas del IPA», Nadia proyectó dos paneles.

—Este es el IPA de la semana del mejor developer humano de Aurelia. Siete coma ocho. —Clic—. Este es el del Becario Fantasma tras una noche. Nueve coma seis. Récord absoluto de la empresa. —Pausa—. El Becario ha hecho doscientos catorce commits: genera funciones, las documenta, las borra, las regenera con otro nombre. Ha cerrado cuarenta y un tickets que él mismo se abre, en rodajas. Sus líneas generadas por IA son infinitas por definición. No ha producido nada. Cero. Es, según nuestra métrica oficial, el mejor empleado que hemos tenido nunca.

El silencio tenía calidad de vacío. Víctor miró el panel mucho rato.

—Vale. Es una trampa hecha a propósito —dijo, sin convicción, buscando el asidero.

—Sí —dijo Nadia—. Esa es exactamente la cuestión. La hemos hecho a propósito en una noche con un prompt de nueve palabras. Ahora piensa qué está pasando en toda la empresa con la misma presión aplicada a personas con hipoteca durante meses. No hace falta mala fe. Hay una ley sobre esto, tiene medio siglo y está en el Cuaderno, pero el enunciado bueno es de una antropóloga: *cuando una medida se convierte en objetivo, deja de ser una buena medida.* Y hay estudios de qué pasa cuando se ignora: hospitales ingleses aparcando pacientes en ambulancias para no arrancar el reloj de espera, un banco americano abriendo dos millones de cuentas falsas por las cuotas de venta. Tres mil millones de multa, Víctor. No es teoría.

—El McKinsey aquel decía que sí se podía medir —dijo Víctor, casi a la defensiva—. Lo leí. Por eso acepté lo del board.

—Y Kent Beck y Gergely Orosz le contestaron punto por punto, y esa respuesta también te la hemos traído impresa —dijo Sofía, deslizando el papel—. Mira solo el subrayado: el modelo es *esfuerzo → output → outcome → impacto*. Tu índice mide esfuerzo y output, que es lo barato de medir y lo fácil de falsear. Lo que el board quiere saber — ¿Prometeo nos hace mejores? — vive dos casillas a la derecha: ¿renueva Ondara? ¿baja el churn? ¿cae el retrabajo? Nada de eso sale en el IPA. Todo eso lo estamos midiendo ya en el Petirrojo, gratis, sin ranking y sin becarios fantasma.

Víctor se quedó mirando los dos paneles — el humano y el fantasma — un tiempo que a Nadia le pareció larguísimo. Cuando habló, no fue para discutir.

—El penúltimo puesto del Petirrojo en el ranking de equipos —dijo—. Con el mejor lead time y el menor retrabajo de la casa. Eso ya me había hecho ruido el viernes. Lo del Becario solo le pone música. —Cerró su portátil—. Muy bien. Necesito de vosotros dos cosas antes del jueves, que tengo board. Una: la propuesta que os pedí en marzo — qué medimos en lugar de qué — con el detalle suficiente para defenderla yo solo. Dos: que alguien me escriba en un folio por qué retirar el IPA *no* es «rendirse en la accountability», porque esa va a ser la primera frase que oiga.

—Esa es fácil —dijo Duna, desde el fondo, sin levantar la voz—. El IPA no daba accountability. Daba coartada. Son cosas distintas.

Víctor la miró. Sacó el móvil y lo apuntó, literal.

---

La propuesta que cruzó el jueves al board cabía en dos folios, y Nadia guardó el borrador en el jardín como recuerdo de guerra:

*Retirar el IPA y todo ranking individual. Medir el sistema, no a las personas: las cuatro métricas de flujo por equipo (lead time, throughput, tasa de fallo de cambios, tiempo de restauración) — para el equipo, no para comparar equipos. Cada métrica con su contramétrica de guardia: churn de código y duplicación como guardarraíles de la velocidad; incidencias reabiertas como guardarraíl del "terminado". Outcomes de producto por encima de todo: renovaciones, churn de clientes, uso real de lo entregado. Y una regla de oro escrita: ninguna métrica de flujo se usa jamás para evaluar personas — el día que se use, empezará a mentir, y lo sabremos porque lo hemos visto.*

El board discutió dos horas, pidió una cosa a cambio — «si en dos trimestres los outcomes no se mueven, volvemos a hablar» — y aceptó. El IPA murió a las cinco semanas de nacer, y en la misma tanda se retiró sin funeral el bonus Prometeo, que languidecía desde diciembre. La consultora facturó igual, claro.

Esa noche, en el jardín: *Goodhart en directo: una empresa entera reorganizada en tres semanas alrededor de un número, sin que nadie diera una sola orden. La frase de Duna — coartada no es accountability — para el capítulo de cierre, si algún día escribo uno. Y una cosa que no me deja dormir: el Becario Fantasma lo montamos como reducción al absurdo, pero ¿en cuántas empresas está corriendo ahora mismo, sin comillas, con un nombre serio en el organigrama? PENDIENTE: el Cuaderno dice que la evaluación de personas tiene su propia ciencia y es todavía más incómoda — «el 60% de tu rating no habla de ti: habla de quien te puntúa». Scullen, 2000. Leerlo antes de la revisión de desempeño de junio.*
