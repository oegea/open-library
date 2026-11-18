La noche de la emergencia, Vicente hizo con una sola batería cuarenta y una gestiones por radio y al amanecer aún le quedaba carga. No fue suerte: sabía cuánta energía tenía y a qué ritmo la estaba gastando. Esta lección te enseña a hacer esa misma cuenta.

Recuerda la diferencia de la lección anterior: la **potencia** es el ritmo al que se gasta (vatios); la **energía** es la cantidad total gastada o disponible. Un ritmo no dice nada del total hasta que sabes cuánto tiempo dura.

## Energía: potencia multiplicada por tiempo

Si la potencia es el ritmo de gasto, la energía total gastada es ese ritmo multiplicado por el tiempo que dura:

**E = P × t**

La energía tiene dos unidades que conviene conocer:

- El **julio (J)**, la unidad oficial, que ya conoces: es la energía que gasta un aparato de 1 vatio durante 1 segundo. Es una unidad muy pequeña: una estufa de 2.000 W gasta 2.000 julios cada segundo.
- El **vatio-hora (Wh)**, la unidad práctica: la energía que gasta un aparato de 1 vatio durante 1 hora. Como una hora tiene 3.600 segundos, **1 Wh = 3.600 J**. Mil vatios-hora son un **kilovatio-hora (kWh)**, que es exactamente lo que te cobra la compañía eléctrica en la factura.

**Ejemplo.** Una estufa de 2.000 W encendida 3 horas gasta E = 2.000 × 3 = 6.000 Wh = 6 kWh.

Fíjate en que el kilovatio-hora no es «kilovatios por hora» ni «kilovatios cada hora»: es kilovatios **multiplicados por** horas. Un ritmo por un tiempo da una cantidad.

## Las baterías: el amperio-hora

La capacidad de una batería no suele venir indicada en vatios-hora, sino en una unidad más cómoda para hacer cuentas: el **amperio-hora (Ah)**.

> Una batería de **60 Ah** puede dar, en teoría, 60 amperios durante 1 hora. O 6 amperios durante 10 horas. O 1 amperio durante 60 horas. En todos los casos, amperios × horas = 60.

Una precisión, para no deshacer lo aprendido en la lección 1: la batería sigue siendo una bomba, no un depósito de electrones. Lo que se le acaba es el combustible químico con el que bombea. Los amperios-hora dicen cuánta carga es capaz de **hacer circular** antes de agotarse. Es la misma idea que el culombio (una corriente multiplicada por un tiempo), pero contando el tiempo en horas: 1 Ah = 1 A × 3.600 s = **3.600 culombios**.

Para saber cuánto dura una batería basta una división:

**Horas de autonomía = capacidad de la batería (Ah) / corriente que consume el aparato (A)**

Si quieres saber cuánta energía guarda una batería, multiplica sus amperios-hora por su tensión (es la fórmula P = U × I con el tiempo dentro: voltios × amperios × horas): una batería de 60 Ah y 12 V almacena 60 × 12 = 720 Wh. Es lo que gasta una estufa de 2.000 W en poco más de veinte minutos, y sin embargo, bien administrado, da para una noche entera de radio. Vamos a verlo.

Antes, una pregunta que el examen hace a veces: ¿qué pasa con la capacidad al juntar baterías? Con dos baterías iguales de 12 V y 60 Ah:

| Conexión | Tensión | Capacidad | Energía total |
|---|---|---|---|
| En serie | 24 V (se suman) | 60 Ah (la de una) | 24 × 60 = 1.440 Wh |
| En paralelo | 12 V (la de una) | 120 Ah (se suman) | 12 × 120 = 1.440 Wh |

En serie se suman los voltios; en paralelo, los amperios-hora. La energía total es la misma en los dos casos, como es lógico: son las mismas dos baterías.

## La cuenta de Vicente, completa

Ya puedes repetir, con todos sus pasos, la cuenta de la noche de la emergencia. Los datos: batería de 60 Ah; la emisora consume 10 A transmitiendo y 0,8 A escuchando.

**Si transmitiera sin parar:**
60 Ah / 10 A = **6 horas**.

