SOLID es el acrónimo famoso, pero no es ni el primero ni el único intento de sistematizar el buen diseño. Esta ampliación recorre tres cuerpos de ideas que lo complementan — y que en conversaciones de seniors marcan la diferencia entre recitar principios y entender diseño: la Ley de Deméter, *Tell, Don't Ask*, y los patrones GRASP. Cierra con la crítica honesta a SOLID, porque un principio que no puede criticarse no es un principio: es una liturgia.

## La Ley de Deméter: no hables con extraños

Formulada en 1987 en la Northeastern University (proyecto Demeter, de ahí el nombre — Deméter, diosa griega de la agricultura, porque el proyecto iba de «cultivar» software). Su forma práctica: un método solo debería hablar con sus **amigos inmediatos** — sus propios campos, sus parámetros, los objetos que él mismo crea — y no con **los amigos de sus amigos**.

El síntoma que caza es el «choque de trenes» (*train wreck*):

```javascript
// Choque de trenes: este código conoce TODA la cadena de estructuras internas
const cp = pedido.getCliente().getDireccion().getProvincia().getCodigoPostal();

// Deméter: pídeselo a tu amigo directo y que él se organice
const cp = pedido.codigoPostalDeEnvio();
```

¿Por qué importa? Acoplamiento estructural: la primera línea depende de *cuatro* formas de objetos; si mañana la dirección se normaliza en otra tabla, o el cliente pasa a tener varias direcciones, ese código — y los cuarenta sitios que repiten la cadena — se rompe. La segunda línea depende de *una* promesa. La Ley de Deméter es el DIP de andar por casa: cada punto de la cadena es un conocimiento que no te corresponde.

Matiz importante que evita fanatismos: la ley aplica a **objetos con comportamiento**, no a **estructuras de datos puras**. Encadenar sobre un JSON de configuración (`config.database.host`) o sobre una estructura inmutable no es un choque de trenes: ahí no hay comportamiento que encapsular. El criterio: si el objeto tiene reglas, no cruces su piel; si es un dato inerte, es solo un dato.

## Tell, Don't Ask: manda, no preguntes

Documentado por Andy Hunt y Dave Thomas (*The Pragmatic Programmer*, 1999) y por Martin Fowler en su bliki (entrada *TellDontAsk*, gratuita). La idea: en lugar de **preguntarle** a un objeto por su estado para decidir *tú* qué hacer con él, **dile** lo que quieres y que decida él, que para eso tiene los datos.

```python
# Ask: la lógica de la factura vive FUERA de la factura (y se repetirá)
if factura.estado == "emitida" and not factura.esta_pagada and factura.dias_vencida() > 30:
    factura.estado = "morosa"
    notificar_riesgo(factura)

# Tell: la regla vive con sus datos; el exterior solo expresa la intención
factura.marcar_morosa_si_procede(notificar_riesgo)
```

La versión *ask* es la fábrica del **modelo anémico** que diseccionaremos en la sección 5: objetos que son sacos de datos y lógica desparramada por los llamadores. Cada `if` sobre el estado interno de otro objeto es una pieza de esa lógica viviendo en casa ajena — y multiplicándose, porque el siguiente llamador copiará el `if`. En ATLAS, el PDF que *recalculaba* impuestos era exactamente un «ask» patológico: preguntaba por los datos crudos y rehacía la lógica por su cuenta.

## GRASP: los patrones de asignación de responsabilidades

Menos famosos que SOLID y anteriores en libro de texto: los **GRASP** (*General Responsibility Assignment Software Patterns*) los cataloga Craig Larman en *Applying UML and Patterns* (1997, con ediciones posteriores). No son reglas sino **preguntas con respuesta por defecto** para la decisión de diseño más frecuente que existe: «¿a quién le toca hacer esto?». Los cuatro que más se usan en la práctica:

- **Information Expert** (experto en información): asigna la responsabilidad a quien *tiene los datos* para cumplirla. ¿Quién calcula el total de la factura? La factura, que tiene las líneas. Es el padre intelectual de *Tell, Don't Ask*.
- **Creator** (creador): ¿quién crea las instancias de X? Quien las contiene, las agrega o tiene los datos de inicialización. ¿Quién crea `LineaFactura`? `Factura`, no un `LineaFacturaManager` flotante.
- **Low Coupling / High Cohesion**: elevados a patrón: ante dos diseños posibles, elige el que acople menos y cohesione más. Son el criterio de desempate de todos los demás.
- **Controller**: el primer objeto tras la interfaz que recibe una operación del sistema no debe ser la interfaz misma sino un coordinador delgado por caso de uso. Guarda este: en la sección 7 lo verás renacer con el nombre de *use case* y en la arquitectura destino del curso con la regla «entrypoints finos».

El valor de GRASP para un junior es enorme y poco publicitado: SOLID te dice cómo *no* acoplar lo que ya existe; GRASP te dice **dónde poner lo nuevo**, que es la pregunta que de verdad te haces cuarenta veces al día.

## La crítica honesta a SOLID

Ningún cuerpo de principios sobrevive intacto al contacto con la realidad, y conviene conocer las objeciones serias:

- **Son cualitativos, no medibles.** ¿Cuántas «razones para cambiar» tiene esta clase? Depende de cómo cuentes los actores. Los principios orientan conversaciones; no sustituyen al juicio. Usarlos como lista de verificación burocrática («esto viola SRP, rechazo el PR») sin argumentar el *coste real* es cargo-cult.
- **OCP envejeció regular.** Cerrar código «para siempre» casaba con un mundo de binarios distribuidos en los 90; con refactorización automática y tests, editar código existente es hoy barato y seguro. La lectura moderna — cerrar contra los cambios *que se repiten*, vía polimorfismo — sigue siendo oro; la lectura literal produce sobre-ingeniería especulativa.
- **La herencia perdió el trono.** LSP se formuló pensando en jerarquías de herencia; la práctica moderna (y este curso) prefiere **composición e interfaces** — el consejo «favorece la composición sobre la herencia» viene nada menos que del libro de patrones de la «Gang of Four» (Gamma, Helm, Johnson, Vlissides, *Design Patterns*, 1994). El LSP sobrevive traducido: todo *contrato* (interfaz, protocolo, duck typing) exige sustitutos honestos.
- **El peligro real es la indirección gratuita.** Cada abstracción tiene un coste de lectura: una interfaz con una sola implementación que nunca cambiará es puro peaje. La pregunta profesional nunca es «¿cumple SOLID?» sino «¿qué cambio concreto se vuelve barato gracias a esta abstracción, y ese cambio es plausible?». Si no hay respuesta, la abstracción sobra (cuarta regla de Beck).

Esta última idea da el criterio con el que leer todo el resto del curso: las arquitecturas que vienen en la próxima sección — hexagonal, clean — son *inversiones*. Como toda inversión, tienen prima y tienen retorno, y se justifican donde el retorno existe: en el corazón de negocio de un sistema que va a vivir años. ATLAS lo es. Un script de una tarde, no.

## Para llevar

- Ley de Deméter: habla solo con tus amigos inmediatos; cada punto extra de una cadena es conocimiento ajeno que te acopla. No aplica a estructuras de datos inertes.
- Tell, Don't Ask: la lógica vive con sus datos; preguntar estado para decidir fuera fabrica modelos anémicos y duplica reglas.
- GRASP (Larman): Information Expert, Creator, Controller, Low Coupling/High Cohesion — la guía para «¿a quién le toca esto?», la pregunta más frecuente del diseño.
- SOLID se critica con razón donde se aplica sin juicio: principios cualitativos, OCP releído a la moderna, composición sobre herencia, y guerra a la indirección sin retorno.
- Toda abstracción es una inversión: exige poder nombrar el cambio concreto que abarata. Ese criterio decide dónde sí (el corazón del negocio) y dónde no (el script de una tarde).
