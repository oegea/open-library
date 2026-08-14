La teoría te dio el agente con SDK. Esta ampliación quita la última capa: qué viaja *de verdad* por el cable cuando tu bucle habla con el modelo. No es masoquismo — es la vacuna definitiva contra la magia, y de paso la explicación de por qué cambiar de proveedor de modelos (sección 8) es tan barato cuando has hecho los deberes. Diez minutos de HTTP crudo, y ya nadie podrá venderte niebla sobre agentes nunca más.

## Lo que el SDK envía por ti

Cada vuelta del bucle es una petición HTTP POST normal y corriente. Con `curl`, la primera llamada de nuestro agente es literalmente esta:

```bash
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-5",
    "max_tokens": 16000,
    "tools": [
      {"name": "leer_sensor",
       "description": "Devuelve las últimas medidas de un sensor.",
       "input_schema": {"type": "object",
                        "properties": {"sensor_id": {"type": "string"}},
                        "required": ["sensor_id"]}}
    ],
    "messages": [
      {"role": "user",
       "content": "Investiga si hay anomalías de caudal en el sector 7."}
    ]
  }'
```

Y la respuesta, cuando el modelo decide usar la herramienta, es un JSON con esta forma (abreviado):

```json
{
  "stop_reason": "tool_use",
  "content": [
    {"type": "text", "text": "Voy a consultar el caudalímetro del sector 7."},
    {"type": "tool_use", "id": "toolu_01ABC...",
     "name": "leer_sensor", "input": {"sensor_id": "caudal-s7"}}
  ]
}
```

Detente en lo que estás viendo, porque es la desmitificación completa: la «decisión» del agente de usar una herramienta es **un trozo de JSON en una respuesta HTTP**. El modelo no ha ejecutado nada, no ha tocado nada, no *puede* tocar nada: ha emitido una petición estructurada, y punto. La siguiente llamada de tu bucle reenvía la conversación con dos añadidos — la respuesta del modelo tal cual, y un bloque tuyo con el resultado:

```json
{"role": "user", "content": [
  {"type": "tool_result", "tool_use_id": "toolu_01ABC...",
   "content": "[12.1, 11.9, 55.0, 54.2, 12.3]"}
]}
```

Eso es todo el misterio del tool use: dos formas de bloque JSON (`tool_use` de ida, `tool_result` de vuelta) y la disciplina de reenviar el historial completo. El SDK de la teoría te ahorra el `curl`, los reintentos ante errores de red y la deserialización — conveniencia real, cero magia añadida. Y los ayudantes de más alto nivel (el *tool runner* del SDK, al que le das funciones anotadas y te escribe el bucle entero) son la tercera capa de la misma cebolla: útil en producción, idéntica por dentro.

## La consecuencia de soberanía

Ahora la observación que conecta con la sección 8: mira cuánto de tu agente es *tuyo*. El bucle: tuyo. Las herramientas: tuyas. Los esquemas: JSON Schema estándar. Lo único específico del proveedor es la forma exacta del endpoint y de los bloques — y todas las API de modelos serios (OpenAI, Google, los servidores de modelos abiertos como vLLM u Ollama) ofrecen el mismo concepto con nombres ligeramente distintos: una petición con herramientas declaradas, una respuesta con llamadas estructuradas, un bloque de resultado. Cambiar tu agente de proveedor es escribir un adaptador de treinta líneas — o usar una capa tipo LiteLLM que ya los tiene escritos. Cuando en el capítulo 8 Vega migra de proveedor en doce días, esta ampliación es la razón técnica de que fuera posible: su bucle nunca dependió de nada que no fuera este contrato mínimo.

## Tres mejoras de veinte líneas (hazlas)

El agente de la teoría es deliberadamente desnudo. Estas tres mejoras son el puente hacia la sección 5, y caben en una tarde:

**1. La esclusa.** Un permiso por herramienta, y confirmación humana para lo que escribe:

```python
POLITICA = {
    "listar_sensores": "auto",
    "leer_sensor": "auto",
    "escribir_diagnostico": "confirmar",
}

def ejecutar_con_politica(nombre, args):
    if POLITICA.get(nombre, "denegar") == "confirmar":
        if input(f"¿Ejecutar {nombre}({args})? [s/N] ").lower() != "s":
            return "el operador ha denegado la ejecución"
    elif POLITICA.get(nombre, "denegar") == "denegar":
        return f"herramienta {nombre} no permitida por política"
    return HERRAMIENTAS[nombre](**args)
```

Fíjate en el detalle importante: la denegación **se le devuelve al modelo como resultado**, y el agente sigue trabajando con ese conocimiento («el operador ha denegado…») en vez de romperse. Acabas de implementar, en diez líneas, el corazón de una política de permisos — la idea que en la próxima sección verás convertida en ley de una casa entera: «Ejecutar, lo listado».

**2. El registro.** Cada petición del modelo y cada resultado, a un fichero JSONL con marca de tiempo. Veinte líneas, y tienes la trazabilidad completa que Corvus vendía en el plan Enterprise. Cuando algo vaya raro dentro de un mes, ese fichero será tu cronología del capítulo 2.

**3. El presupuesto.** Un contador de vueltas y un tope (`if vuelta > 15: abortar con resumen`). Los agentes reales pueden entrar en bucles improductivos — releer lo mismo, intentar variantes de un camino muerto — y un tope convierte «se ha quedado pensando toda la noche» en «ha parado en la vuelta 15 y me ha contado hasta dónde llegó». Los arneses comerciales lo llaman límites de presupuesto; tú lo llamas un `if`.

Con las tres puestas, vuelve a mirar tu bucle: jaula aún no tiene (eso es un contenedor, sección 5), pero ya tiene permisos, ventana y freno. Has recorrido, en pequeño, el mismo camino que Vega — y esa es exactamente la intención.

## Para llevar

- El tool use es JSON sobre HTTP: el modelo emite peticiones estructuradas (`tool_use`), tu código ejecuta y responde (`tool_result`). Verlo crudo una vez inmuniza contra todo el marketing posterior.
- El SDK y el tool runner son capas de conveniencia sobre ese contrato — útiles, y huecas de magia. Elige capa según convenga; entiende siempre la de abajo.
- Como el contrato es mínimo y casi universal, tu bucle es portable entre proveedores por construcción. La soberanía de la sección 8 empieza aquí.
- Permisos, registro y presupuesto caben en sesenta líneas en total. La distancia entre el juguete y un arnés serio es ingeniería incremental, no un salto cualitativo — hazla con tus manos y la sección 5 te parecerá un lunes cualquiera.
