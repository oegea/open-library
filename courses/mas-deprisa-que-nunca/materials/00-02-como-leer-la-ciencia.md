Este curso promete fundamentos científicos, así que antes de empezar conviene acordar qué significa eso. No hace falta ser investigador para leer evidencia con criterio; hace falta conocer media docena de ideas. Este capítulo te las da, junto con el mapa del viaje completo. Es el capítulo más corto del curso y probablemente el que más veces recordarás.

## La escalera de la evidencia

No toda la "evidencia" pesa lo mismo. De menos a más, esta es la escalera que usaremos en todo el curso:

1. **Anécdota.** «En mi empresa hicimos X y funcionó.» Es un dato real, pero no sabemos si X causó el resultado, si fue casualidad, o si mil empresas hicieron X y quebraron sin que nadie escribiera un post sobre ello. Las charlas de conferencia viven aquí.
2. **Caso de estudio.** Una anécdota investigada con método: entrevistas, documentos, datos internos. Mucho más rica, pero sigue siendo una empresa, un contexto. El estudio de las minas de Durham que veremos en la sección 1, o el análisis del accidente del Challenger de la sección 10, son casos de estudio magníficos — y aun así, casos.
3. **Estudio correlacional.** Se mide a mucha gente o muchos equipos y se buscan asociaciones: «los equipos con más X rinden más». El problema eterno: **correlación no es causalidad**. ¿X causa el rendimiento, el rendimiento causa X, o una tercera cosa causa ambos? Gran parte de la investigación sobre organizaciones (incluidos los informes DORA que citaremos) vive aquí, y no es poco — pero hay que leerla sabiendo lo que es.
4. **Experimento controlado (RCT).** Se asigna **al azar** quién recibe la intervención y quién no, de modo que la única diferencia sistemática entre grupos es la intervención misma. Es lo más cerca que se puede estar de demostrar causa. Son caros y raros en management; cuando existen (y en este curso aparecerán varios, alguno espectacular), valen oro.
5. **Meta-análisis.** El resumen estadístico de muchos estudios sobre la misma pregunta. Corrige la debilidad de cualquier estudio individual (muestras pequeñas, contextos raros) y estima el tamaño real del efecto. Es el estándar de referencia — con su propia letra pequeña: un meta-análisis de estudios malos sigue siendo débil («basura entra, basura sale»).

Dos nociones más y tenemos el equipo completo:

- **Tamaño del efecto.** Que algo sea «estadísticamente significativo» solo dice que probablemente no es ruido; no dice si es *grande*. Los investigadores usan la **d de Cohen**: orientativamente, d≈0,2 es un efecto pequeño, d≈0,5 mediano y d≈0,8 grande. La usaremos a menudo, porque la diferencia entre «el feedback mejora el rendimiento (d=0,41)» y «mejora el rendimiento» es la diferencia entre saber algo y repetir un eslogan.
- **Replicación.** Un hallazgo vale lo que valen sus réplicas. La psicología vivió en la década de 2010 una crisis de replicación que tumbó o encogió efectos famosos. Este curso está escrito después de esa crisis, y se nota: varios resultados que la literatura de agile cita alegremente salen aquí con su tamaño real, bastante más humilde.

## La navaja de Popper

Un criterio filosófico que usaremos como herramienta práctica. El filósofo **Karl Popper** propuso que lo que distingue una teoría científica no es que pueda confirmarse, sino que pueda **fallar**: una teoría es científica si es incompatible con alguna observación posible — si existe un experimento imaginable cuyo resultado la refutaría. Una idea compatible con cualquier resultado («el equipo falló porque no era *suficientemente* agile») no es una teoría: es una consigna blindada. (La formulación canónica puede leerse en la entrada «Karl Popper» de la *Stanford Encyclopedia of Philosophy*, de acceso abierto.)

Esta navaja corta en dos direcciones y ambas nos interesan. Primero, hacia los frameworks: cuando algo se vende como infalible — si funciona, mérito del método; si no funciona, culpa de tu implementación — estamos ante fe, no ante ingeniería. Segundo, hacia tu propio trabajo: en la sección 3 veremos que tratar cada feature como una **hipótesis falsable** («creemos que X hará que los usuarios hagan Y; si en cuatro semanas Y no se mueve, estábamos equivocados») no es una metáfora bonita sino una práctica con un ensayo controlado aleatorizado detrás.

