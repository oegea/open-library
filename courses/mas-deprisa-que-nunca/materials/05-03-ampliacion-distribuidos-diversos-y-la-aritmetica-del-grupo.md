Tres temas que la teoría no pudo abarcar y que completan el mapa de los equipos: qué dice la evidencia seria (hay dos RCTs en *Nature* y *QJE*, nada menos) sobre remoto e híbrido; qué dice — y qué no dice — la ciencia sobre diversidad y rendimiento; y un pequeño simulador para tocar con las manos la aritmética de Brooks.

## 1. Remoto, híbrido y el principio 6 releído

El Manifiesto Ágil (2001) declaró que «el método más eficiente y eficaz de transmitir información a un equipo de desarrollo, y dentro de él, es la conversación cara a cara». En 2001 era razonable; hoy tenemos datos de verdad, y piden una lectura más fina:

- **Bloom, Liang, Roberts y Ying (2015, *Quarterly Journal of Economics*)** — un RCT real en Ctrip (~16.000 empleados; call center): el teletrabajo produjo **+13% de rendimiento**, más satisfacción y **la mitad de rotación**… en tareas individuales y medibles. Limitación clave: un call center no es un equipo de producto.
- **Yang et al. (2021, *Nature Human Behaviour*)** — datos de ~61.000 empleados de Microsoft durante el paso al remoto total: las redes de colaboración se volvieron **más estáticas y aisladas en silos**, con menos puentes entre grupos, y la comunicación se desplazó de síncrona a asíncrona — con posible daño, según los autores, a la transferencia de información compleja y nueva. El remoto total no mató la productividad individual; erosionó el tejido *entre* grupos.
- **Bloom, Han y Liang (2024, *Nature*)** — RCT del híbrido (1.612 profesionales, 3 días oficina / 2 remoto): **un tercio menos de bajas voluntarias, sin efecto en rendimiento ni promoción** a dos años. El híbrido bien diseñado salió gratis en rendimiento y carísimo de no ofrecer en retención.
- Y el precedente que el open source conocía hace décadas: **Herbsleb y Mockus (2003, *IEEE TSE*)** midieron que el trabajo distribuido entre sedes tardaba del orden de **2,5 veces más** que el equivalente colocalizado — por fricción de comunicación y redes de contacto más pobres.

¿Síntesis? El principio 6 no dice «volved todos a la oficina»; leído con 2026 de perspectiva, dice: **la riqueza del canal debe elegirse según la ambigüedad de la tarea** (eso es, formalizado, la teoría de riqueza de medios de Daft y Lengel: los medios ricos — cara a cara, vídeo — para negociar significado; los pobres — texto — para transmitir hechos). Los equipos distribuidos que funcionan hacen deliberadamente lo que el open source institucionalizó: escritura excelente, decisiones documentadas en público, asincronía por defecto — **más** momentos síncronos ricos, deliberados y caros, para lo ambiguo: el kickoff de Gersick, el conflicto que se enquista, el onboarding (la memoria transactiva se construye fatal por chat). Remoto no es oficina menos algo: es otro sistema sociotécnico, que hay que diseñar en vez de improvisar.

## 2. Diversidad y rendimiento: la evidencia honesta

Pocas áreas tienen tanta distancia entre el discurso público y la literatura. Lo que dicen los meta-análisis académicos (Joshi y Roh, 2009, 8.757 equipos; Horwitz y Horwitz, 2007; Bell et al., 2011; van Dijk et al., 2012): **los efectos directos medios de la diversidad sobre el rendimiento son pequeños y cercanos a cero** — tanto para diversidad demográfica como funcional. Lo cual no cierra el tema: lo abre, porque el efecto medio nulo esconde dos fuerzas contrarias que el **modelo categorización-elaboración** (van Knippenberg et al., 2004) describe bien:

- La diversidad ayuda por la vía de la **elaboración de información**: más perspectivas, más conocimiento no redundante procesado — especialmente en tareas complejas y creativas (la diversidad *de conocimiento y función* es la mejor posicionada: exactamente la que encarna un equipo multifuncional).
- Y daña por la vía de la **categorización social**: «nosotros/ellos», fallas (*faultlines*) que parten el equipo en subgrupos.
- **Qué fuerza gana lo deciden los moderadores**: normas inclusivas, interdependencia, liderazgo… y la seguridad psicológica y los turnos equilibrados de la teoría — que son, literalmente, la maquinaria que convierte diferencia en información en lugar de en bandos.

