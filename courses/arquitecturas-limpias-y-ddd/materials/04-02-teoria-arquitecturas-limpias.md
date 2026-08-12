Las tres reglas de la servilleta de Silvia — dentro el negocio, dependencias hacia dentro, fronteras con contrato — no son suyas: son la destilación de veinte años de propuestas convergentes que este capítulo recorre en orden. Al final habrás visto que «arquitectura hexagonal», «onion architecture» y «clean architecture» son tres dibujos del mismo teorema, y sabrás enunciar el teorema sin los dibujos.

## Qué es (y qué no es) la arquitectura

Empecemos desarmando un malentendido: la arquitectura de un sistema **no es su stack tecnológico**. «Somos una app en React con backend en Python y PostgreSQL» no describe una arquitectura, igual que «ladrillo y hormigón» no describe un edificio. La definición útil: **arquitectura es el conjunto de decisiones sobre qué piezas existen, qué sabe cada una de las demás y por dónde pasan las fronteras** — precisamente las decisiones que cuesta caro revertir. Una buena arquitectura, dirá Robert C. Martin, es la que **pospone** las decisiones costosas: que elegir base de datos, framework o forma de entrega importe lo más tarde posible y lo menos posible.

El contraejemplo tiene nombre técnico y artículo académico propio, cosa que sorprende a mucha gente: la **big ball of mud** (gran bola de barro). Brian Foote y Joseph Yoder la describieron en un paper de 1997 con ese título (disponible gratis en laputan.org), con una honestidad memorable:

> «Una big ball of mud es una jungla de código espagueti, estructurada al azar, extensa, descuidada, unida con cinta americana y alambre. [...] Estos sistemas muestran signos inequívocos de crecimiento no regulado y de reparaciones repetidas y oportunistas.» *(traducción propia)*

La tesis incómoda del paper: la bola de barro no es una anomalía — es **la arquitectura más frecuente del mundo**, porque es lo que emerge cuando nadie decide fronteras y cada urgencia se resuelve por el camino más corto. ATLAS no es un accidente; es el estado natural de un sistema al que nadie le puso paredes. Las arquitecturas de este capítulo son, todas, formas de ponérselas.

## Capas: la primera pared

La respuesta clásica es la **arquitectura en capas**: presentación arriba, lógica en medio, datos abajo, y cada capa usa solo a la inferior. Es un avance enorme sobre el barro — al menos el HTML no ejecuta SQL — y fue el estándar de facto durante décadas.

Pero tiene un defecto estructural que quizá ya puedes oler después de la sección 3: en la práctica, la capa de negocio **depende de la capa de datos** — la importa, conoce sus tablas, sus transacciones, su ORM. La flecha apunta de la política al detalle, violando el DIP a escala de edificio. Consecuencias conocidas: no puedes testear el negocio sin levantar una base de datos, cambiar de almacenamiento toca el negocio, y con los años la lógica migra hacia donde están los datos (procedimientos, consultas con reglas dentro) hasta que la «capa de negocio» es un pasillo vacío entre la pantalla y el SQL. A esta degeneración se la conoce en la literatura DDD como *smart UI* o, en su variante final, otra vez la bola de barro con tres pisos.

La pregunta que abre la era moderna es: ¿y si mantenemos las capas pero **giramos la flecha**?

## Hexagonal: puertos y adaptadores

En 2005, Alistair Cockburn publicó el artículo que formaliza el giro: *Hexagonal Architecture*, hoy renombrado **Ports and Adapters** (alistair.cockburn.us/hexagonal-architecture, gratuito). Su declaración de intenciones cabe en una frase citada mil veces:

> «Permitir que una aplicación sea usada por igual por usuarios, programas, tests automáticos o scripts por lotes, y que sea desarrollada y probada aislada de sus eventuales dispositivos y bases de datos de ejecución.» *(traducción propia)*

El modelo mental: la aplicación es un **hexágono**. Dentro, la lógica — el negocio — sin una sola referencia al mundo exterior. En los lados del hexágono, **puertos**: contratos que declaran conversaciones posibles con el exterior, definidos *por la aplicación* y en *su* vocabulario («guardar factura», «notificar al cliente», «obtener tipo de cambio»). Y fuera, **adaptadores**: piezas que traducen entre un puerto y una tecnología concreta — un adaptador HTTP que convierte peticiones REST en llamadas al puerto de entrada; un adaptador MySQL que implementa el puerto de salida «guardar factura»; un adaptador de test que implementa el mismo puerto en memoria.

