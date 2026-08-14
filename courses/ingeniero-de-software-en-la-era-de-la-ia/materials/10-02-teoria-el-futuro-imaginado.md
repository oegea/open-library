En la acequia, Élia puso la regla antes de que empezara el juego: «todo lo que se diga a partir de este momento es imaginación». Esta teoría juega con la misma regla, dicha aquí con la solemnidad de un contrato: **lo que sigue mezcla hechos verificables de hoy con extrapolación, y cada vez que crucemos la frontera lo diremos explícitamente.** Un curso que ha exigido rigor durante diez secciones no va a abandonarlo en la última — pero tampoco va a privarte de lo que el prompt de cualquier buen ingeniero incluye: mirar hacia dónde apunta la curva. Versión deliberadamente optimista, porque el pesimismo ya tiene demasiados portavoces y porque el optimismo, en tecnología, es una profecía que ayuda a autocumplirse bien.

## El presente, para anclar (esto no es imaginación)

Hechos a fecha de este curso. Los agentes de código son herramienta cotidiana y las plataformas empujan hacia su multiplicación: GitHub ha lanzado su centro de mando para gestionar múltiples agentes de distintos proveedores desde un mismo panel; Google ha entrado con su propio entorno agent-first; Anthropic ha publicado tanto las capacidades de equipos de agentes como las guías de arneses de larga duración que viste en la sección 7; y el ecosistema abierto (sección 8) garantiza que nada de esto sea monocultivo. Los estándares de portabilidad (MCP, AGENTS.md) tienen gobernanza neutral. Y la evidencia sobre productividad sigue siendo la matizada que viste en la sección 2 — amplificador, no varita. Ese es el suelo. Ahora, el juego.

## La escalera (aquí empieza la imaginación)

La extrapolación más citada del sector es la de Steve Yegge (*Revenge of the Junior Developer*, 2025, escrito con décadas de Google y Amazon a la espalda), que describe la progresión como olas: del autocompletado al chat, del chat a los agentes, de los agentes a los **clusters** de agentes, y de ahí a las **flotas** — enjambres supervisados donde el ingeniero ya no conversa con un agente sino que *opera un sistema de agentes*, con paneles, colas de trabajo y presupuestos. Sus escritos posteriores imaginan esa capa de orquestación con todo el color del mundo; tómalo como lo toma él mismo: provocación informada, no hoja de ruta. La versión sobria de la misma escalera es la de Nadia en la acequia, y conviene subirla peldaño a peldaño señalando qué se conserva en cada salto, porque ahí está la sustancia del curso:

- **Del prompt al agente** (esto ya pasó): el criterio se movió de «qué escribo» a «qué contexto, herramientas y verificación le doy» — las secciones 4 a 6.
- **Del agente a la cuadrilla** (esto está pasando): el criterio se mueve al diseño del flujo — qué se paraleliza, qué se verifica contra qué, dónde van las esclusas humanas. El writer/reviewer y el loop engineering de la sección 7 son los primeros ladrillos.
- **De la cuadrilla a la flota** (imaginación a partir de aquí): si la curva sigue, el trabajo diario de un ingeniero de producto podría parecerse menos a una sesión de edición y más a la sala de control de Tomás: umbrales, alarmas, presupuestos, y la pregunta permanente de qué merece atención humana. **Ingeniería de sistemas de agentes**: fiabilidad, observabilidad, colas, economía de recursos — todo el manual de sistemas distribuidos, aplicado a trabajadores no deterministas. Si esta imaginación acierta, los ingenieros mejor posicionados serán los que sepan de *sistemas*, no los que memorizaran sintaxis — que es, nótese, la apuesta que este curso lleva haciendo desde la sección 1.
- **El peldaño especulativo final**: flotas que mantienen software cuya teoría vive, escrita y versionada, en el repositorio mismo — AGENTS.md, ADRs, evals como definición ejecutable de «bien» — con humanos poseyendo esa teoría y firmando. Si te suena, es porque es el mapa de la pared de Vega, extrapolado. La imaginación honesta rara vez inventa: alarga.

