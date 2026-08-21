Dos piezas prácticas para cerrar la sección: la ley de Goodhart convertida en simulación que puedes ejecutar (y enseñar en una reunión incómoda), y la instrumentación mínima con la que un equipo puede empezar mañana sin fabricar su propio IPA.

## 1. El Becario Fantasma de bolsillo: divergencia proxy-valor en 40 líneas

El fenómeno de fondo del IPA — optimizar una **proxy** (medida sustitutiva) hace que la proxy y el **valor real** diverjan — se deja simular con un modelo mínimo. Supón que el valor real de un PR depende de dos cosas: su utilidad y su calidad de verificación; y que la proxy solo cuenta *número de PRs y líneas*. Comparamos dos políticas: optimizar el valor y optimizar la proxy.

```python
import random

def generar_pr(politica):
    """Cada 'unidad de esfuerzo' produce un PR según lo que se optimiza."""
    if politica == "valor":
        utilidad = random.uniform(0.5, 1.0)    # se elige trabajo útil
        verificacion = random.uniform(0.6, 1.0) # y se verifica en serio
        n_prs, lineas = 1, random.randint(40, 200)
    else:  # política "proxy": maximizar conteo
        utilidad = random.uniform(0.0, 0.6)    # lo útil da igual: cuenta igual
        verificacion = random.uniform(0.1, 0.5) # verificar no puntúa
        n_prs, lineas = random.randint(2, 5), random.randint(300, 900)
    proxy = n_prs * 10 + lineas * 0.1
    valor = utilidad * verificacion * 100
    # la deuda: el PR mal verificado genera retrabajo futuro (resta valor)
    deuda = (1 - verificacion) * 30
    return proxy, valor - deuda

for politica in ("valor", "proxy"):
    p, v = zip(*(generar_pr(politica) for _ in range(1000)))
    print(f"política {politica:6s} → métrica visible: {sum(p)/1000:6.1f}   "
          f"valor real: {sum(v)/1000:6.1f}")
```

Los números concretos son de juguete; la estructura no: en cuanto la proxy es más fácil de mover que el valor (siempre lo es — por eso es proxy), **la política que la maximiza gana el marcador y pierde el partido**. Añade una tercera política con guardarraíl (`si verificacion < 0.6, el PR no puntúa`) y verás el mecanismo de defensa en acción: el guardarraíl no arregla la proxy — la encarece de falsear.

La versión seria de esta simulación se llama *reward hacking* y es un área activa de la seguridad en IA: los agentes optimizan literalmente lo que su función de recompensa dice, con celo goodhartiano perfecto. Que la misma matemática describa a un modelo de lenguaje y a una empresa bajo bonus trimestral no es una coincidencia: es la razón por la que este capítulo existe.

## 2. El panel mínimo viable de un equipo

Si mañana te toca proponer «qué medimos», esta es la configuración más pequeña que respeta todo lo aprendido — cuatro capas, una pantalla:

1. **Flujo (sistema, para el equipo):** lead time en percentiles (P50/P85), throughput semanal, WIP actual, aging de lo abierto. Fuente: el tracker que ya tienes; coste: un script. Uso: la daily y la retro. Prohibición escrita: no comparar equipos, no evaluar personas.
2. **Calidad (guardarraíles):** tasa de fallo de cambios (¿qué % de despliegues requiere remedio?), tiempo de restauración, reaperturas, y — en la era de agentes — churn de código temprano (líneas reescritas a los pocos días de escribirse) y duplicación. Estas existen para que la capa 1 no pueda «mejorar» haciendo trampas.
3. **Outcome (producto):** 2-3 métricas de comportamiento de usuario ligadas a las apuestas activas (uso real de lo entregado, retención, el indicador de la renovación de turno). Es la capa que justifica a las otras dos, y la única que debería subir a un board.
4. **Salud (personas, agregada y anónima):** una encuesta breve y periódica — las dimensiones de SPACE dan el índice: satisfacción, percepción de productividad, fricción — con resultados para el propio equipo. Es el canario: el flujo puede lucir bien seis meses mientras la capa 4 se hunde, y entonces tienes un incendio con contabilidad en orden (la sección 10 tiene los datos de en qué acaba eso).

Tres reglas de operación, todas ya justificadas en la teoría: cada métrica con su pareja tensionada; los números abren conversaciones, no las cierran («el lead time ha subido» es el principio de una pregunta, no un veredicto); y auditoría trimestral del propio panel — qué está incentivando de verdad, qué ha dejado de medir, qué medida ha caducado.

## 3. Tres señales de que tu organización mide para juzgar (aunque diga que no)

Del caso IPA y sus primos, un detector de bolsillo:

- **Los números viajan hacia arriba con nombres propios.** Si el dashboard del equipo llega al comité con columnas por persona — o por equipo en ranking —, es evaluación con disfraz, y la gente lo sabrá antes que tú: la métrica empezará a mentir esa misma semana.
- **Las métricas se anuncian junto a decisiones de plantilla.** Da igual el propósito declarado: el aprendizaje asociativo hace el resto (Aurelia tradujo el IPA en «la próxima lista» sin que nadie lo dijera).
- **Nadie puede explicar qué decisión del equipo cambió por mirar el número.** La prueba del algodón inversa: una métrica sana deja rastro de decisiones («bajamos el WIP al ver el aging», «matamos la feature al ver el uso»). Una métrica que solo se *reporta* no informa: vigila. Y la vigilancia, como toda la sección 1 estableció, es una teoría sobre las personas — la equivocada.

## Para profundizar

- Sobre reward hacking y la conexión Goodhart-IA: Amodei et al., "Concrete Problems in AI Safety" (arXiv, 2016) — lectura sorprendentemente útil para managers: https://arxiv.org/abs/1606.06565
- DORA, "guía de las cuatro métricas y sus trampas" (CC BY 4.0): https://dora.dev/
- Kohavi et al. (2007), OEC y guardrails — PDF: http://ai.stanford.edu/~ronnyk/2007GuideControlledExperiments.pdf
