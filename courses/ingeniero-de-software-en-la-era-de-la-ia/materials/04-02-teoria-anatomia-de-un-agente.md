En el capítulo, Nadia desmonta la magia delante de todos: un bucle, tres herramientas, un print. Esta teoría es esa demostración por escrito, completa y ejecutable — al terminarla habrás construido tu primer agente y sabrás exactamente qué compró Élia cuando contrató a Corvus. Aquí empieza la parte más práctica del curso: a partir de esta sección, todo lo que leas lo puedes teclear.

## La definición sin niebla

Un **agente** es un programa que, en bucle, le pide a un modelo de lenguaje que decida el siguiente paso hacia un objetivo, ejecuta las **herramientas** que el modelo pide, y le devuelve los resultados para que decida el siguiente. Cuatro piezas, y solo cuatro:

1. **El modelo** — el LLM de la sección 2. Se accede por API; no vive en tu máquina, no recuerda nada entre llamadas.
2. **El bucle** — un `while` escrito por ti, en tu lenguaje favorito. Es código normal y corriente: tuyo, determinista, depurable.
3. **Las herramientas** — funciones tuyas que el modelo puede *pedir* que se ejecuten. El modelo nunca ejecuta nada: describe lo que quiere («llama a `leer_sensor` con `sector=7`») y **tu código decide si lo hace y lo hace**. Esta frontera es la frase más importante que dijo Nadia: *un agente puede exactamente lo que sus herramientas le permiten*.
4. **El contexto** — todo lo que el modelo ve en cada vuelta: la instrucción inicial, el historial de la conversación, los resultados de las herramientas. Como el modelo no tiene memoria, el bucle se lo reenvía todo, cada vez.

La mecánica de cada vuelta: mandas al modelo la conversación completa junto con la lista de herramientas disponibles (nombre, descripción y esquema de parámetros de cada una). El modelo responde una de dos cosas: «quiero usar tal herramienta con tales parámetros» (en la API, una respuesta con `stop_reason: "tool_use"`) o «he terminado, esta es mi respuesta». Si pide herramienta, la ejecutas, añades el resultado a la conversación, y vuelta a empezar. Eso es todo. Ahora escribámoslo.

## El agente mínimo, en Python

Completo y funcional contra la API de Anthropic (`pip install anthropic`, y una clave en la variable de entorno `ANTHROPIC_API_KEY`). Es, pieza por pieza, el agente de la demostración de Nadia: tres herramientas inofensivas sobre una copia de datos, y el print como ventana.

```python
import json
import anthropic

# ── Las herramientas: funciones normales. El agente puede ESTO y nada más. ──
SENSORES = {
    "caudal-s7": [12.1, 11.9, 55.0, 54.2, 12.3],   # sector 7: la anomalía
    "caudal-s6": [11.8, 12.0, 12.2, 11.9, 12.1],   # sector 6: normal
}

def listar_sensores():
    return json.dumps(list(SENSORES.keys()))

def leer_sensor(sensor_id: str):
    return json.dumps(SENSORES.get(sensor_id, "sensor desconocido"))

def escribir_diagnostico(texto: str):
    with open("diagnostico.txt", "w") as f:
        f.write(texto)
    return "diagnóstico guardado"

HERRAMIENTAS = {
    "listar_sensores": listar_sensores,
    "leer_sensor": leer_sensor,
    "escribir_diagnostico": escribir_diagnostico,
}

# ── Lo que el modelo ve de cada herramienta: nombre, descripción, esquema. ──
ESQUEMAS = [
    {"name": "listar_sensores", "description": "Lista los sensores disponibles.",
     "input_schema": {"type": "object", "properties": {}}},
    {"name": "leer_sensor", "description": "Devuelve las últimas medidas de un sensor.",
     "input_schema": {"type": "object",
                      "properties": {"sensor_id": {"type": "string"}},
                      "required": ["sensor_id"]}},
    {"name": "escribir_diagnostico", "description": "Guarda el diagnóstico final.",
     "input_schema": {"type": "object",
                      "properties": {"texto": {"type": "string"}},
                      "required": ["texto"]}},
]

# ── El bucle. Esto ES un agente. ──
client = anthropic.Anthropic()
conversacion = [{"role": "user", "content":
    "Investiga si hay anomalías de caudal y escribe un diagnóstico breve."}]

while True:
    respuesta = client.messages.create(
        model="claude-opus-5",
        max_tokens=16000,
        tools=ESQUEMAS,
        messages=conversacion,
    )
    conversacion.append({"role": "assistant", "content": respuesta.content})

    if respuesta.stop_reason != "tool_use":          # el modelo ha terminado
        print(next(b.text for b in respuesta.content if b.type == "text"))
        break

    resultados = []
    for bloque in respuesta.content:
        if bloque.type == "tool_use":
            print(f"[ventana] el modelo pide: {bloque.name}({bloque.input})")
            salida = HERRAMIENTAS[bloque.name](**bloque.input)
            resultados.append({"type": "tool_result",
                               "tool_use_id": bloque.id, "content": salida})
    conversacion.append({"role": "user", "content": resultados})
```

