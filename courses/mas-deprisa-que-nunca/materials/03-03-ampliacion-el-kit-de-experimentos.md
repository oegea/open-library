La teoría estableció el porqué; esta ampliación es el taller: los tipos de experimento ordenados por coste, la letra pequeña estadística de los «5 usuarios» y del modelo de Kano, y el detalle que separa un experimento de un autoengaño con gráficas: el criterio de éxito preregistrado.

## 1. La escalera de experimentos, de una tarde a un trimestre

Ordenados por coste creciente — y la regla de oro es subir por la escalera solo cuando el peldaño anterior no haya matado la hipótesis:

1. **Análisis de datos existentes** (horas). Como el script de Nadia: la telemetría, los tickets de soporte, los logs de búsqueda interna («¿qué buscan los usuarios que no encuentran?»). Es el único experimento gratis y suele ser el más ignorado.
2. **Entrevistas de comportamiento pasado** (días). Con las reglas de la teoría: específico, conductual, pasado. Cinco entrevistas malas («¿te gustaría…?») valen cero; cinco buenas («enséñame la última vez que…») reorientan un trimestre.
3. **Puerta pintada / fake door** (una tarde). El botón de lo que no existe, midiendo clics. Variantes: página de aterrizaje con registro, entrada en el menú, email anunciando la «próxima» capacidad. Servidumbre ética: revelar pronto, no hacerlo con cosas sensibles (imagina una puerta pintada de «videollamada con su familiar» en Nido), y dar algo a cambio del clic.
4. **Mago de Oz y conserje** (días-semanas). El servicio funciona de verdad, pero por detrás lo hacen personas: el «resumen semanal generado por IA» que en el piloto escriben dos humanos (mago de Oz: el usuario no lo sabe), o el proceso entero hecho a mano para tres clientes (conserje: el usuario lo sabe). Miden lo más valioso: uso real repetido, sin construir el sistema.
5. **Prototipo con las personas del flujo real** (días). El experimento de las gobernantas: no «¿te gusta la pantalla?» sino «¿qué harías con esto el martes a las 7:40?». La pregunta que hundió los resúmenes — ¿quién revisa esto y cuándo? — solo aparece con la gente que vive el flujo.
6. **A/B test en producción** (semanas, y exige tráfico). El estándar de oro para efectos pequeños en producto vivo. Con dos avisos de Kohavi: define la métrica de decisión (**OEC**, overall evaluation criterion) *antes*, y acompáñala de **guardrails** — métricas que no pueden empeorar (latencia, errores, bajas) — porque casi cualquier cosa puede «ganar» si eliges la métrica después (la sección 8 vuelve sobre esto).

Con volúmenes B2B pequeños — Nido tiene cientos de residencias, no millones de usuarios — los A/B clásicos casi nunca alcanzan potencia estadística, y no pasa nada: los peldaños 1-5 deciden la mayoría de hipótesis. El error de manual es el inverso: empresas con millones de eventos decidiendo por corazonada de comité.

## 2. «Cinco usuarios bastan»: el modelo y su letra pequeña

La regla más citada de la investigación de usabilidad — con 5 usuarios encuentras ~85% de los problemas — tiene origen respetable: **Nielsen y Landauer (1993)** modelaron el descubrimiento de problemas como proceso de Poisson, Found(i) = N(1 − (1 − λ)^i), y con la λ media que estimaron (~0,31), cinco usuarios dan ~85%. El problema es la varianza que la regla esconde:

- **Spool y Schroeder (2001)**, en sitios reales de e-commerce: los 5 primeros participantes descubrieron ~35% de los problemas; seguían apareciendo problemas nuevos en el participante 18. λ no es una constante de la naturaleza: cae con la complejidad del producto y de las tareas.
- **Faulkner (2003)**, con 60 usuarios y remuestreo: los grupos de 5 encontraron **de media** el 85%… con un rango del **55% al 99%**. Con 10 usuarios el mínimo sube al 80%; con 20, al 95%.

La lectura madura no es «5 es mentira» sino «5 es una media con varianza enorme». Y la recomendación económica de Nielsen sobrevive con otra forma: **mejor 3 rondas de 5 con iteración entre medias que 1 ronda de 15** — porque cada ronda corrige y el siguiente lote explora el diseño ya mejorado. Lo que no sobrevive es usar «ya probamos con 5» como certificado de ausencia de problemas.

Puedes ver la varianza tú mismo, que para eso eres developer:

```python
import random

N_PROBLEMAS = 30
random.seed(7)
# a cada problema, una detectabilidad distinta (esto es lo que la regla del 5 ignora)
detectabilidad = [random.betavariate(2, 6) for _ in range(N_PROBLEMAS)]

def encuentra(n_usuarios):
    return sum(
        1 for p in detectabilidad
        if any(random.random() < p for _ in range(n_usuarios))
    )

for n in (5, 10, 20):
    tasas = sorted(encuentra(n) / N_PROBLEMAS for _ in range(2000))
    print(f"{n} usuarios → mediana {tasas[1000]:.0%}, "
          f"peor 5%: {tasas[100]:.0%}, mejor 5%: {tasas[1900]:.0%}")
```

Ejecútalo y verás el resultado de Faulkner reproducido en miniatura: la mediana con 5 usuarios ronda cifras respetables y la cola inferior es alarmante.

## 3. Kano, con su letra pequeña

El **modelo de Kano** (Kano, Seraku, Takahashi y Tsuji, 1984 — publicado en japonés; no existe traducción abierta oficial) clasifica atributos de producto en: **básicos** (su ausencia indigna, su presencia no se nota: que Nido no pierda la sesión), **de rendimiento** (más es mejor, linealmente: velocidad de carga), **atractivos** (*delighters*: nadie los pide, encantan al aparecer), indiferentes e inversos. Dos ideas suyas envejecen muy bien: los atributos **migran** (el delighter de hoy es el básico de mañana — la foto semanal de las actividades empezó siendo sorpresa y hoy es exigible), y la inversión en básicos ausentes rinde más que la inversión en delighters extra — exactamente la lista de tres folios de Encarna frente al roadmap de Atlas.

La letra pequeña: la investigación metodológica seria (Mikulić y Prebežac, 2011) muestra que las distintas técnicas de clasificación **asignan los mismos atributos a categorías distintas** — la fiabilidad del cuestionario funcional/disfuncional de Kano es cuestionable. Úsalo como **lenguaje para conversar** sobre el portfolio («¿esto es básico o delighter? ¿para quién?»), no como instrumento de medida que decide por ti.

## 4. El preregistro casero: la práctica que lo cambia todo

La ciencia aprendió por las malas (crisis de replicación mediante) que decidir el criterio de éxito *después* de ver los datos invalida el análisis: siempre hay un corte, un segmento, una métrica secundaria donde «funcionó». La versión de producto es idéntica y la solución también: **preregistrar**. Antes de lanzar el experimento, un documento de una página, inmutable, con:

1. La hipótesis en el formato de la teoría (con su condición de fallo).
2. La **métrica de decisión** (una) y sus **guardrails**.
3. El umbral y el plazo («si menos del 25% de las familias activas pulsa la puerta pintada en 3 semanas, la hipótesis muere»).
4. Qué se hará con cada resultado — incluida la muerte: quién comunica que no, y a quién.

El punto 4 es el más importante y el menos practicado. En Aurelia funcionó porque Marga aceptó de antemano el trato («si dice que no, nos hemos ahorrado tres meses»); sin ese acuerdo previo, el resultado negativo entra en la trituradora política y sale convertido en «bueno, pero el test no era concluyente». La sección 9 le pondrá nombre a esa trituradora (escalada de compromiso) y evidencia a su antídoto (reglas de parada pactadas antes, evaluadas por alguien distinto de quien propuso).

Una nota final sobre la era de los agentes: generar el prototipo, la puerta pintada o el análisis de telemetría cuesta hoy horas donde costaba semanas — la IA ha abaratado espectacularmente el *peldaño*, no la *escalera*. Saber qué hipótesis merece testarse, con qué criterio muere y qué se hace con el cadáver sigue costando lo mismo: pensamiento. Ese desequilibrio nuevo — pruebas baratas, criterio caro — es un anticipo del argumento central de la sección 13.

## Para profundizar

- Nielsen, J. — "Why You Only Need to Test with 5 Users" (y por qué leerlo con esta ampliación al lado): https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/
- Faulkner, L. (2003). "Beyond the five-user assumption" — PDF: https://link.springer.com/content/pdf/10.3758/BF03195514.pdf
- Kohavi, Tang & Xu (2020). *Trustworthy Online Controlled Experiments* — libro de pago; el capítulo de OEC/guardrails está anticipado en el paper KDD 2007 (enlace en la teoría).
- Murphy et al. (2005). Meta-análisis del sesgo hipotético — working paper: https://people.umass.edu/resec/workingpapers/documents/resecworkingpaper2004-9.pdf
