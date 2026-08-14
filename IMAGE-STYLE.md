# Guía de estilo de imágenes

Estilo visual único para todas las imágenes de la biblioteca (portadas de curso,
tarjetas de categoría, imágenes de noticias). El objetivo es que cualquier imagen
nueva, generada en cualquier momento y con cualquier herramienta, parezca de la
misma colección.

## El estilo

**Retrato pictórico en primer plano.**

Pintura digital cálida y atmosférica, pero con composición de *thumbnail*, no
de cuadro: estas imágenes se ven casi siempre como cards pequeñas en el
catálogo, así que el sujeto tiene que leerse de un vistazo a 300 píxeles.

- **Un solo objeto protagonista que llena el 70–80 % del encuadre**, centrado
  o ligeramente descentrado. Primer plano, como un retrato de producto.
- **Prohibido:** paisajes anchos, escenas panorámicas, sujetos pequeños o
  lejanos, multitud de elementos. Si al encoger la imagen a miniatura el
  sujeto no se distingue, la composición está mal.
- Fondo simple y desenfocado: solo atmósfera y color, sin detalles que
  compitan.
- Acabado pictórico: pinceladas suaves, luz cálida envolvente, brillos ricos.
- La firma de la colección es la luz: **el objeto iluminado en dorado ámbar
  cálido, la atmósfera y las sombras en teal profundo**.
- Tono cálido, evocador, con un punto de asombro. Nada estridente.
- **Nunca texto, letras, logotipos ni marcas de agua dentro de la imagen.**

### Paleta lumínica

| Papel en la escena       | Color                                  |
| ------------------------ | -------------------------------------- |
| Atmósfera y sombras      | teal profundo (herencia del `#123c43`) |
| Luz sobre el objeto      | dorado ámbar (herencia del `#f0a92e`)  |
| Brillos                  | crema suave                            |
| Oscuridad profunda       | azul marino                            |

No son colores planos: son la temperatura de la luz. El objeto brilla cálido;
lo que lo rodea respira frío.

### Formato

- Relación de aspecto **16:9**, en horizontal (en ChatGPT: pedir directamente
  "16:9 landscape"). Es el formato exacto de las cards de curso y categoría
  (`aspect-ratio: 16 / 9` en la aplicación), así que se ve sin recortes.
- Excepción — imágenes de **noticias**: la lista de noticias las recorta a
  21:9 (más panorámicas), perdiendo franjas arriba y abajo. Generar igualmente
  en 16:9 pero mantener el sujeto centrado en vertical.
- Exportar como JPG y guardar en `media/` con nombre en kebab-case:
  `media/<curso>-cover.jpg`, `media/category-<categoria>.jpg`.
- Actualizar después el `coverImage` del `course.json` o el `imagePath` del
  JSON de categoría.

## Prompt base (copiar siempre como inicio)

```
Warm atmospheric digital painting with soft visible brushwork. Close-up
product-portrait composition: one single large subject filling 70-80% of the
frame, centered, instantly readable even as a small thumbnail. Simple softly
blurred background with no competing details — pure atmosphere. No wide
landscapes, no tiny distant objects, no busy scenes. Signature lighting: the
subject bathed in warm golden amber light with soft cream highlights, the
surrounding atmosphere and shadows in cool deep teal. Rich, cozy, slightly
wondrous mood. Absolutely no text, no letters, no logos, no watermark.
16:9 landscape.

Subject: <un solo objeto, descrito en una o dos frases>
```

Para crear una imagen nueva: copia el prompt base y sustituye la línea
`Subject:`. No cambies la parte del estilo — es lo que mantiene la colección
coherente. Regla de oro: un solo objeto, grande, que se reconozca en miniatura.

## Logo

El logo es la excepción al estilo pictórico: debe ser **plano, de colores
sólidos y con fondo transparente**, porque se ve a ~30 px en el header y como
favicon. Misma paleta, distinto tratamiento.

Prompt base de logo (sustituir `<MARK>` por la descripción del símbolo y
`<COLORS>` por la variante de color):

```
Minimalist flat vector logo mark for a digital library. Solid flat colors
only, clean bold geometric shapes, no gradients, no outlines, no shadows, no
3D, absolutely no text or letters. <COLORS> Transparent background. The mark
must remain perfectly legible at 24 pixels: one simple bold silhouette, no
fine details. Centered with generous empty margins around it.

The mark: <MARK>
```

Variantes de color:

- Para header claro: `Two colors: deep teal (#123c43) as the main color and
  warm amber (#f0a92e) as the accent.`
- Para header oscuro: `Two colors: soft cream (#f5efe0) as the main color and
  warm amber (#f0a92e) as the accent.`

Marks definidos (los tres conceptos):

- **Libro amanecer:** `a simple open book seen from the front as one solid
  bold shape, with five short sun rays fanning out from behind its spine like
  a sunrise, each ray shaped like a small page.`
- **Motas de luz:** `a simple open book drawn as one bold shape, with three
  round dots of light rising from its pages in a gentle diagonal, decreasing
  in size as they rise (dots in amber).`
- **La llama:** `a simple rounded flame (in amber) centered inside a thick
  circular ring that is deliberately open at the top, as if the light escapes
  upward.`

## Prompts ya definidos

### Portadas de curso

**El código que perdura** (`media/codigo-que-perdura-cover.jpg`):

```
Subject: a vintage brass drafting compass standing upright on old architectural
blueprints, close-up, warm lamplight glinting on the brass, the blueprint lines
fading into soft teal shadow around it.
```

**La filosofía de Open Knowledge / The philosophy of Open Knowledge**
(`media/philosophy-cover.jpg`, compartida por ambos idiomas):

```
Subject: an antique brass oil lamp with a warm glowing flame, close-up,
sitting on a stack of two old leather books, its golden light pushing back the
deep teal darkness around it.
```

**Open Knowledge en marcha / Running Open Knowledge**
(`media/running-cover.jpg`, compartida por ambos idiomas):

```
Subject: a charming miniature model of a classical library building with tiny
glowing amber windows and a large brass wind-up key sticking out of its side,
close-up on a wooden table, soft teal dusk atmosphere behind it.
```

**El oficio y la máquina: el ingeniero de software en la era de la IA**
(`media/oficio-y-la-maquina-cover.jpg`):

```
Subject: a brain made of glowing golden circuit traces and microchips, close-up
filling the frame, warm amber light along its circuit paths, dissolving into
cool teal shadow at the edges.
```

**Cuando todo falla: radioafición en España**
(`media/radioaficion-cover.jpg`):

```
Subject: the front panel of a vintage ham radio transceiver, close-up, its
round tuning dial and needle gauges glowing warm amber in a dark teal room,
soft light reflecting off the metal knobs.
```

### Tarjetas de categoría

**Open Knowledge** (`media/category-open-knowledge.jpg`):

```
Subject: a large open book filling the frame, close-up, its pages glowing
softly golden with a few tiny motes of warm light drifting up from them into
the surrounding teal darkness.
```

**Desarrollo de Software** (`media/category-desarrollo-de-software.jpg`):

```
Subject: a close-up macro view of mechanical keyboard keys, softly backlit in
warm amber, shallow depth of field, the farther keys dissolving into a cool
teal glow. Blank keycaps with no letters.
```

**Radio y Comunicaciones** (`media/category-radio-y-comunicaciones.jpg`):

```
Subject: a classic vintage broadcast microphone, close-up, filling the frame,
its chrome grille catching warm amber studio light against a softly blurred
deep teal background.
```