Dos detalles del artículo original que se pierden en los resúmenes:

- **El número seis no significa nada.** Cockburn dibujó un hexágono para escapar del dibujo en capas (arriba/abajo) y sugerir *varios* puertos sin fijar cuántos. Él mismo dice que pudo ser un octógono.
- **La simetría es el corazón del patrón**: no hay «frontend» y «backend» — hay puertos *primarios* (quien conduce la aplicación: UI, tests, API) y *secundarios* (a quien la aplicación conduce: BD, correo). Un test automático es un actor primario tan legítimo como un humano. Por eso la testabilidad no es un añadido: es una consecuencia geométrica.

¿Te suena? Es el seam de Feathers (sección 2) y el DIP (sección 3) elevados a plano del edificio. Y es, casi palabra por palabra, la regla tres de la servilleta: *la frontera se cruza por puertas con contrato*.

## Clean Architecture: la síntesis y la regla

Entre 2005 y 2012 florecieron variantes con el mismo genoma — la **Onion Architecture** de Jeffrey Palermo (2008), la **Screaming Architecture** y otras. En 2012, Robert C. Martin las agrupó en un artículo breve, *The Clean Architecture* (blog.cleancoder.com, gratuito), con el diagrama de círculos concéntricos que probablemente hayas visto: entidades en el centro, casos de uso alrededor, adaptadores de interfaz después, frameworks y drivers en el borde. Y sobre el diagrama, una única ley, que él llama **la regla de la dependencia**:

> «Las dependencias del código fuente solo pueden apuntar hacia dentro. Nada en un círculo interior puede saber nada en absoluto sobre algo de un círculo exterior.» *(traducción propia)*

Eso es todo. De verdad: eso es *todo el artículo*. Los círculos concretos importan menos que la ley — el propio Martin dice que puede haber más o menos anillos. La regla de la dependencia es la regla dos de la servilleta, es el DIP aplicado sin excepciones, y tiene un corolario operativo que puedes usar mañana en cualquier revisión de código: **mira los imports**. Un fichero de negocio que importa un driver de base de datos, un SDK de un proveedor o un framework web es una gotera en la frontera. El barro empieza siempre por un import inocente.

De la misma época y autor es una idea complementaria que merece su nombre: la **screaming architecture** (arquitectura que grita). Al abrir la carpeta raíz de un proyecto, ¿qué grita? Si grita «¡soy una app de Django!» — `views/`, `models/`, `templates/` —, la tecnología ha ocupado el trono. Debería gritar «¡soy un sistema de facturación!»: `facturacion/`, `clientes/`, `impuestos/`. La primera pregunta de un recién llegado no es «¿qué framework usáis?» sino «¿qué hace este sistema?», y la estructura de carpetas es la primera respuesta que recibe.

## El mismo teorema, tres dibujos

| Propuesta | Autor, año | Dibujo | Aportación distintiva |
|---|---|---|---|
| Hexagonal / Ports & Adapters | Cockburn, 2005 | Hexágono | Simetría primario/secundario; el test como actor de pleno derecho |
| Onion | Palermo, 2008 | Anillos | El modelo de dominio en el núcleo, explícito |
| Clean | Martin, 2012 | Círculos concéntricos | La regla de la dependencia como ley única; entidades vs. casos de uso |

Las diferencias reales entre las tres son menores que las diferencias entre dos equipos cualesquiera aplicando la misma. Lo invariante — el teorema — es la servilleta de Silvia: **(1) dentro el negocio, fuera el mundo; (2) dependencias solo hacia dentro; (3) fronteras cruzadas por contratos.**

## La servilleta, ejecutable

Así se ve el teorema en un módulo pequeño y real, en JavaScript. Tres ficheros, tres papeles:

```javascript
// domain/RepositorioDeFacturas.js — EL PUERTO (dentro: solo el contrato)
// El negocio declara qué necesita, en su vocabulario. Ningún import hacia fuera.
export class RepositorioDeFacturas {
  async guardar(factura) { throw new Error("implementar"); }
  async buscarPorId(id) { throw new Error("implementar"); }
}
```

