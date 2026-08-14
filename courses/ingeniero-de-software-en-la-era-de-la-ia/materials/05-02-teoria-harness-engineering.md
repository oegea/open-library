Tomás lo entendió a la primera porque llevaba treinta años haciéndolo con otro nombre: jaulas, finales de carrera, setas de emergencia, registros. Esta teoría le pone el nombre nuevo a esa tradición vieja, la ordena en piezas, y — requisito innegociable de este curso — te deja ficheros reales para que al terminar puedas montar tu propio arnés, en Claude Code o en cualquier otra herramienta.

## Qué es el arnés, exactamente

La definición más limpia la dejó el ensayo que acuñó el término **harness engineering** — *The Anatomy of an Agent Harness* (Trivedy, blog de LangChain, marzo de 2026) —, traducción propia:

> «Un arnés es cada pieza de código, configuración y lógica de ejecución que no es el modelo en sí.»

Todo: el bucle, las herramientas y sus permisos, el entorno donde se ejecuta, los ficheros de contexto, las comprobaciones automáticas, los registros. Cuando usas Claude Code, Codex o cualquier agente comercial, estás usando un modelo *más* un arnés que alguien diseñó — y la mayoría de las diferencias que notas entre herramientas «con el mismo modelo debajo» son diferencias de arnés. De ahí la fórmula de Addy Osmani (ingeniero de Google, en su ensayo *Agent Harness Engineering*, 2026), traducción propia: «un modelo decente con un gran arnés supera a un gran modelo con un mal arnés». Es la lección del capítulo 5 en una frase: el Autopilot y la Cuadrilla podían llevar el mismo modelo dentro; los separaba la casa construida alrededor.

Dos ideas más completan el marco teórico. Birgitta Böckeler (Thoughtworks, en martinfowler.com) describe el arnés como un sistema de **guías y sensores** — piezas que encauzan lo que el agente puede hacer y piezas que le informan (y te informan) de cómo va — y advierte de que un buen arnés «no debería aspirar necesariamente a eliminar la aportación humana, sino a dirigirla adonde más importa» (traducción propia). Y el equipo de Anthropic, en sus notas sobre diseño de arneses (2026), deja las dos frases más citables de la disciplina, traducción propia: «cada componente de un arnés codifica una suposición sobre lo que el modelo no puede hacer por sí solo», y — contra la idea de que esto es un apaño temporal — «el espacio de combinaciones interesantes de arnés no se encoge a medida que los modelos mejoran. Se mueve». Los modelos de 2026 necesitan menos arnés para lo que los de 2024 hacían mal, y lo necesitan para cosas nuevas que en 2024 ni se intentaban. El arnés no es un andamio que se retira: es la parte del edificio que sigues poseyendo cuando cambias de inquilino.

Vamos con las cuatro piezas que montó Vega, que son las cuatro de cualquier arnés serio.

## Pieza 1: la jaula (entorno de ejecución)

Un agente ejecuta comandos; los comandos tienen consecuencias; luego la primera decisión es *dónde* ejecuta. La respuesta de Tomás — contenedor desechable, copia del repositorio, sin credenciales de producción, red cortada salvo lista blanca — es el patrón estándar, y no es paranoia: es la constatación de que un agente equivocado (o manipulado: sección 9) con acceso a tu máquina real es un incidente, y el mismo agente en un contenedor es una anécdota. Los agentes comerciales lo traen de serie en distintos grados: Codex ejecuta en sandbox sin acceso a red por defecto; Claude Code pide confirmación para comandos según configuración y soporta contenedores de desarrollo. El principio de ingeniería subyacente tiene cuarenta años: **minimizar el radio de la explosión**. Que fallar sea barato — porque va a fallar, igual que tus tests fallan: para eso están. La versión artesanal de Tomás («si algo huele raro, se tira el contenedor entero») es literalmente infraestructura inmutable aplicada a agentes.

