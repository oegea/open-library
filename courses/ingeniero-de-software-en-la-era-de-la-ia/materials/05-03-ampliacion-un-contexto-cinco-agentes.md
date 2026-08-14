La teoría te dejó un AGENTS.md completo y la promesa de que el arnés esencial es portable. Esta ampliación cobra la promesa: el mapa de dónde vive cada pieza del arnés en las cinco herramientas de agente más usadas, y los matices de escritura de AGENTS.md que separan un fichero correcto de uno excelente. Es la sección «esto no lo sabía» para quien ya usa una de estas herramientas a diario — y el seguro de vida para cuando cambie de ella.

## El mapa de portabilidad

La misma información — contexto del proyecto, preferencias personales, flujos del equipo, política de permisos — vive en sitios distintos según la herramienta. El mapa, a fecha de este curso (los detalles finos cambian con cada versión: verifica en la documentación de la tuya; lo estable es la estructura):

| Pieza | Claude Code | Codex CLI | OpenCode | goose | Aider |
|---|---|---|---|---|---|
| **Contexto de proyecto** | `CLAUDE.md` en la raíz (recomendado: una línea `@AGENTS.md`) | `AGENTS.md` nativo | `AGENTS.md` nativo | `AGENTS.md` / ficheros de hints según versión | Ficheros de convenciones (`CONVENTIONS.md` por costumbre) que apuntas por configuración — apuntar a `AGENTS.md` es una línea |
| **Contexto personal global** | `~/.claude/CLAUDE.md` | `~/.codex/` (config y guía global) | Config de usuario | Config de usuario | `~/.aider.conf.yml` |
| **Jerarquía / cercanía** | CLAUDE.md por directorio; el más específico complementa | AGENTS.md anidados; gana el más cercano al fichero editado | AGENTS.md anidados | Según versión | Por configuración |
| **Flujos empaquetados** | Comandos slash en `.claude/commands/`, skills | Prompts/plantillas propias | Comandos propios | Recetas/extensiones | Scripting externo |
| **Política de permisos** | `settings.json` (allow/ask/deny), hooks, sandbox | Niveles de aprobación + sandbox (sin red por defecto) | Configuración de permisos | Extensiones y config | Confirmaciones; tú controlas el git |
| **Herramientas externas** | MCP | MCP | MCP | MCP (proyecto fundacional de la misma fundación) | Menos integrado; enfoque CLI |

Tres lecturas de la tabla, de más obvia a más útil. Primera: **el contexto de proyecto converge en AGENTS.md** — cuatro de cinco herramientas lo leen nativamente o a una línea de configuración de distancia, y Claude Code a una línea de importación. Escribirlo bien una vez rinde en todas partes. Segunda: **MCP es la otra capa común** — tus servidores de herramientas funcionan con cualquiera de las cuatro que lo hablan. Tercera, y la que menos gente ha interiorizado: **la política de permisos es la pieza menos portable** — cada herramienta la expresa a su manera, y por eso el consejo de la teoría era escribir primero la política en humano («leer casi todo, proponer todo, ejecutar lo listado, mergear jamás») en tu propio AGENTS.md o documento de equipo, y *luego* traducirla a la sintaxis de cada herramienta. La política es tuya; las sintaxis, prestadas.

## Matices de AGENTS.md que no caben en un ejemplo

La teoría te dio el qué; estos son los ajustes finos que se aprenden con cicatrices:

**Escribe comandos, no descripciones de comandos.** «Ejecuta los tests con make» obliga al agente a adivinar el target; `make test-fast` se copia y ejecuta. La diferencia parece menor y no lo es: cada ambigüedad es una vuelta de bucle gastada en resolverla — o peor, resuelta mal.

**Di el porqué en una frase cuando la regla sea contraintuitiva.** «No normalizar a UTC» a secas es una orden que un razonamiento suficientemente seguro de sí mismo podría cuestionar; «no normalizar a UTC: son horas solares por el acuerdo de 1974 (ver docs/hora-de-acequia.md)» es una valla señalizada que convierte al agente en aliado de la regla. Regla sin porqué invita a la excepción; regla con porqué, a la consulta.

**Enlaza, no incrustes.** El acta de 1974 no va en el AGENTS.md: va enlazada. El fichero es un índice de alta señal, no una enciclopedia — el agente seguirá el enlace *cuando la tarea lo pida*, que es exactamente la economía de atención correcta (y la razón de ser de las skills, su versión empaquetada).

**Pódalo con el mismo ritual que las dependencias.** El AGENTS.md crece por sedimentación — cada incidente deja su línea — y nadie borra. Ponle revisión periódica: cada línea que el equipo ya no pueda justificar, fuera. Un fichero de contexto es un prompt permanente que pagas en cada sesión, en tokens y en atención; la teoría ya citó lo que pasa cuando engorda: el modelo empieza a ignorar tus instrucciones reales.

**Versiónalo con dueño.** Cambios por pull request, como el código — porque *es* código en el sentido que importa: modifica el comportamiento del sistema en producción (el sistema, aquí, incluye a tus agentes). El equipo que edita su AGENTS.md por consenso silencioso en el editor de cada uno redescubrirá el Google Doc de Bruno con otro nombre.

**Un truco de verificación** que vale por todos los consejos: pídele a tu agente, en un directorio limpio, que te explique cómo se trabaja en este repositorio usando solo el AGENTS.md. Lo que responda mal o no sepa responder es exactamente lo que falta o sobra en el fichero. Es la versión agéntica del test de Nadia con el compañero nuevo — y tarda dos minutos.

## El criterio de compra, ya que estamos

Esta tabla también sirve para elegir herramienta, y el criterio del curso a estas alturas no te sorprenderá: entre dos agentes comparables, prefiere el que lee formatos estándar, expone su política de permisos como configuración inspeccionable y habla MCP — no porque los demás sean malos, sino porque ese conserva tu libertad de cambiar de opinión. La herramienta es alquilada; el contexto, los flujos y la política son tuyos. Elige herramientas que respeten esa frontera, y la frontera te devolverá el favor el día del correo con «cambios importantes en tu plan».

## Para llevar

- AGENTS.md y MCP son las dos capas comunes del ecosistema; la política de permisos es la menos portable — escríbela primero en humano, tradúcela después a cada herramienta.
- Comandos literales, porqués de una frase en las reglas contraintuitivas, enlaces en vez de incrustaciones, poda periódica y cambios por PR: la diferencia entre un AGENTS.md correcto y uno excelente.
- Test de dos minutos: que el agente te explique el repositorio usando solo el fichero. Lo que falle es tu lista de tareas.
- Elige herramientas que lean estándares y expongan su política: son las que te dejan marcharte — y por eso mismo, las que menos motivos te darán para hacerlo.