**Si solo escuchara:**
60 Ah / 0,8 A = **75 horas**.

**En una noche real**, un operador disciplinado pasa escuchando casi todo el tiempo. Supón que de cada 100 minutos, 95 son de escucha y 5 de transmisión. El consumo medio se calcula repartiendo cada corriente según el tiempo que dura:

- Escucha: 95 minutos a 0,8 A → 95 × 0,8 = 76
- Transmisión: 5 minutos a 10 A → 5 × 10 = 50
- Total: 76 + 50 = 126, repartido entre los 100 minutos: 126 / 100 = **1,26 A de media**

Y con ese consumo medio:
60 Ah / 1,26 A ≈ **48 horas**.

Dos días con una sola batería, frente a las 6 horas de quien no suelta el micrófono. Mira además de dónde sale el consumo: los cinco minutos de transmisión gastan 50 y los noventa y cinco de escucha gastan 76. Hablar cinco minutos cuesta dos tercios de lo que cuesta escuchar más de hora y media. Por eso la regla de Vicente era escuchar mucho y hablar poco y corto.

En la práctica hay que ser más prudente que la cuenta. Una batería de coche se estropea si se descarga por debajo de la mitad, y con los años y con el frío pierde capacidad. Lo sensato es contar con la mitad de lo calculado: unas 24 horas en lugar de 48. Sigue siendo una noche entera y parte del día siguiente, que es lo que Vicente necesitaba. La cuenta da el orden de magnitud, y el orden de magnitud es lo que hace falta para decidir bien cuando no hay otra cosa.

## Donde la gente se lía

- **Confundir vatios y vatios-hora.** Los vatios son un ritmo; los vatios-hora, una cantidad. «Esta batería tiene 100 vatios» no significa nada; «esta batería tiene 100 vatios-hora», sí.
- **Confundir amperios y amperios-hora.** Los amperios dicen cuánta corriente circula ahora mismo; los amperios-hora, cuánta carga puede hacer circular la batería antes de agotarse.
- **Leer «kilovatio-hora» como «kilovatios por hora».** Es kilovatios *multiplicados por* horas.
- **Creer que una batería se puede exprimir entera.** Las cuentas dan el máximo teórico; en la práctica, la mitad.

## Compruébalo tú

1. Una plancha de 800 W funciona durante 5 horas. ¿Cuánta energía gasta, en kWh?
2. Un receptor consume 0,4 A y se alimenta con una batería de 20 Ah. ¿Cuántas horas funcionará, en teoría?
3. Una batería de 12 V y 100 Ah, ¿cuánta energía almacena, en vatios-hora?
4. Conectas en paralelo dos baterías iguales de 12 V y 40 Ah. ¿Qué tensión y qué capacidad tiene el conjunto?
5. Una emisora consume 0,5 A escuchando y 8 A transmitiendo. En una hora escucha 54 minutos y transmite 6. ¿Cuál es su consumo medio? ¿Cuántas horas duraría, en teoría, una batería de 50 Ah?
6. ¿Cuántos culombios puede hacer circular una batería de 2 Ah?

**Soluciones**

1. E = P × t = 800 × 5 = 4.000 Wh = **4 kWh**.
2. 20 Ah / 0,4 A = **50 horas**.
3. E = 100 Ah × 12 V = **1.200 Wh** (1,2 kWh).
4. En paralelo la tensión es la de una sola y las capacidades se suman: **12 V y 80 Ah**.
5. Escucha: 54 × 0,5 = 27. Transmisión: 6 × 8 = 48. Total 75, repartido entre 60 minutos: 75 / 60 = **1,25 A de media**. Autonomía teórica: 50 / 1,25 = **40 horas** (en la práctica, cuenta con unas 20).
6. 1 Ah son 3.600 culombios, así que 2 Ah son 2 × 3.600 = **7.200 culombios**.

## En una frase

La energía es la potencia multiplicada por el tiempo; la capacidad de una batería, en amperios-hora, dividida entre la corriente media que consumes, te dice cuántas horas de voz te quedan.
