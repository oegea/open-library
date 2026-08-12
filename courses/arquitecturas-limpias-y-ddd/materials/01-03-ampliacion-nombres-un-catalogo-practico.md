La teoría dio los principios; esta ampliación es un catálogo de campo. Son los patrones y trampas de nomenclatura que más aparecen en revisiones de código reales, incluidos varios que los propios seniors suelen no haber formalizado nunca. Úsalo como referencia: no hace falta memorizarlo, hace falta saber que existe.

## Convenciones por lenguaje: respeta la casa

Cada lenguaje tiene convenciones asentadas, y seguirlas es parte de la legibilidad — un lector de Python espera `snake_case` y le frena encontrarse `camelCase`:

| | JavaScript | Python |
|---|---|---|
| variables y funciones | `camelCase` (`totalFactura`) | `snake_case` (`total_factura`) |
| clases | `PascalCase` (`LineaFactura`) | `PascalCase` (`LineaFactura`) |
| constantes verdaderas | `MAYUSCULAS` (`IVA_GENERAL`) | `MAYUSCULAS` (`IVA_GENERAL`) |
| «privado» por convención | `#campo` (privado real) o `_campo` | `_campo` (un guion bajo) |

La guía oficial de estilo de Python, **PEP 8**, es un documento abierto y breve que merece una lectura completa (peps.python.org/pep-0008). En JavaScript no hay guía oficial, pero las convenciones anteriores son universales en la práctica.

La regla que engloba a todas: **en caso de conflicto entre tu gusto y la convención del proyecto, gana el proyecto.** La consistencia local vale más que la elegancia personal, porque el lector calibra sus expectativas con el código circundante.

## Funciones: verbos que no mienten

- **Una función *hace*: nómbrala con un verbo.** `calcularTotal()`, `enviar_recordatorio()`. Un nombre sin verbo (`total()`, `factura()`) obliga al lector a adivinar si consulta o actúa.
- **Pares consulta/acción.** Una convención con pedigrí (Bertrand Meyer la formalizó como *Command-Query Separation*, CQS, en los años 80: una rutina o responde una pregunta o cambia el estado, nunca ambas): los nombres deben delatar el bando. `esValida()`, `tieneDescuento()`, `puedeFacturarse()` prometen no tocar nada; `emitir()`, `anular()`, `recalcular()` prometen efectos. La función `getCliente()` que crea clientes — el ejemplo de la teoría — es exactamente una violación de CQS disfrazada por el nombre.
- **Simetrías completas.** Si hay `abrir()` debe haber `cerrar()`, no `finalizar()`; si hay `add` debe haber `remove`, no `delete` en una clase y `remove` en la vecina. Las asimetrías obligan a consultar la documentación para cada pareja.
- **El test del «y».** Si el nombre honesto lleva conjunción — `validarYGuardar()` — no busques un nombre mejor: divide la función. El nombre era el diagnóstico, no el problema.

## Booleanos, colecciones y unidades

- **Booleanos como afirmaciones.** `esActivo`, `tiene_lineas`, `is_expired` — nombres que se leen como una frase que puede ser verdadera o falsa. Evita los negativos (`noEsValido`): la expresión `if (!noEsValido)` es un pequeño acertijo de lógica que nadie pidió.
- **Colecciones en plural o con sufijo explícito.** `facturas`, `lineasPendientes`. Una de las fuentes de bugs más tontas y frecuentes es la variable en singular que contiene una lista (`factura[3]`… ¿era una lista de facturas o una factura con índices?).
- **Las unidades, en el nombre o en el tipo.** `timeout` es una bomba: ¿segundos, milisegundos? `timeoutMs`, `plazo_dias`, `importe_centimos` desactivan la bomba gratis. (La NASA perdió la sonda Mars Climate Orbiter en 1999 por una confusión de unidades entre equipos — libras-fuerza frente a newtons; el informe oficial de la NASA lo documenta. En la sección 5 verás la solución de fondo: tipos que llevan su unidad, los *value objects*.)

## Trampas con solera

- **Nombres «Hungarian» fósiles.** Prefijos de tipo (`strNombre`, `intTotal`) tuvieron sentido en los 90 sin editores inteligentes; hoy solo añaden ruido y, peor, mienten cuando el tipo cambia y el prefijo no. (Curiosidad que pocos conocen: la *notación húngara original* de Charles Simonyi en Microsoft codificaba la *semántica*, no el tipo — `dx` para «diferencia de coordenadas», `us` para «cadena sin sanear» — y esa versión sí era útil; la copia degenerada que codificaba tipos es la que merece el descrédito. Joel Spolsky lo cuenta en su artículo abierto *Making Wrong Code Look Wrong*, 2005.)
- **El sufijo numérico.** `calc()` y `calc2()`, `facturacion.php` y `facturacion_v2.php`. Un número al final de un nombre es la confesión de que nadie supo decir *en qué se diferencian*. Si la diferencia es «la política de cálculo de antes y después de 2014», el nombre lo puede decir: `calcularConNormativaPre2014()`.
- **Palabras vacías.** `Manager`, `Processor`, `Handler`, `Util`, `data`, `info`, `aux`, `temp`: nombres que caben en cualquier cosa no describen ninguna. Casi siempre esconden o una responsabilidad sin identificar o un cajón de sastre. (Anticipo de la sección 6: en la arquitectura destino de este curso hay exactamente *una* palabra reservada para «cosa que habla con el exterior», y es `Repository`. Prohibir los sinónimos — `Manager`, `Client`, `Service`, `Connector` — no es capricho: garantiza que el lector reconozca el patrón a simple vista.)
- **Comentario-nombre desincronizados.** Cuando renombres, busca el nombre viejo en comentarios, docs y mensajes de log. Un log que dice `calculando con modo=7` cuando el código ya habla de `politicaRedondeo` reabre la brecha entre lo que se dice y lo que se hace.

## Renombrar con seguridad

Renombrar es el refactor más rentable por unidad de esfuerzo, y los entornos modernos lo hacen casi gratis:

- En **JavaScript/TypeScript**: cualquier editor con soporte de lenguaje (VS Code y equivalentes) renombra símbolos en todo el proyecto (*Rename Symbol*, F2 en VS Code). En TypeScript la garantía es fuerte; en JavaScript dinámico, revisa usos por cadena (`obj["nombre"]`), que el renombrado automático no ve.
- En **Python**: los IDEs (PyCharm, VS Code con Pylance) renombran con análisis estático; la misma advertencia con `getattr(obj, "nombre")` y usos dinámicos.
- En ambos: si el símbolo es público (una API que consumen otros), renombrar es un cambio de contrato, no un refactor — mantén un alias con aviso de obsolescencia durante una transición.

Y la advertencia que la historia hará carne en la próxima sección: en un sistema dinámico, sin tipos y sin tests — es decir, en el Monstruo — *ningún* renombrado automático es completamente de fiar. La red de seguridad va primero.

## Para llevar

- Sigue la convención del lenguaje y, sobre todo, la del proyecto: la consistencia es legibilidad.
- Funciones con verbo; consultas y acciones distinguibles por el nombre (CQS); si el nombre pide un «y», divide.
- Booleanos afirmativos, colecciones en plural, unidades en el nombre.
- Desconfía de sufijos numéricos, prefijos de tipo y palabras vacías (`Manager`, `aux`, `Util`): son síntomas, no estilos.
- Renombrar es el refactor más barato; hazlo con las herramientas del editor y con respeto a los usos dinámicos y a las APIs públicas.
