La fecha del quince de marzo no fracasará por pereza del equipo ni por mala fe de Marga. Fracasará — con un 88% de probabilidad, según la curva de Nadia — por causas que llevan más de medio siglo documentadas: la naturaleza del software como actividad, y la naturaleza de la mente humana como estimadora. Esta sección recorre ambas, les pone números, y termina en una estación de esquí de Utah en febrero de 2001, donde diecisiete personas escribieron el documento que dio nombre a todo esto.

## 1968: la palabra provocadora

En octubre de 1968, en Garmisch (Alemania), el Comité de Ciencia de la OTAN reunió a medio centenar de los mejores informáticos del mundo en la primera **NATO Software Engineering Conference**. El informe (editado por Peter Naur y Brian Randell, 1969; el facsímil circula libremente) confiesa algo extraordinario en su primera sección:

> "The phrase 'software engineering' was deliberately chosen as being provocative, in implying the need for software manufacture to be based on the types of theoretical foundations and practical disciplines, that are traditional in the established branches of engineering."
> **[traducción propia]** «La expresión "ingeniería del software" se eligió deliberadamente por provocadora, al implicar la necesidad de que la fabricación de software se base en el tipo de fundamentos teóricos y disciplinas prácticas tradicionales en las ramas establecidas de la ingeniería.»

Es decir: el propio nombre de nuestra profesión nació como provocación — una aspiración, no una descripción. El contexto era lo que la época llamó la **crisis del software**: los sistemas ambicionados crecían más deprisa que la capacidad de construirlos; los proyectos se hundían en sobrecostes y retrasos. En 1968 la profesión ya sabía que algo en la metáfora de la fábrica no encajaba. Merece la pena retener esto cuando alguien presente el caos actual como una novedad de la era que sea: llevamos en crisis declarada desde antes de la llegada a la Luna.

## 1970: Royce, el paper que todos citan y casi nadie ha leído

Dos años después, **Winston W. Royce** publicó "Managing the Development of Large Software Systems" (*Proceedings, IEEE WESCON*, 1970), universalmente citado como el origen del modelo en **cascada** (*waterfall*): las fases secuenciales — requisitos, análisis, diseño, código, pruebas, operación — cada una terminada antes de empezar la siguiente. Lo que la cita universal omite es lo que el texto dice inmediatamente después de presentar ese diagrama:

> "I believe in this concept, but the implementation described above is risky and invites failure."
> **[traducción propia]** «Creo en este concepto, pero la implementación descrita arriba es arriesgada e invita al fracaso.»

Y el porqué, que Nadia reconoció como una descripción de Atlas: las pruebas llegan al final del ciclo, y ese es el primer momento en que los aspectos críticos del sistema **se experimentan en lugar de analizarse**. Si ahí falla algo de fondo, el proceso rebobina hasta el principio, y — cita textual — cabe esperar «hasta un 100% de sobrecoste en plazo y/o costes». Los remedios de Royce, con sus títulos literales, incluyen **"Do it twice"** («organiza las cosas para que la versión entregada al cliente sea en realidad la segunda», tras un piloto que enseñe lo que ningún plan contiene) e **"Involve the customer"** (implicar formalmente al cliente en puntos tempranos, antes de la entrega final). Iteración y feedback del cliente, en 1970, en el supuesto manifiesto del waterfall. Royce, por cierto, jamás usa la palabra «waterfall»: se la pusieron otros después.

La historia siguió su curso zigzagueante — **Barry Boehm** propuso en 1988 el **modelo en espiral** (*IEEE Computer*, 21(5)), ciclos guiados por riesgo con prototipos en cada vuelta, el puente formal entre el mundo planificado y el iterativo — pero la lección histórica ya está completa: **la iteración no fue una rebelión contra el saber establecido; era el saber establecido**, sepultado durante décadas bajo la comodidad administrativa del plan por fases. Cuando algo se cuenta como «antes reinaba el waterfall porque nadie sabía hacerlo mejor», ya sabes qué escalera aplicar.

## La falacia de planificación: tu cerebro es el primer proveedor de fechas falsas

Pasemos del software a la mente. En 1979, **Daniel Kahneman y Amos Tversky** acuñaron el término **planning fallacy** (falacia de planificación) en "Intuitive Prediction: Biases and Corrective Procedures": la tendencia sistemática a subestimar la duración de nuestras propias tareas, *incluso conociendo nuestro historial de retrasos*. El estudio emblemático es de **Buehler, Griffin y Ross (1994, *Journal of Personality and Social Psychology*, 67(3))**: pidieron a estudiantes predecir cuándo terminarían su tesina. Predicción media: **33,9 días**. Realidad media: **55,5 días**. Un 64% de desviación — entre personas que conocían perfectamente sus retrasos anteriores.