## Pieza 2: los permisos

La discusión Bruno–Tomás del capítulo es la discusión que deberías tener en tu equipo, y conviene robarle la conclusión formulada por Nadia:

**Leer, casi todo. Proponer, todo. Ejecutar, lo listado. Mergear, jamás.**

Es el **principio de mínimo privilegio** — cada actor con los permisos mínimos para su función, doctrina de seguridad desde los años setenta — aplicado a un actor nuevo. Fíjate en la asimetría deliberada: leer y proponer son baratos y reversibles, así que se dan generosamente (un agente que no puede leer no puede ayudar, y una propuesta no ejecutada no rompe nada); ejecutar se da por lista blanca (tests, linter, build: cosas cuya peor consecuencia es un fallo en un contenedor); y las acciones irreversibles hacia el exterior — mergear, desplegar, publicar — quedan estructuralmente fuera, no prohibidas por una instrucción en un prompt (que el modelo podría ignorar o ser inducido a ignorar) sino **ausentes del mundo del agente**: la Cuadrilla no tiene el botón de merge, como la caldera de Tomás no tenía cable hacia la puerta del taller. La diferencia entre «le he dicho que no lo haga» y «no puede hacerlo» es toda la diferencia, y el error exacto de Élia con Corvus fue aceptar la primera creyendo tener la segunda. En la práctica, cada herramienta lo expresa a su manera — Claude Code con reglas de permisos (allow/ask/deny) por herramienta y comando, hooks que interceptan acciones, y modos de sandbox; Codex con niveles de aprobación y sandboxing por sistema operativo —, pero la política es tuya y anterior a la herramienta: decide primero el «leer/proponer/ejecutar/jamás» de tu equipo y luego tradúcelo a la configuración de turno.

## Pieza 3: el contexto operativo — AGENTS.md, y cómo escribir uno bueno

La tercera pieza es un fichero de texto en la raíz del repositorio, y es la más barata y la más rentable de las cuatro. **AGENTS.md** es un formato abierto y deliberadamente simple — «un README para agentes», lo describe su especificación (agents.md; el formato, nacido del ecosistema de OpenAI y otros, está hoy bajo una fundación de la Linux Foundation y lo usan decenas de miles de proyectos) — donde el equipo escribe lo que un agente necesita saber para trabajar en esa casa: cómo se compila, cómo se prueban las cosas, qué convenciones rigen, qué está prohibido tocar. Es Markdown normal, sin esquema obligatorio: su única magia es que las herramientas compatibles (Codex, OpenCode, goose, Aider, y Claude Code vía el enlace que veremos) lo leen automáticamente al empezar a trabajar.

La pregunta importante no es el formato sino el contenido, y aquí la regla de oro sale directa de la sección 3: **el AGENTS.md existe para el contexto que no se puede deducir del código** — la teoría, no la sombra. Un agente ya sabe leer tu `package.json`; lo que no puede saber es que las horas del planificador son horas de acequia. Con ese criterio, esto incluye un AGENTS.md bueno:

- **Comandos exactos**: cómo ejecutar los tests (¿toda la suite o hay una rápida?), el linter, el build, el entorno local. Literales, copiables.
- **Convenciones del equipo que el código no evidencia**: estilo de commits, dónde van los tests, qué se considera «hecho».
- **Las vallas de Chesterton señalizadas**: los acuerdos del mundo real que el código encarna y que un cambio «técnicamente correcto» podría destruir. La entrada más valiosa del fichero de Vega es una línea: *las horas del planificador son horas de acequia y no se normalizan jamás* — con enlace al documento que lo explica.
- **Los límites**: qué no se toca sin abrir discusión, qué directorios son generados, qué es legacy congelado.

