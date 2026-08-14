El correo, leído con café, era una obra maestra del género.

Empezaba celebrando «un año increíble de crecimiento conjunto». Anunciaba que Corvus había sido adquirida por Nordwind Cloud «para acelerar nuestra misión». Comunicaba «la evolución de nuestros planes hacia una estructura más simple»: el plan de Vega desaparecía —la palabra exacta era *sunset*, como si a los productos se les pusiera el sol— y su sustituto natural, el nuevo «Scale», costaba cuatro veces más. Los precios antiguos se mantendrían sesenta días. El párrafo final invitaba a «agendar una llamada con tu Customer Success Partner para diseñar juntos tu camino de migración».

—Cuatro veces —dijo Bruno—. Cuatro. Veces.

—Y fijaos qué elegancia —dijo Élia, con una calma que no presagiaba nada bueno para Corvus—: el plan que matan es exactamente el que nos deja usar sus modelos *sin* su Autopilot, sin su panel, sin su suite integrada. El plan de los que solo queremos la tubería. Se conoce que la tubería sola no fideliza.

Tomás removía el café con la parsimonia de quien ya ha visto esta película.

—En mi gremio esto tiene nombre desde hace cuarenta años —dijo—. Compras el autómata del fabricante X, y resulta que el software de programarlo solo funciona con la consola del fabricante X, que solo se conecta con el bus del fabricante X. Te regalan la entrada y te cobran la salida. —Dio un sorbo—. La pregunta no es si Corvus es mala gente. La pregunta es: ¿cuánto nos cuesta hoy irnos? Porque ese número, y no el precio del plan, es el que dice quién manda en esta relación.

Élia cogió un rotulador.

—Pues vamos a calcularlo. Ahora mismo. Inventario: ¿qué es exactamente lo que Corvus hace por nosotros a día de hoy?

Y ahí, delante de la pizarra, ocurrió la escena que un año antes habría sido imposible. Porque un año antes la respuesta habría sido «todo»: el Autopilot mantenía el repo, su panel era la memoria del equipo, sus flujos integrados llegaban hasta el despliegue, y nadie sabía dónde acababa Corvus y empezaba Vega. Ese era, de hecho, el diseño: la razón de que todo viniera «tan bien atado».

Pero después del riego fantasma, pieza a pieza, sin proponérselo del todo como estrategia, habían ido reconstruyendo la frontera. El arnés de la Cuadrilla era suyo, código abierto y código propio, en su repositorio. Los prompts estaban versionados en git, con su suite de evals: cuarenta y dos escenarios que definían, con independencia de qué modelo hubiera debajo, qué significaba que el parte de las siete estuviera *bien*. El contexto de la casa vivía en `AGENTS.md` y en los documentos de diseño — formato estándar, texto plano, legible por cualquier agente del mercado y por cualquier humano. Las herramientas que la Cuadrilla usaba para hablar con la telemetría y con el gestor de incidencias eran servidores MCP, un protocolo abierto que no pertenecía a ningún proveedor. Hasta la costumbre de leer los diffs enteros era, mirada así, una pieza de independencia: el conocimiento de lo que entraba en el repositorio estaba en el equipo, no en un panel ajeno.

Cuando terminaron el inventario, la columna «qué hace Corvus por nosotros» tenía exactamente dos líneas: *acceso a modelos* y *facturación unificada*.

Se quedaron mirándola en silencio. Fue Nadia la que se echó a reír primero.

—Somos idiotas —dijo—. Llevamos un año teniéndole miedo a esta empresa. Y es un *enchufe*. Un enchufe caro.

—Eh, un respeto a los enchufes —dijo Bruno—. Los enchufes son estándar. Esto era un enchufe con la forma de nuestra mano.

La migración la planificaron aquella misma mañana en media pizarra, y la palabra «pánico» no llegó a pronunciarse. Probaron el arnés contra dos proveedores de modelos distintos —uno grande, y un modelo de pesos abiertos servido en una máquina alquilada, para las tareas con datos sensibles de los regantes—. La suite de evals hizo exactamente el trabajo para el que había nacido: ejecutada contra cada candidato, midió qué se resentía y qué no, sin opiniones ni marketing. El parte de las siete salió igual de digno por tres tuberías distintas; el agente de diagnóstico perdió un poco de finura con el modelo abierto pequeño y la recuperó con el mediano. Dos tareas exigieron retocar prompts; los retoques pasaron por pull request, como todo, con sus checks en verde.

