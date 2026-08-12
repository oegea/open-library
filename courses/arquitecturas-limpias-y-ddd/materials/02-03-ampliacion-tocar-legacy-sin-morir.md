La teoría contó la maniobra grande (caracterizar, cambiar, verificar). Esta ampliación recoge las técnicas de grano fino de *Working Effectively with Legacy Code* (Michael Feathers, 2004) que más se usan en el mundo real y menos se conocen por su nombre. Son el vocabulario compartido de los equipos que rescatan sistemas — y saber el nombre de una maniobra es media maniobra.

## Seams: los puntos de intervención

Feathers llama **seam** (costura) a *un punto donde puedes alterar el comportamiento de un programa sin editar su código en ese punto*. Es el concepto central de todo el libro. Para poner un test necesitas dos cosas: ejecutar la pieza aislada y observar su resultado; los seams son los sitios por donde el aislamiento es posible.

El seam universal en lenguajes como JavaScript y Python es el **seam de objeto/parámetro**: si una función recibe sus colaboradores como argumentos, puedes pasarle sustitutos en el test.

```python
# Sin seam: la dependencia está soldada dentro
def emitir_recordatorios():
    facturas = MySQLConexion().query("SELECT ...")   # imposible de testear sin BD
    for f in facturas:
        smtp_enviar(f.email, plantilla(f))            # imposible sin servidor de correo

# Con seam: las dependencias entran por la puerta
def emitir_recordatorios(buscar_vencidas, enviar):
    for factura in buscar_vencidas():
        enviar(factura.email, plantilla(factura))
```

La segunda versión se testea pasando un `buscar_vencidas` que devuelve datos fijos y un `enviar` que apunta a una lista. Fíjate en la dirección del truco: no hemos «añadido tests al código»; hemos **cambiado la forma del código para que los tests sean posibles**. Testabilidad es una propiedad del diseño, no del framework de testing — esta frase es medio curso resumido, y en la sección 6 verás que el patrón repository es exactamente este seam elevado a principio arquitectónico.

## Sprout: crecer al lado, no dentro

¿Qué haces cuando necesitas añadir lógica a una función-monstruo de mil líneas que no puedes caracterizar todavía? El instinto — «son cuatro líneas, las meto dentro» — hace crecer al monstruo. La técnica correcta es el **sprout method** (método brote): escribe la lógica nueva en una **función nueva, limpia y con tests**, y añade al monstruo solo la llamada.

```javascript
// Dentro de calc2(), línea 900 y pico, UNA línea nueva:
importe = aplicarRecargoDeEquivalencia(importe, cliente); // ← llamada al brote

// Y en un fichero nuevo, testeado desde el primer día:
export function aplicarRecargoDeEquivalencia(importe, cliente) {
  if (!cliente.enRecargoDeEquivalencia) return importe;
  return redondearImporteDeLinea(importe * (1 + RECARGO_EQUIVALENCIA));
}
```

El monstruo queda casi intacto (riesgo mínimo) y el código nuevo nace limpio (deuda cero). Cuando la lógica nueva es grande, la variante es la **sprout class**: una clase nueva entera. La consecuencia estratégica es preciosa: con disciplina de brotes, *todo el código nuevo de un sistema legacy nace testeado*, y el porcentaje limpio crece monótonamente aunque nadie haga «el gran refactor».

## Wrap: envolver sin tocar

Complementaria del brote: cuando necesitas que *antes o después* de la lógica vieja ocurra algo nuevo, no edites la lógica vieja — **envuélvela** (*wrap method*). La función original se renombra y se vuelve privada; una función nueva con el nombre original llama a la vieja y añade lo nuevo alrededor:

```python
def emitir_factura(pedido):            # el nombre público no cambia para nadie
    factura = _emitir_factura_original(pedido)   # lo viejo, intacto
    registrar_auditoria(factura)                  # lo nuevo, testeado aparte
    return factura
```

Brote y envoltura comparten filosofía: **minimizar la superficie de contacto con lo que no tiene red.**

## Scratch refactoring: refactorizar para tirar

Técnica psicológicamente liberadora y casi desconocida fuera del libro de Feathers: para *entender* un código impenetrable, refactorízalo salvajemente — renombra, extrae, borra, reordena — **sin intención de conservar nada**, y cuando lo hayas entendido, **tira la rama**. Sin tests no puedes fiarte de ese refactor, y no importa: su producto no era el código, era el mapa mental que ahora tienes. Júlia hizo una versión manual de esto la noche del martes, con papel y boli; con un editor es más rápido. La regla de hierro es una sola: la rama se llama `scratch/` y **jamás se fusiona**.

## Golden master con herramientas: approval testing

El golden master artesanal (ficheros de referencia + comparación) tiene tooling maduro que conviene conocer: las librerías de **approval testing** (aprobación). En lugar de `assert resultado == esperado`, escribes `verify(resultado)`: la primera ejecución guarda el resultado como «recibido» y te pide *aprobarlo* (normalmente con un diff visual); las siguientes comparan contra lo aprobado. Para salidas grandes — una remesa de facturas, un HTML, un JSON de 400 líneas — es radicalmente más cómodo que mantener aserciones a mano. Busca `ApprovalTests` (existe para Python, JavaScript y una docena de lenguajes más; proyecto de código abierto de Llewellyn Falco y comunidad). Un detalle profesional: los ficheros aprobados se versionan en Git — un cambio de comportamiento aparece en la revisión de código como un diff legible del *comportamiento*, no del código.

## El algoritmo completo de cambio en legacy

El capítulo 2 del libro de Feathers resume el proceso entero en cinco pasos que merecen estar en una nota pegada al monitor:

1. **Identifica los puntos de cambio** (dónde tiene que entrar tu modificación).
2. **Encuentra los puntos de test** (dónde puedes observar comportamiento).
3. **Rompe las dependencias** (crea seams — la parte delicada, con técnicas como las de arriba, hecha con cambios mínimos y mecánicos).
4. **Escribe los tests** (de caracterización, sobre los seams recién abiertos).
5. **Haz el cambio y refactoriza** (ahora sí, con red).

El error universal de los impacientes es saltar del paso 1 al 5. Se llama «editar y rezar», y en Meridian ya sabemos cómo acaba.

## Para llevar

- Seam: punto donde alterar comportamiento sin editar el código en ese punto. Crear seams pasando dependencias como parámetros es la técnica madre; la testabilidad es una propiedad del diseño.
- Sprout: la lógica nueva nace en funciones/clases nuevas y testeadas; al legacy solo se le añade la llamada. Wrap: lo nuevo envuelve a lo viejo sin tocarlo.
- Scratch refactoring: refactoriza para entender y tira la rama. El producto es el mapa mental.
- Approval testing: golden master con herramienta (aprobar diffs en lugar de escribir aserciones); los ficheros aprobados se versionan.
- El algoritmo de Feathers: puntos de cambio → puntos de test → romper dependencias → tests → cambio. No saltarse pasos: eso ya tiene nombre, y es «editar y rezar».