Y esto lo excluye: todo lo que el agente puede deducir solo (la estructura de carpetas, qué framework usas), la prosa motivacional («escribe código limpio y mantenible» — no aporta ni un bit de información), y los tutoriales de las herramientas que el agente ya conoce. El antipatrón dominante es el **fichero hinchado**, y no es una cuestión estética: la propia documentación de Claude Code lo dice sin rodeos — «Bloated CLAUDE.md files cause Claude to ignore your actual instructions!» («¡Los ficheros CLAUDE.md hinchados hacen que Claude ignore tus instrucciones reales!»). Es el context rot de la sección anterior aplicado a tu propio fichero: cada línea de paja le roba atención a las líneas que importan. La disciplina correcta es la de un buen README: corto, denso, y podado cada vez que crece.

Dos detalles operativos que un senior debe conocer. Primero, la **resolución por cercanía** en monorepos: puede haber varios AGENTS.md (raíz, y otro en `apps/movil/`, por ejemplo), y la regla estándar es que gana el más cercano al fichero que se está editando — el contexto específico manda sobre el general — mientras que lo que el humano pida explícitamente en la conversación manda sobre todo. Segundo, el **enlace desde Claude Code**: Claude Code lee su propio fichero, `CLAUDE.md`, no AGENTS.md. Su documentación oficial da la solución canónica para no duplicar: si tu repositorio ya usa AGENTS.md, crea un CLAUDE.md que lo importe con la sintaxis de importación `@`:

```markdown
@AGENTS.md
```

Un CLAUDE.md de una línea. El contenido vive una sola vez, en el formato estándar, y cada herramienta lo encuentra por su puerta. Esa línea minúscula es una decisión de soberanía (sección 8): tu contexto operativo en un formato que ningún proveedor posee.

Y aquí, el ejemplo completo prometido — el AGENTS.md de Vega en su versión final, la del cierre de la historia (alguna de estas líneas nace en capítulos que aún no has leído; te sonarán al llegar), abreviado pero real en estructura, para que tengas una plantilla honesta:

```markdown
# Azud — guía para agentes

Plataforma de riego para comunidades de regantes. El código toca válvulas
reales: el agua perdida no tiene rollback. En la duda, propón y pregunta.

## Comandos
- Tests rápidos: `make test-fast` (~40 s; ejecútalos tras cada cambio)
- Suite completa + simulador: `make test-all` (~6 min; antes de proponer PR)
- Linter y tipos: `make lint` — el CI rechaza cualquier aviso
- Entorno local con datos sintéticos: `make dev`

## Reglas de la casa (no negociables)
- Las horas del planificador son "horas de acequia" (ancladas al sol), NO
  horas civiles. Jamás normalizar a UTC. Contexto: docs/hora-de-acequia.md
  y el acta de 1974 que ese documento cita.
- Los tests de válvulas SIEMPRE contra el simulador (`make sim`), nunca
  contra hardware. Sin excepciones.
- Todo cambio en drivers de hardware exige un test que reproduzca el fallo
  (lo comprueba el CI: check `driver-regression`).
- `report_utils.py` es legacy en extinción (ver ADR-001): no añadir código
  nuevo ahí; la funcionalidad nueva va a `informes_v2/`.

## Convenciones
- Commits: convencionales (`fix:`, `feat:`, `docs:`); una idea por PR.
- Los tests viven junto al código (`foo.py` → `foo_test.py`).
- El módulo de informes tiene 3 consumidores externos no visibles en el
  código: docs/consumidores-informes.md antes de tocar su salida.

## Qué no hacer sin abrir discusión
- Tocar `schedule_offsets.py`, migraciones de BD, o cualquier cosa bajo
  `facturacion/`.
```

Fíjate en lo que este fichero es: la teoría de Naur, destilada y versionada. Cada línea responde a la pregunta «¿qué necesitaría saber un compañero nuevo — de carne o de silicio — para no romper esta casa?». Si tu equipo escribe hoy este fichero, habrá mejorado su onboarding humano aunque no use un solo agente. Que es exactamente lo que descubrió Élia: «ha tenido que venir una máquina a leernos para que documentemos la casa».