Andrej Karpathy — a quien esta era le debe medio vocabulario — ofrece las dos varas de medir para este tránsito: su **autonomy slider** (la autonomía como dial continuo que se gira tarea a tarea según riesgo y verificabilidad, no como interruptor), y su insistencia en que esta será una «década de agentes» — progresión larga, no acontecimiento — donde la distinción que importa es la que él mismo traza entre vibe coding y **agentic engineering**: delegar la escritura sin delegar el criterio. Y de su ensayo de 2026, la frase que resume las secciones 2 y 3 de este curso mejor que nosotros (traducción propia): «puedes externalizar tu pensamiento, pero no puedes externalizar tu comprensión» — y su corolario: «el programador es, cada vez más, no solo un escritor de código, sino un orquestador de agentes».

## El ingeniero de producto

Queda el desplazamiento del propio rol, y este medio-peldaño está ya medio ocurrido, así que crucemos la frontera con cuidado. Hecho observable: en los equipos que trabajan agent-first, el reparto del tiempo del ingeniero ya ha cambiado — menos teclear, más decidir qué construir, especificar, revisar, verificar y hablar con el dominio. Extrapolación razonable: si el coste de *escribir* código sigue cayendo hacia cero, el valor se concentra íntegramente en lo que Brooks llamó lo esencial (sección 1) — decidir qué debe hacer el sistema, comprobar que lo hace y responder de ello. A ese perfil el sector lo llama **ingeniero de producto** (*product engineer*): alguien que entiende el negocio lo bastante para decidir, la ingeniería lo bastante para poseer la teoría, y las herramientas lo bastante para orquestar su construcción. Este curso se preguntó al diseñarse si debía llamarse así — «el ingeniero de producto en la era de la IA» — y la respuesta fue que no, y la razón es la historia entera de Vega: el giro hacia el producto solo funciona *sobre* la base de ingeniería. Élia decidiendo qué construir vale porque puede bajar a la sala de máquinas; Nadia orquestando la Cuadrilla vale porque escribió un agente con sus manos y sabe qué hay dentro. El ingeniero de producto no es un ingeniero que dejó de serlo: es un ingeniero al que la automatización le liberó las manos para subir donde siempre debió estar. Quien intente el atajo — producto sin ingeniería, orquestación sin comprensión — descubrirá la fuga de la abstracción el peor día posible, con un almendral de por medio.

## La vertiente optimista, dicha sin rubor

Marcado como opinión esperanzada, que es la especie más honesta de imaginación. Primero: **crear nunca fue tan accesible** — la distancia entre «tengo una idea que ayudaría a mi comunidad de regantes» y «existe y funciona» se ha desplomado, y eso significa software para caber en mercados diminutos, para asociaciones, para el problema hiperlocal que jamás habría justificado un equipo — un Azud para cada acequia del mundo. Segundo: **el trabajo que se automatiza primero es el que menos echaremos de menos** — el boilerplate, la migración mecánica, el CRUD número mil — y lo que queda en el lado humano es la parte noble: entender problemas, diseñar sistemas, poseer teorías, responder. Tercero: **el conocimiento profundo se revaloriza** — contra la intuición del pánico, esta ola paga mejor que nunca entender los sistemas por dentro, y un junior con curiosidad y las herramientas de hoy puede construirse una comprensión que antes exigía una década de acceso privilegiado: las cajas están más abiertas que nunca para quien decida mirar dentro. Y cuarto, el optimismo de Paca, que no es tecnológico: las herramientas pasan, y cada una trae a sus vendedores de pánico y a sus vendedores de humo; el oficio — estar cuando hay que estar, saber lo que hay que saber, responder de lo que se firma — sigue ahí, bajando cuando le toca, como el agua. Este curso apuesta a que la generación que aprenda ambas cosas — las herramientas nuevas y el oficio viejo — hará con ellas cosas que nosotros no sabemos imaginar. Esa ignorancia también hay que marcarla, y es la mejor noticia de esta sección.