```javascript
// application/emitirFactura.js — EL CASO DE USO (dentro: orquesta el negocio)
import { Factura } from "../domain/Factura.js";   // import hacia DENTRO: legal

export async function emitirFactura({ pedido, repositorioDeFacturas }) {
  const factura = Factura.crearDesdePedido(pedido);  // reglas de negocio puras
  await repositorioDeFacturas.guardar(factura);      // habla con el puerto, no con MySQL
  return factura;
}
```

```javascript
// infrastructure/MySQLRepositorioDeFacturas.js — EL ADAPTADOR (fuera)
import mysql from "mysql2/promise";                               // el driver vive AQUÍ
import { RepositorioDeFacturas } from "../domain/RepositorioDeFacturas.js"; // import hacia dentro

export class MySQLRepositorioDeFacturas extends RepositorioDeFacturas {
  async guardar(factura) { /* SQL, filas, transacciones: solo aquí */ }
  async buscarPorId(id) { /* ... */ }
}
```

Comprueba la ley con los imports: `domain` no importa nada; `application` importa solo `domain`; `infrastructure` importa el mundo *y* el contrato de dentro. Todas las flechas apuntan hacia el centro. Y el premio inmediato, como prometía Cockburn: para testear `emitirFactura` no hace falta MySQL — basta un adaptador en memoria de veinte líneas. En Python el dibujo es idéntico (una clase base abstracta o un `Protocol` como puerto, módulos como capas).

Este módulo de tres ficheros es, a escala 1:100, exactamente la arquitectura del documento real que leeremos en la sección 10 — sus carpetas se llaman `domain/`, `application/` e `infrastructure/`, y su ley fundamental está enunciada en cuatro palabras: *dependencies always point inward*.

## Lo que la arquitectura no resuelve

Cerramos con la advertencia que la historia dejó plantada y que Gabriel se negó a responder «hasta el capítulo ocho». Fénix fracasó *teniendo* un diseño moderno. Los céntimos que no cuadraban no eran un problema de capas: eran **quince mil verdades de negocio que solo existían en el código viejo**. Una arquitectura limpia hace el conocimiento *fácil de alojar y de cambiar*; no genera el conocimiento. De dónde sale ese conocimiento, cómo se captura y qué relación tiene con el lenguaje que hablan Marta y contabilidad — eso es la otra mitad de este curso, y se llama Domain-Driven Design. Las capas son la casa. Falta saber qué vive dentro.

## Para llevar

- Arquitectura = decisiones sobre piezas, conocimiento mutuo y fronteras — las decisiones caras de revertir. Buena arquitectura: la que pospone y abarata decisiones, no la que fija un stack.
- Big ball of mud (Foote & Yoder, 1997): la arquitectura por defecto del universo; emerge sola donde nadie pone fronteras.
- Capas clásicas: mejor que el barro, pero la flecha negocio→datos viola el DIP y la lógica acaba emigrando hacia el SQL.
- Hexagonal (Cockburn, 2005): dentro la lógica, puertos como contratos en vocabulario del negocio, adaptadores por tecnología. Simetría: el test es un actor primario. El seis no significa nada.
- Clean (Martin, 2012): una sola ley — las dependencias del código fuente apuntan hacia dentro. Auditable mirando imports.
- Screaming architecture: las carpetas deben gritar el negocio, no el framework.
- La arquitectura aloja el conocimiento del dominio; no lo produce. Fénix murió de eso, no de capas — continuará en la sección 8.

## Para profundizar

- Alistair Cockburn, *Hexagonal Architecture* — el artículo original, gratuito (alistair.cockburn.us).
- Robert C. Martin, *The Clean Architecture* (2012) y *Screaming Architecture* (2011), gratuitos en blog.cleancoder.com.
- Brian Foote & Joseph Yoder, *Big Ball of Mud* (1997) — gratuito en laputan.org; lectura amena y humillante a partes iguales.
- Herberto Graça, serie *DDD, Hexagonal, Onion, Clean, CQRS: how I put it all together* (herbertograca.com, gratuita) — la mejor cartografía comparada de todas estas propuestas.