## Pieza 4: los sentidos (feedback loops)

Un agente sin comprobaciones automáticas trabaja a ciegas y — peor — te convierte a ti en su única comprobación. La documentación de buenas prácticas de Claude Code lo formula con precisión quirúrgica, traducción propia: «sin una comprobación que pueda ejecutar, "parece terminado" es la única señal disponible, y tú te conviertes en el bucle de verificación». Los **feedback loops** — tests, linter, comprobador de tipos, compilador, el simulador de la red de riego — son los sentidos del agente: en cada vuelta del bucle le dicen si su último paso acercó o alejó del objetivo, y le permiten corregirse solo, que es la diferencia entre un agente útil y uno que produce plausibilidades. La inversión más rentable en cualquier arnés es mejorar estos sentidos: hacerlos **rápidos** (un test de seis minutos dentro de un bucle que itera veinte veces es media hora de espera; la suite rápida de 40 segundos de Vega existe por esto) y **honestos**. Y aquí la historia del curso se cierra sobre sí misma: un test flaky siempre fue una molestia, pero dentro de un arnés es *un sentido que miente* — y un agente, que a diferencia de un humano no acumula la sospecha de «este test falla a veces, reejecuta», actúa sobre la mentira con total confianza. El 14 de marzo empezó exactamente así: un sentido que mentía y una máquina que le creyó. Si tu suite tiene tests intermitentes, arreglarlos ya no es higiene: es requisito de habilitación agéntica. Lo mismo vale para los tipos estáticos, el linter estricto, los contratos de API: toda esa infraestructura «pesada» que el desarrollo rápido consideraba opcional se revaloriza, porque cada una es un sentido más con el que tu agente puede notar sus propios errores. La tradición entera de la ingeniería de calidad — CI, bancos de pruebas, los treinta años de Tomás — resulta ser la mitad del arnés que estos sistemas necesitaban.

## La regla del reparto: lo determinista no se le pide al agente

Hay un principio de diseño que atraviesa las cuatro piezas y que merece nombre propio, porque es el que separa los arneses bien pensados de los prompts kilométricos: **todo lo que pueda ser determinista, se hace determinista — y se saca del bucle del agente.** Antes de añadir una instrucción al contexto («ejecuta siempre los tests antes de proponer», «no dejes secretos en el código», «revisa las dependencias»), hazte la pregunta: ¿esto lo puede imponer un mecanismo que se ejecute *siempre*? Si la respuesta es sí — un git hook que corre la suite en cada commit, un check de CI que bloquea el push sin revisión, un escáner de secretos, un auditor de dependencias vulnerables, un analizador estático — entonces ahí es donde vive, y no en la prosa.

Las razones son tres, y las tres son de ingeniero. **Fiabilidad**: la instrucción en el prompt se cumple probabilísticamente (el modelo puede no recordarla, malinterpretarla o ser inducido a saltársela); el hook se ejecuta siempre, por construcción — el no determinismo es exactamente la puerta que no quieres dejar abierta en una barrera. **Coste**: cada cosa que el agente tiene que «pensar» son vueltas de bucle — tokens, latencia, contexto ocupado; un hook es gratis y no gasta atención. Y **universalidad**, que es el win-win que se suele pasar por alto: el git hook y el check de CI también se ejecutan cuando el *humano* hace cambios a mano — la misma barrera protege contra el agente descuidado, el junior con prisa y el senior con exceso de confianza, sin duplicar nada. El botón de merge inexistente, el check de test de regresión que frenó a la Cuadrilla, la lista blanca de red: todas las barreras que funcionan en esta historia son deterministas.