## Cómo seguir formándote (esto vuelve a ser real, y es un regalo)

Lo prometido: el material bueno, sin morralla, ordenado por lo que construye. Todo abierto o de acceso libre legítimo.

**Los cimientos (el criterio que no caduca):**
- Naur, *Programming as Theory Building* (1985) — si solo relees una cosa de este curso, que sea esta.
- Bainbridge, *Ironies of Automation* (1983) — cinco páginas que explican 2026.
- Brooks, *No Silver Bullet* (1986) — esencia y accidente; releer con cada ola.
- El informe OTAN de 1968 (archivo de Brian Randell) — el acta fundacional; se lee sorprendentemente bien.
- El Código Ético de la ACM — media hora, obligatoria.

**La práctica de hoy (las manos):**
- Anthropic, *Building Effective Agents* + las guías de context engineering y arneses de larga duración (anthropic.com/engineering) — el canon técnico de agentes.
- La documentación de buenas prácticas de Claude Code (code.claude.com/docs) — el flujo completo; traduce bien a Codex y OpenCode.
- Hamel Husain, *Your AI Product Needs Evals* (hamel.dev) — la disciplina de evaluación.
- Para el oficio de escribir prompts — que sigue siendo la mitad del contexto: la guía y el tutorial interactivo de Anthropic (platform.claude.com y github.com/anthropics/prompt-eng-interactive-tutorial), y la *Prompt Engineering Guide* de DAIR.AI (promptingguide.ai), con su sección adversarial para saber también cómo se ataca lo que escribes.
- Simon Willison (simonwillison.net) — el registro más riguroso y continuo de esta era: seguridad, herramientas, criterio. Suscríbete.
- Mitchell Hashimoto, *My AI Adoption Journey* (mitchellh.com) — el camino completo de un practicante serio, por etapas.
- 12-Factor Agents (Dex Horthy, GitHub) — la doctrina de posesión, factor a factor.

**Los vigías (para no perderte las olas siguientes):**
- Los ensayos de Karpathy (karpathy.bearblog.dev) y de Yegge (sourcegraph.com y su blog) — los dos extremos del telescopio: el matiz y la provocación.
- Las notas de ingeniería de Anthropic, OpenAI y Google — el estado del arte, de primera mano, gratis.
- OWASP GenAI (genai.owasp.org) — la seguridad, actualizada anualmente.

**Y el método para usar todo lo anterior**, que es lo único que de verdad te pedimos retener: el cuaderno de asombros. Apunta lo que no entiendas, con fecha. Ve a mirar dentro. El primer asombro es gratis y ya lo conoces: no sabes cómo funciona lo que usas todos los días. La diferencia entera del oficio — hoy, y en cualquiera de los futuros que esta sección imaginó — está entre los que se lo perdonan y los que van a mirar.

## Para llevar

- Separar hechos de imaginación es una destreza profesional; este capítulo la practicó marcando cada frontera. Exígele lo mismo a todo lo que leas sobre el futuro.
- La escalera plausible: prompt → agente → cuadrilla → flota → ingeniería de sistemas de agentes. En cada peldaño el criterio no desaparece: sube — de escribir, a dar contexto, a diseñar flujos, a operar sistemas.
- La autonomía es un dial, no un interruptor (Karpathy): se gradúa por tarea, según riesgo y verificabilidad. Y será una década, no un acontecimiento.
- El ingeniero de producto es el destino probable del rol — y solo funciona sobre base de ingeniería: puedes externalizar el pensamiento, no la comprensión.
- La versión optimista es defendible con argumentos: crear más accesible que nunca, lo automatizado es lo menos amado, el conocimiento profundo se revaloriza, y el oficio — el de Paca — no entiende de olas.
- El método permanente: cuaderno de asombros, y mirar dentro.

## Para profundizar

La sección entera de «cómo seguir formándote» es el para-profundizar de este capítulo — y la bibliografía completa del curso, con licencias, te espera en el cierre.