El mecanismo, demostrado en esos mismos experimentos, importa más que la cifra. Al estimar, construimos un **escenario** del plan — la **vista interna**: imagino los pasos, todo encaja, sumo — en lugar de consultar la **experiencia** — la **vista externa**: ¿cuánto duraron de verdad las últimas veinte cosas parecidas? Y cuando el historial nos contradice, lo descartamos con atribuciones («aquello se retrasó por causas excepcionales») — sin advertir que *siempre* hay causas excepcionales, solo que cada vez unas distintas. Bruno lo formuló mejor que el paper: lo que no está en la lista es lo que te mata, y no está en la lista precisamente porque nadie lo sabe todavía.

Añade una segunda capa, la **sobreprecisión** (*overprecision*): **Alpert y Raiffa** (trabajo de 1969, publicado en 1982 en la antología de Kahneman, Slovic y Tversky) pidieron intervalos de confianza del 98% — «da un rango que contenga el valor real con un 98% de seguridad» — y el valor real cayó fuera **alrededor del 40% de las veces** (debería ser el 2%). Réplicas posteriores (Moore y Healy, 2008, *Psychological Review*) confirman que la sobreprecisión es de los sesgos más robustos que existen. Traducción al oficio: hasta nuestros rangos son estrechos. Cuando un equipo dice «entre 4 y 6 semanas», la historia dirá a menudo 11.

**Estado de la evidencia: sólido.** La falacia de planificación es de lo mejor replicado en la literatura de juicio y decisión — laboratorio, campo y megaproyectos (la línea de Bent Flyvbjerg sobre infraestructuras documenta sobrecostes sistemáticos a escala de miles de proyectos).

## Lo que dicen los datos del software (y las cifras que hay que jubilar)

¿Y en software concretamente? La mejor evidencia disponible son los estudios del grupo de **Magne Jørgensen** (Simula Research Laboratory). Su revisión de encuestas (Moløkken y Jørgensen, 2003) converge en dos cifras: **el 60-80% de los proyectos sufre sobrecoste**, y el sobrecoste medio es del **30-40%**. Grave, pero notablemente menor que la cifra que quizá te suene: el 189% de sobrecoste medio del **CHAOS Report** del Standish Group. Jørgensen y Moløkken-Østvold analizaron esa cifra (2006, *Information and Software Technology*, 48(4)) y la encontraron incompatible con todos los demás estudios, con muestreo sesgado hacia proyectos fallidos y metodología no reproducible. El CHAOS Report es la fuente más citada de la industria y una de las menos fiables: si lo citas, cita también su crítica.

Segunda cifra a jubilar, esta con dolor porque es elegante: el **cono de incertidumbre** — ese diagrama según el cual la incertidumbre de la estimación se estrecha suavemente conforme avanza el proyecto (en la formulación canónica de Boehm y McConnell: ±4x al inicio, ±1,25x a mitad…). **Todd Little (2006, *IEEE Software*, 23(3))** lo contrastó con datos reales de 106 proyectos de su empresa: la precisión seguía una distribución **lognormal** (cola larga hacia el retraso: te puedes retrasar 3x, difícilmente adelantarte 3x) y **el rango relativo de incertidumbre no se estrechaba** a lo largo del proyecto. El cono no es una ley empírica; es, como mucho, el mejor caso alcanzable. Un dataset no cierra la cuestión — honestidad — pero no existe ningún dataset publicado que muestre el cono comportándose como promete.

## La vista externa, ejecutable

La corrección propuesta por Kahneman y Tversky en 1979 — **reference class forecasting**, pronóstico por clase de referencia — es exactamente lo que Nadia hizo: no preguntes a tu imaginación; pregunta a la distribución de resultados de proyectos similares. Y su versión potenciada es la simulación **Monte Carlo** sobre datos propios: en lugar de resumir tu historial en una media (que borra la información más importante: la variabilidad), lo usas entero.

La idea, en el Python que Nadia adaptó del Cuaderno:

```python
import random

# Ítems completados por semana, últimas 30 semanas REALES del equipo
# (solo trabajo verificado y en producción; la irregularidad es el dato)
historico = [9, 4, 11, 2, 7, 6, 13, 3, 8, 5, 10, 4, 6, 9, 1,
             7, 12, 5, 8, 3, 6, 10, 4, 7, 9, 2, 11, 6, 5, 8]

trabajo_restante = 74      # ítems conocidos hoy
descubrimiento = (0.25, 0.55)  # trabajo extra que históricamente aparece (25-55%)

def simular_una_vez():
    pendiente = trabajo_restante * (1 + random.uniform(*descubrimiento))
    semanas = 0
    while pendiente > 0:
        pendiente -= random.choice(historico)  # una semana futura = una semana pasada al azar
        semanas += 1
    return semanas

resultados = sorted(simular_una_vez() for _ in range(10_000))
for p in (50, 85, 95):
    print(f"Percentil {p}: {resultados[int(len(resultados) * p / 100)]} semanas")
```

