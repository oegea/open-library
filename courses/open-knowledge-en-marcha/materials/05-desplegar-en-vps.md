Como el modo base de datos guarda estado en disco, quiere lo contrario de
serverless: **una máquina, un disco, una instancia**. Su hogar natural es
un VPS pequeño a precio fijo mensual — lo que también significa **cero
costes variables**: sin facturación por petición, sin sorpresas de ancho de
banda, sin una factura que un atacante o un pico de tráfico puedan inflar.
Unos pocos euros al mes, planos.

## La receta

En cualquier VPS pequeño (1 vCPU y 512 MB de RAM bastan de verdad para
empezar), una Raspberry Pi en una estantería o un servidor casero con
Docker:

```sh
git clone https://github.com/oegea/open-knowledge.git && cd open-knowledge
docker build -t open-knowledge .
docker run -d --name open-knowledge --restart unless-stopped \
  -p 3000:3000 -v ok_data:/data open-knowledge
```

Pon un proxy inverso delante para el HTTPS. Con Caddy es literalmente una
línea — certificados incluidos y renovados solos:

```sh
caddy reverse-proxy --from tu-dominio.ejemplo --to :3000
```

Ahora abre tu dominio y **registra la primera cuenta: se convierte en la
administradora.** Hazlo inmediatamente — en una instancia recién nacida, el
primer registro son las llaves del edificio. Guarda el código de
recuperación en un lugar seguro y fuera de línea; sin correo registrado,
ese código es tu camino de vuelta si pierdes el autenticador.

## La única regla: el volumen

Todo lo que importa vive en `/data`: la base de datos SQLite, cada imagen y
audio subidos, y la clave de cifrado que protege los secretos TOTP en
reposo. De ahí se siguen dos consecuencias:

1. **Monta siempre un volumen persistente en `/data`.** Un contenedor sin
   él lo olvida todo al recrearse.
2. **No ejecutes nunca dos instancias contra los mismos datos.** SQLite
   está construido alrededor de un único escritor; una sola instancia no es
   una limitación que sortear sino el diseño. Y te llevará mucho más lejos
   de lo que esperas — esto es una librería de cursos, no una red social.

## Operación, honestamente pequeña

- **Actualizaciones:** `git pull`, reconstruir la imagen, recrear el
  contenedor con el mismo volumen. Las migraciones corren solas al arrancar
  y son estrictamente aditivas — una actualización jamás reescribe ni borra
  tus datos.
- **Copias de seguridad:** copia el volumen, o pulsa "Descargar copia" en
  el panel para el zip del entorno completo. Y haz lo que hacen los
  operadores con canas: **prueba una restauración** en una instancia de
  usar y tirar, una vez. Una copia que has restaurado es una póliza de
  seguros; una que no, es una esperanza.
- **Plataformas de contenedores** (Fly.io, Railway, Render…) también
  funcionan: monta un volumen persistente en `/data` y mantén exactamente
  una instancia. Ten presente que las plataformas de pago por uso rara vez
  ofrecen topes de gasto duros — un VPS de precio fijo no puede darte
  sustos, y por eso este curso lo recomienda.
- **Sin Docker** es simplemente `pnpm install && pnpm build && pnpm start`
  (Node 20+); el estado vive en `./data`, reubicable con la variable de
  entorno `OK_DATA_DIR`.