Aviso de rigor sobre las fuentes que probablemente te citen: los informes de consultoría tipo McKinsey (*Diversity Wins* y sucesores), que muestran correlaciones empresa-nivel entre diversidad directiva y resultados, han recibido críticas metodológicas serias (Green y Hand, 2024, *Econ Journal Watch*: al re-analizar los datos no pudieron reproducir los resultados, y concluyen que esos informes no deben usarse como evidencia): no son la base sobre la que defender nada. La defensa seria de la diversidad no necesita inflar datos de rendimiento: se sostiene en la equidad (que no requiere justificación instrumental), en la diversidad cognitiva bien gestionada para tareas complejas — y en no confundir jamás «el efecto medio es nulo» con «da igual»: significa que **la gestión es la variable**. Un equipo diverso bien facilitado supera; uno mal facilitado paga; la mediocridad homogénea, al menos, es predecible. Elige.

## 3. La aritmética del grupo, ejecutable

Para la intuición de Brooks y Steiner, nada como verlo. Un modelo de juguete: cada persona aporta capacidad 1, pero cada par de personas consume una fracción de capacidad en coordinación (reuniones, contexto, re-explicaciones), y el holgazaneo crece suavemente con el tamaño (Ringelmann):

```javascript
// Capacidad efectiva de un equipo de n personas (modelo de juguete)
function capacidadEfectiva(n, costePorEnlace = 0.04, loafing = 0.015) {
  const enlaces = (n * (n - 1)) / 2;              // Brooks: n(n-1)/2
  const coordinacion = enlaces * costePorEnlace;   // pérdida de proceso (Steiner)
  const motivacion = n * loafing * (n - 1);        // pérdida motivacional creciente
  return Math.max(0, n - coordinacion - motivacion);
}

for (let n = 2; n <= 15; n++) {
  const cap = capacidadEfectiva(n);
  console.log(
    `${String(n).padStart(2)} personas → capacidad ${cap.toFixed(1)}` +
    ` (${(cap / n * 100).toFixed(0)}% por cabeza)` +
    ` ${"█".repeat(Math.round(cap * 2))}`
  );
}
```

Con estos parámetros (inventados, como corresponde a un juguete — el fenómeno es real, las constantes no), la capacidad total hace pico en torno a 8-9 personas y luego *baja en términos absolutos*: la persona 12 resta. Juega con las constantes: equipos con excelente tooling de coordinación (documentación, interfaces claras, asincronía bien hecha) tienen `costePorEnlace` menor y aguantan más tamaño — que es exactamente por qué escalar pasa por *reducir el coste del enlace o eliminar enlaces* (equipos desacoplados, API entre equipos), no por añadir cabezas al mismo grafo denso.

Y la moraleja del juguete conecta las tres partes de esta ampliación: el tamaño, la distribución geográfica y la diversidad comparten estructura — **ninguno es bueno o malo per se; todos cargan un coste de coordinación/categorización que la gestión puede pagar o no**. Los equipos que funcionan no son los que evitan estas variables: son los que las diseñan con los ojos abiertos.

## Para profundizar

- Bloom et al. (2015) — working paper: https://www.nber.org/system/files/working_papers/w18871/w18871.pdf
- Yang et al. (2021), remoto y silos — https://www.nature.com/articles/s41562-021-01196-4
- Bloom, Han & Liang (2024), híbrido — https://www.nature.com/articles/s41586-024-07500-2
- Joshi & Roh (2009), meta-análisis de diversidad — PDF: https://ideas.wharton.upenn.edu/wp-content/uploads/2018/07/Joshi-Roh-2009.pdf
- Traylor et al. (2024), diversidad y procesos de equipo — open access: https://journals.sagepub.com/doi/10.1177/20413866241245312
- Brooks, F. — *The Mythical Man-Month* (libro de pago; resumen fiable: https://en.wikipedia.org/wiki/The_Mythical_Man-Month)