Y el mismo núcleo en JavaScript, por si tu terminal habla Node:

```javascript
const historico = [9, 4, 11, 2, 7, 6, 13, 3, 8, 5, 10, 4, 6, 9, 1,
                   7, 12, 5, 8, 3, 6, 10, 4, 7, 9, 2, 11, 6, 5, 8];
const restante = 74, descubrimiento = [0.25, 0.55];

const simular = () => {
  let pendiente = restante * (1 + descubrimiento[0] +
    Math.random() * (descubrimiento[1] - descubrimiento[0]));
  let semanas = 0;
  while (pendiente > 0) {
    pendiente -= historico[Math.floor(Math.random() * historico.length)];
    semanas++;
  }
  return semanas;
};

const res = Array.from({ length: 10_000 }, simular).sort((a, b) => a - b);
[50, 85, 95].forEach(p => console.log(`P${p}: ${res[Math.floor(res.length * p / 100)]} semanas`));
```

Tres observaciones que convierten el juguete en herramienta:

1. **La salida es una curva, no un número.** «P50: 20 semanas, P85: 27» es una frase que negocio puede usar para decidir cuánto riesgo compra. «20 semanas» a secas es la falacia de planificación con corbata.
2. **El modelo es deliberadamente tonto.** No modela dependencias ni vacaciones ni cisnes: asume que tu futuro se parecerá a tu pasado, incluida la semana del incidente de agosto. Esa es su virtud — la vista interna «corregiría» esa semana mala, y por eso la vista interna falla.
3. **Es tan bueno como sus datos.** Necesita un historial de trabajo *real terminado* (no story points inflados — la sección 8 explica por qué se inflan) y trozos de tamaño más o menos comparable. Los equipos que trocean el trabajo en ítems pequeños y parecidos no lo hacen por liturgia: le están dando de comer a su clase de referencia.

## ¿Entonces nunca se puede planificar? El mapa de los dominios

Cuidado con el péndulo. La respuesta madura no es «planificar es inútil», sino «según para qué». Aquí es útil — como *mapa conceptual*, y lo marcamos con honestidad: framework de sensemaking publicado en *Harvard Business Review* (Snowden y Boone, 2007, "A Leader's Framework for Decision Making"), premiado y ampliamente usado, pero **sin validación empírica como teoría** — el marco **Cynefin**, que distingue entre problemas **claros** (la relación causa-efecto es evidente: aplica la buena práctica), **complicados** (causa-efecto existe pero requiere análisis experto: los expertos y los planes funcionan — un puente, una migración bien conocida), **complejos** (causa-efecto solo se entiende retrospectivamente: hay que sondear con experimentos seguros-de-fallar y responder a lo que emerja) y **caóticos** (actúa primero, estabiliza).

El desarrollo de producto nuevo — ¿qué necesitan de verdad las gobernantas de Ondara? ¿usará alguien Atlas? — es dominio complejo: ningún análisis previo sustituye al contacto con la realidad, porque la información necesaria *aún no existe*; se genera al construir y exponer. Instalar la versión 28 de algo instalado 27 veces es complicado: planifícalo con Gantt y te irá bien. El error de las organizaciones no es planificar; es aplicar la maquinaria del dominio complicado (fechas, fases, certezas) al dominio complejo — comprar certidumbre falsa en el único terreno donde no está en venta. La curva de Nadia no le dice a Marga «no habrá fecha»; le dice «esta es la fecha que los datos venden, y este es su precio en riesgo».

## 2001: Snowbird — qué es (y qué no es) el Manifiesto Ágil

Con todo lo anterior en la mano, la historia del manifiesto se entiende mejor que como suele contarse. Del **11 al 13 de febrero de 2001**, en el hotel The Lodge de la estación de esquí de Snowbird (Utah), se reunieron **diecisiete** practicantes — representantes de corrientes rivales entre sí: Extreme Programming, Scrum, DSDM, Adaptive Software Development, Crystal, Feature-Driven Development, Pragmatic Programming — convocados por Bob Martin tras un intento previo en Oregón (la crónica de primera mano es "History: The Agile Manifesto" de Jim Highsmith, en agilemanifesto.org; Alistair Cockburn confesó allí: «personalmente no esperaba que este grupo concreto de agilistas llegara a ponerse de acuerdo en nada sustantivo»). Se pusieron de acuerdo en 68 palabras:

> "Individuals and interactions over processes and tools / Working software over comprehensive documentation / Customer collaboration over contract negotiation / Responding to change over following a plan. That is, while there is value in the items on the right, we value the items on the left more."
> **[traducción propia]** «Individuos e interacciones sobre procesos y herramientas / Software funcionando sobre documentación exhaustiva / Colaboración con el cliente sobre negociación contractual / Respuesta al cambio sobre seguir un plan. Es decir: aunque hay valor en lo de la derecha, valoramos más lo de la izquierda.»

Más doce principios (agilemanifesto.org/principles.html) que conviene leer alguna vez enteros, porque contienen cosas que el «agile» corporativo olvidó — entregas frecuentes, conversación directa, **ritmo sostenible**, excelencia técnica, simplicidad, equipos autoorganizados, y la reflexión regular del equipo sobre su propia eficacia.

Tres precisiones que separan el documento de su leyenda:

1. **Es un armisticio, no un método.** Diecisiete rivales acordando valores comunes — deliberadamente por encima de sus diferencias de método. Todo lo que diga «el agile dice que hagas X ceremonia» está hablando de otra cosa.
2. **No cayó del cielo: cristalizó.** Cada pieza tiene genealogía — la iteración de Royce, el riesgo de Boehm, los equipos autónomos de Durham (sección 1), el desarrollo de producto japonés que veremos en la sección 3, y la experiencia acumulada de los noventa. La palabra «agile» fue la marca de una corriente de treinta años.
3. **Sus autores serían los primeros en aplicarle la navaja de Popper.** La frase final del texto de Highsmith advierte contra convertirlo en religión: el movimiento quería «devolverle credibilidad a la palabra metodología». Lo que pasó después — la industria de certificaciones, los rituales sin principios — enfureció a varios firmantes hasta el punto de renegar de la palabra. Esa historia, con citas, en la sección 12.

Y una curiosidad de licencias que anticipa un tema del curso: el manifiesto permite copiarse libremente, pero **solo íntegro y con su aviso** — sus autores intuyeron que el mayor riesgo del texto era ser citado a trozos convenientes. No les faltaba razón.

## Para llevar

- La profesión sabe que el software no se fabrica como un puente desde 1968; la iteración y el feedback temprano están en Royce (1970) — el paper del «waterfall» advierte contra el waterfall e incluye «do it twice» e «involve the customer».
- La falacia de planificación es robusta y universal: estimamos 34 y tardamos 55, incluso conociendo nuestro historial, porque usamos la vista interna (escenarios) en vez de la externa (distribuciones de casos pasados). Y nuestros rangos también son estrechos (overprecision: ~40% de fallos en intervalos «del 98%»).
- Datos reales de software: 60-80% de proyectos con sobrecoste, sobrecoste medio 30-40% (Jørgensen). El 189% del CHAOS Report y el cono de incertidumbre no superan el escrutinio: jubílalos.
- La alternativa honesta a la fecha-punto es la curva: reference class forecasting y Monte Carlo sobre el historial real del equipo. Compromete percentiles, no deseos.
- Planificar funciona en dominios claros y complicados; el desarrollo de producto nuevo es complejo: la información se genera construyendo y exponiendo, no analizando (Cynefin como mapa, no como ley).
- El Manifiesto Ágil (Snowbird, 2001) es un armisticio de valores entre corrientes rivales, la cristalización de treinta años de aprendizaje — no un método, y desde luego no un ritual.

## Para profundizar

- Informe NATO 1968 (Naur & Randell) — facsímil: https://www.scrummanager.com/files/nato1968e.pdf
- Royce, W. (1970). "Managing the Development of Large Software Systems" — facsímil: https://github.com/tpn/pdfs/blob/master/Managing%20the%20Development%20of%20Large%20Software%20Systems%20-%201970%20(waterfall).pdf
- Buehler, R., Griffin, D. & Ross, M. (1994). "Exploring the planning fallacy" — PDF: https://web.mit.edu/curhan/www/docs/Articles/biases/67_J_Personality_and_Social_Psychology_366,_1994.pdf
- Jørgensen, M. & Moløkken-Østvold, K. (2006). Crítica al CHAOS Report — PDF: https://web-backend.simula.no/sites/default/files/publications/Jorgensen.2006.4.pdf
- Flyvbjerg, B. (2022). "Top ten behavioral biases in project management" — arXiv: https://arxiv.org/abs/2202.00125
- Manifiesto Ágil, principios e historia: https://agilemanifesto.org/ · /principles.html · /history.html
- Snowden, D. & Boone, M. (2007). "A Leader's Framework for Decision Making", *HBR* — de pago; ficha: https://pubmed.ncbi.nlm.nih.gov/18159787/