Lo que queda para el agente es, precisamente, lo que no se puede hacer determinista: el juicio. Y entre ambos mundos está el patrón más fértil de todos, el **híbrido**: la herramienta determinista *detecta* y el agente *interpreta y repara*. El auditor de dependencias — que existía mucho antes de la IA — encuentra tres vulnerabilidades y su salida entra como contexto del agente, que planifica la actualización evaluando roturas; el escáner de secretos bloquea el commit y el agente entiende el porqué y corrige; el linter marca y el agente arregla en la misma vuelta. Los sentidos del arnés son deterministas por diseño; el operario del bucle aporta lo que los sentidos no tienen: criterio. Fíjate en lo que acabamos de describir: no es una técnica nueva — es exactamente lo que siempre hicimos (automatizar lo automatizable, reservar el juicio humano para lo que lo exige), amplificado, con un actor más al que las mismas barreras de siempre le aplican igual de bien.

## Portabilidad: el arnés como capa tuya

Cierre con la vista puesta en la sección 8. De las cuatro piezas, ¿cuáles pertenecen a un proveedor? Ninguna. La jaula es un contenedor estándar; la política de permisos es una decisión de equipo expresable en cualquier herramienta; AGENTS.md es un formato abierto que leen Codex, OpenCode, goose y Aider directamente y Claude Code vía `@AGENTS.md`; los sentidos son tu CI de siempre. Las herramientas concretas añaden valor encima (y sus extras — hooks, subagentes, skills — los veremos en la sección 7), pero el arnés esencial es **tuyo**: cambiar de agente debería costarte una tarde de configuración, no una migración. Diseñarlo así, deliberadamente, es la diferencia entre usar herramientas y pertenecerles — que es la lección que a Vega le costó un almendral aprender.

## Para llevar

- El arnés es todo lo que no es el modelo: entorno, permisos, contexto, sentidos. «Un modelo decente con un gran arnés supera a un gran modelo con un mal arnés» (Osmani) — y el arnés, a diferencia del modelo, se posee.
- Jaula: entorno desechable, sin credenciales, red mínima. Que fallar sea barato.
- Permisos: leer casi todo, proponer todo, ejecutar lo listado, mergear jamás. Lo irreversible se hace estructuralmente imposible, no prohibido por prompt.
- AGENTS.md: la teoría que el código no evidencia, en comandos literales y vallas señalizadas. Corto y denso — el fichero hinchado hace que se ignoren tus instrucciones reales. En Claude Code, `CLAUDE.md` = `@AGENTS.md`, y el contenido vive una sola vez.
- Feedback loops rápidos y honestos: sin ellos, tú eres el bucle de verificación. Un test flaky es un sentido que miente; arreglarlo es requisito, no higiene.
- La regla del reparto: lo determinista, a hooks y checks estándar que se ejecutan siempre — para agentes y para humanos por igual —; el juicio, al agente; y en medio, el patrón híbrido: la herramienta determinista detecta, el agente interpreta y repara. Es lo de siempre, amplificado.
- Cada componente del arnés codifica una suposición sobre lo que el modelo no puede hacer solo — y ese espacio no se encoge con modelos mejores: se mueve (Anthropic).

## Para profundizar

- Trivedy, *The Anatomy of an Agent Harness* (blog de LangChain, 2026) — el ensayo que acuñó el término; buen mapa de piezas.
- A. Osmani, *Agent Harness Engineering* (addyosmani.com, 2026) — práctico y con criterio de trinchera.
- B. Böckeler, *Harness Engineering — first thoughts* (martinfowler.com, 2026) — guías y sensores; a dónde dirigir la aportación humana.
- Documentación de buenas prácticas de Claude Code (code.claude.com/docs) — permisos, CLAUDE.md, gestión de contexto; casi todo traduce a cualquier agente.
- agents.md — la especificación del formato, con ejemplos reales de proyectos grandes.
- Ejercicio: escribe el AGENTS.md de tu proyecto actual usando la plantilla de esta sección. Máximo una página. Enseñárselo a un compañero nuevo y ver qué pregunta es el mejor test de calidad que existe.