Doce días después del correo, Vega ejecutó el cambio: una mañana de trabajo, la mayor parte esperando a que las evals terminaran de dar fe. Por la tarde, la Cuadrilla entera corría sin una sola llamada a Corvus. Nadie de fuera notó nada. Esa era la gracia.

---

La llamada de despedida con Íker fue breve y, a su manera, instructiva.

Íker —que había sobrevivido a la adquisición con título nuevo y el mismo entusiasmo— no entendía la decisión, y su desconcierto era sincero, que era lo interesante. Ofreció descuentos. Ofreció «una sesión estratégica con nuestro equipo de arquitectura». Ofreció, ya con la puerta cerrándose, tres meses gratis del plan Scale «para que vierais todo el valor de la plataforma integrada».

—Íker —dijo Élia, sin acritud—, te voy a explicar por qué no hay negociación posible, porque creo que a tu empresa le vendría bien oírlo. No nos vamos por el precio. El precio ha sido solo el aviso. Nos vamos porque el año pasado descubrimos, de la peor manera posible, la diferencia entre dos tipos de dependencia. Hay dependencias que puedo *inspeccionar*: sé exactamente qué pasa por ellas, sé lo que me dan, y si mañana quiebran o se vuelven caras, las cambio, porque el acoplamiento está a la vista y cabe en una pizarra. Y hay dependencias que se ofrecen a hacérmelo todo, tan bien atado que mirar dentro es de mala educación. Vuestro producto es de las segundas por diseño. Cada función nueva que anunciáis ata un nudo más. —Hizo una pausa—. Cuando algo se acopla a todo de forma que no puedo inspeccionarlo, ya no es una herramienta que uso. Es una herramienta que me usa. Y con el agua de mis clientes, eso no puede volver a pasar.

Hubo un silencio al otro lado. Luego Íker, con la honestidad súbita de los comerciales a puerta ya perdida, dijo:

—¿Sabes lo que es curioso? Los clientes que mejor usan Corvus son siempre los más fáciles de retener. Y los que hacen… lo que habéis hecho vosotros… —buscó la palabra sin encontrarla— …esos no hay manera.

—Eso que no sabes nombrar —dijo Tomás, inclinándose hacia el altavoz— se llama ser dueño de tu flujo. Que vaya bien, chaval.

---

Aquella noche, la última entrada del cuaderno de asombros fue más larga que de costumbre.

*Día 212. Hoy hemos cambiado de proveedor de modelos como quien cambia de compañía eléctrica, y me he pasado el día pensando en por qué ha sido tan fácil, porque hace un año habría sido un incendio de seis meses.*

*No ha sido fácil por suerte. Ha sido fácil porque, sin darnos cuenta, todo lo que hemos construido desde marzo era una estrategia de salida: los prompts en git y no en un panel; las evals que definen «bien» con independencia del modelo; el contexto en ficheros estándar que lee cualquier agente; las herramientas detrás de un protocolo abierto; el arnés nuestro, con las piezas a la vista. Ninguna de esas cosas la hicimos «contra» Corvus. Las hicimos para entender nuestro propio sistema. Resulta que son la misma cosa: lo que puedes entender, lo puedes sustituir.*

*Tomás dice que la soberanía no es autarquía —seguimos alquilando los modelos, y bien alquilados están, son carísimos de hacer—. Es otra cosa: que ninguna pieza alquilada sea insustituible, y que el mapa de qué depende de qué esté en nuestra pizarra y no en el PowerPoint de un comercial. Élia lo ha dicho más corto: alquila caballos, no vendas el mapa.*

*P. D. Bruno ha propuesto enmarcar el correo del «sunset» y colgarlo al lado de la captura del check rojo. Aprobado por unanimidad. Nuestra pared empieza a parecer un museo de las cosas que casi nos comen.*

---

*En la teoría de esta sección: el lock-in como fenómeno de ingeniería y no de mala suerte — cómo medir el coste de salida de cada dependencia de tu flujo de IA; qué piezas conviene poseer (prompts, evals, contexto, arnés) y cuáles alquilar (modelos, infraestructura); los estándares abiertos que hacen posible cambiar de proveedor — AGENTS.md, MCP, APIs compatibles — y el estado real del ecosistema de modelos de pesos abiertos y agentes open source en 2026; y el criterio de Élia, formalizado: desconfía del acoplamiento que no puedes inspeccionar.*