Léelo dos veces, porque es el programa más importante del curso. Fíjate en cuatro cosas. Primera: **el modelo nunca toca nada** — la línea que ejecuta de verdad es `HERRAMIENTAS[bloque.name](**bloque.input)`, y esa línea es tuya; podrías ponerle un `if` delante que pidiera confirmación, que comprobara permisos, que registrara en un log. Ese `if` que todavía no existe es la semilla de toda la sección 5. Segunda: la «ventana» de Corvus, la que costaba un plan Enterprise, aquí es un `print`. Tercera: el agente decide su propio camino — nadie le dijo que comparara el sector 7 con el 6; lo hará (o no, según la ejecución: recuerda el no determinismo) porque comparar es lo que el texto de un buen diagnóstico suele hacer. Y cuarta: cada vuelta reenvía `conversacion` entera — el contexto crece a cada paso, y eso tendrá consecuencias.

## El mismo agente en JavaScript

Para que veas que no hay nada específico de un lenguaje (`npm install @anthropic-ai/sdk`; se omiten las herramientas, idénticas en espíritu):

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const conversacion = [{ role: "user", content:
    "Investiga si hay anomalías de caudal y escribe un diagnóstico breve." }];

while (true) {
  const respuesta = await client.messages.create({
    model: "claude-opus-5",
    max_tokens: 16000,
    tools: ESQUEMAS,
    messages: conversacion,
  });
  conversacion.push({ role: "assistant", content: respuesta.content });

  if (respuesta.stop_reason !== "tool_use") {
    console.log(respuesta.content.find((b) => b.type === "text")?.text);
    break;
  }

  const resultados = [];
  for (const bloque of respuesta.content) {
    if (bloque.type === "tool_use") {
      console.log(`[ventana] el modelo pide: ${bloque.name}`, bloque.input);
      const salida = await HERRAMIENTAS[bloque.name](bloque.input);
      resultados.push({ type: "tool_result",
                        tool_use_id: bloque.id, content: salida });
    }
  }
  conversacion.push({ role: "user", content: resultados });
}
```

Dos apuntes de honestidad técnica. Uno: los SDK oficiales incluyen ayudantes que te escriben este bucle (en Python, un *tool runner* al que le pasas las funciones y listo) — en producción probablemente los uses; aquí lo escribimos a mano porque el objetivo es que no quede ni un centímetro de magia. Dos: los agentes comerciales (Claude Code, Codex, el Autopilot de Corvus) son este mismo bucle con muchísima más ingeniería alrededor — mejores herramientas, gestión del contexto, permisos, recuperación de errores. La diferencia, como dijo Nadia, no está en la inteligencia: está en todo lo demás. «Todo lo demás» tiene nombre, y es el título de la próxima sección.

## Workflows contra agentes: no todo debe ser un bucle libre

Ahora que sabes lo que es un agente, toca el criterio de cuándo usarlo — y la mejor fuente es el ensayo de Anthropic *Building Effective Agents* (diciembre de 2024), lectura obligada de esta sección. Su distinción central, traducción propia:

> Los **workflows** son «sistemas donde los LLM y las herramientas se orquestan mediante caminos de código predefinidos»; los **agentes** son «sistemas donde los LLM dirigen dinámicamente sus propios procesos y uso de herramientas».

En un workflow, *tú* decides los pasos y el modelo rellena cada uno; en un agente, el modelo decide los pasos. El parte diario para los regantes que conocerás en la sección 6 es un workflow: script que junta datos → una llamada al modelo → publicar; el camino es fijo y solo hay un paso de LLM. La investigación de la anomalía es un agente: nadie sabe de antemano cuántos sensores mirar. El ensayo cataloga cinco patrones de workflow que cubren muchísimo terreno antes de necesitar un agente — **encadenamiento de prompts** (la salida de una llamada alimenta la siguiente), **enrutado** (una llamada clasifica y despacha a flujos especializados), **paralelización** (varias llamadas a la vez, se agregan resultados), **orquestador-trabajadores** (una llamada trocea la tarea y reparte) y **evaluador-optimizador** (una llamada genera, otra critica, se itera) — y sobre todo deja el consejo que deberías tatuarte antes de montar nada: «Find the simplest solution possible, and only increase complexity when needed» — busca la solución más simple posible y añade complejidad solo cuando haga falta. Un agente es más flexible y, exactamente por eso, más caro, más lento y más impredecible que un workflow. La madurez en este oficio nuevo se parece sospechosamente a la de siempre: no usar la pieza potente donde bastaba la simple. El ensayo llama **augmented LLM** («LLM aumentado») al bloque de construcción común a todo — el modelo equipado con herramientas, recuperación de información y memoria — del que tanto workflows como agentes se componen.

## Context engineering: el recurso escaso no es la inteligencia

El bucle reenvía la conversación entera en cada vuelta. En nuestro juguete da igual; en un agente real que lee ficheros de dos mil líneas y ejecuta suites de tests, el contexto se convierte en el recurso crítico del sistema, y gestionarlo tiene ya nombre de disciplina: **context engineering** (ingeniería del contexto). Dos ideas de la guía de Anthropic sobre el tema (2025) que explican comportamientos que verás a diario. Primera, el **attention budget** (presupuesto de atención): la ventana de contexto no solo es finita — el rendimiento del modelo se degrada a medida que se llena, fenómeno conocido como **context rot**: a más tokens, menos precisión recuperando cualquiera de ellos. Un modelo con la ventana medio llena de volcados de logs irrelevantes razona peor sobre lo relevante. Segunda, el principio de diseño que se deriva, traducción propia: «encuentra el conjunto más pequeño posible de tokens de alta señal que maximice la probabilidad del resultado deseado». No «mete todo lo que tengas», sino lo contrario: cada token compite por atención con los demás. De ahí las técnicas que verás en las secciones 5 y 7 — resúmenes periódicos del historial (*compaction*), notas estructuradas que el agente escribe para sí mismo, subagentes con contextos limpios para tareas acotadas — y de ahí también una regla práctica inmediata: cuando tu asistente de código empiece a comportarse peor en una sesión larga, no es un misterio; es context rot, y la solución suele ser empezar sesión nueva con un resumen, no insistir. Y fíjate en la rima con la sección 2: el modelo solo sabe lo que hay en sus pesos o en su contexto. La ingeniería del contexto es, literalmente, la ingeniería de *qué sabe tu agente* — el AGENTS.md de la próxima sección no será más que la parte estable y versionada de esta disciplina.

## MCP: un enchufe estándar para las herramientas

Última pieza de vocabulario. En nuestro agente, las herramientas eran funciones locales, y para un agente que escribes tú, eso basta. Pero en cuanto varios agentes distintos (el tuyo, Claude Code, el de tu compañera) quieren usar las mismas capacidades (la telemetría de tu empresa, el gestor de incidencias, una base de datos), aparece el problema clásico de integración N×M: cada agente integrándose con cada sistema. El **Model Context Protocol (MCP)** es la solución estándar: un protocolo abierto (anunciado por Anthropic en noviembre de 2024, hoy gobernado por una fundación bajo la Linux Foundation, con miles de servidores publicados) por el que un **servidor MCP** expone herramientas, recursos y prompts de forma que *cualquier* cliente compatible puede usarlos. Está construido sobre JSON-RPC y declaradamente inspirado en el LSP, el protocolo que permitió que cualquier editor hablara con cualquier analizador de lenguaje — la misma jugada, ahora entre agentes y capacidades. Criterio de uso, sin fanatismo en ninguna dirección: **cuándo sí** — cuando una capacidad va a ser consumida por varios agentes o herramientas distintas, o cuando quieres poder cambiar de agente sin reescribir integraciones (nota la rima con la soberanía de la sección 8: un protocolo abierto entre tu agente y tus sistemas es un acoplamiento que puedes inspeccionar y sustituir). **Cuándo no** — para un agente único con tres funciones propias, como el nuestro: un servidor MCP ahí es pura ceremonia; empieza con funciones locales y extrae a MCP cuando la reutilización lo pida. Es, otra vez, un principio viejo con ropa nueva: no construyas la abstracción antes de tener el segundo consumidor.

## Para llevar

- Agente = modelo + bucle + herramientas + contexto. El bucle es un `while` tuyo; el modelo propone, tu código dispone. No hay más magia que esta.
- Un agente puede exactamente lo que sus herramientas le permiten. La seguridad y el control no se le piden al modelo: se construyen en la capa de herramientas y permisos — tema de la sección 5.
- La trazabilidad es trivial cuando el bucle es tuyo: un print. Desconfía de quien te la venda como función premium.
- Workflows (caminos fijos, tú decides los pasos) antes que agentes (el modelo decide): usa la solución más simple que funcione y sube de complejidad solo cuando haga falta (Anthropic, *Building Effective Agents*).
- El contexto es el recurso escaso: finito, degradable (context rot) y caro. Ingeniería del contexto = decidir qué sabe tu agente con el mínimo de tokens de alta señal.
- MCP estandariza la conexión agente↔herramientas (como el LSP estandarizó editor↔lenguaje): úsalo cuando haya reutilización o quieras portabilidad; para tres funciones locales, sobra.

## Para profundizar

- Anthropic, *Building Effective Agents* (anthropic.com/engineering, diciembre 2024) — el ensayo que ordenó el vocabulario del sector. Corto y con diagramas; léelo antes de montar nada.
- Anthropic, *Effective context engineering for AI agents* (anthropic.com/engineering, 2025) — attention budget, context rot y las técnicas de gestión de contexto.
- La documentación de tool use de la API de Claude (platform.claude.com/docs) — la referencia exacta de los bloques `tool_use`/`tool_result` que usa nuestro bucle; los conceptos son equivalentes en las API de otros proveedores.
- modelcontextprotocol.io — la especificación de MCP, con tutoriales para escribir tu primer servidor en unas decenas de líneas.
- Tu propio teclado: modifica el agente de esta sección. Añádele una cuarta herramienta, ponle un `if` de confirmación delante de `escribir_diagnostico`, haz que dos ejecuciones diverjan. Nada de lo que leas te enseñará más que eso.