## Las cifras zombi

En la industria del software circulan números que todo el mundo cita y casi nadie ha rastreado. El programador y ensayista Laurent Bossavit los llamó *leprechauns*: duendes bibliográficos. El patrón es siempre el mismo: alguien cita a alguien que citaba a alguien, y en el origen de la cadena hay un estudio minúsculo, un contexto irrelevante o directamente nada. Tres avisos de los que este curso se hará cargo con detalle:

- «El 64% de las features nunca se usan» — procede de una presentación de 2002 sobre **cuatro** aplicaciones internas, jamás publicada con metodología.
- «Recuperarse de una interrupción cuesta 23 minutos y 15 segundos» — esa cifra con segundos incluidos no aparece en ningún paper; viene de una entrevista. (El dato real del estudio es otro, y lo veremos.)
- «Hay programadores 10x» — el estudio de origen es de 1968, con doce sujetos, midiendo otra cosa.

La lección no es «desconfía de todo», sino: **una afirmación con número exige una fuente con método**. Cuando en este curso un número no la tenga, lo marcaremos como lo que es — folclore, a veces folclore útil — y cuando la tenga, sabrás exactamente de dónde sale. Te pedimos el mismo estándar para lo que leas fuera, incluido — hoy más que nunca — lo que se afirma sobre la IA.

## Con esta vara mediremos también al agile

Una advertencia que es también una declaración de intenciones: la vara de medir se aplica a todos. Al consultor que cobra el curso de tres días, a McKinsey, a los informes de vendors con producto que colocar — y también al Manifiesto Ágil, a la Scrum Guide y a los hallazgos que a este curso le gustan. Verás secciones enteras dedicadas a contarte que un modelo famoso (las etapas de Tuckman, el efecto Hawthorne, el growth mindset corporativo) tiene mucha menos evidencia de la que su fama sugiere. No es afán de derribo: es que un curso que solo contara lo que conviene a su tesis sería exactamente el tipo de material del que intenta protegerte.

## El mapa del viaje

El curso tiene tres movimientos:

**Primero, los cimientos (secciones 1 a 11).** La ciencia por debajo del agile, ordenada de dentro afuera: de dónde viene la idea de equipo autoorganizado (S1); por qué el software se resiste a la planificación y qué pasó en Snowbird en 2001 (S2); cómo se decide *qué* construir con método científico (S3); qué motiva de verdad a una persona (S4); qué hace funcionar a un equipo (S5); cómo el feedback y la reflexión convierten trabajo en aprendizaje (S6); la física del flujo de trabajo — colas, lotes, interrupciones (S7); cómo medir sin corromper lo que mides (S8); cómo decidir en grupo sin engañarse (S9); el ritmo sostenible y el aprendizaje del fallo (S10); y la organización entera — estructura, managers, cultura (S11).

**Segundo, la gobernanza (sección 12).** El modelo organizativo que el software libre lleva treinta años demostrando — autoorganización con reglas explícitas — y lo que la ciencia de los comunes de Elinor Ostrom dice sobre él. También: qué pasó con el agile cuando se convirtió en industria, contado por los propios firmantes del manifiesto.

**Tercero, la era de la IA (sección 13).** Con todos los principios en la mano, la evidencia empírica 2023-2026 sobre IA y desarrollo de software — que es más rara, más contradictoria y más interesante de lo que cuentan tanto los entusiastas como los apocalípticos — y una extrapolación honesta, marcada como tal, de qué formas de trabajar tienen sentido cuando el código es barato y el criterio no.

La sección 14 cierra con la síntesis, la bibliografía completa y por dónde seguir.

Cada sección se sostiene sola, pero el orden importa: la historia es continua y la teoría se apoya en lo anterior. Si solo te llevas una cosa de este capítulo, que sea la escalera de la evidencia. Vas a usarla en cada sección — y, si el curso funciona, durante el resto de tu carrera.

Ahora sí. Valencia, 2026. Una sala llena de dashboards en verde y una empresa que va mal.
