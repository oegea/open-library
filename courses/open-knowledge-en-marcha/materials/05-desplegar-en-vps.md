Como el modo base de datos guarda estado en disco, quiere lo contrario de
serverless: **una máquina, un disco, una instancia**. Su hogar natural es un
VPS pequeño a precio fijo mensual — lo que también significa **cero costes
variables**: nadie puede inflarte la factura con tráfico.

**La receta.** En cualquier VPS pequeño (1 vCPU / 512 MB sobra para
empezar), una Raspberry Pi o un servidor casero con Docker:

```sh
git clone https://github.com/oegea/open-knowledge.git && cd open-knowledge
docker build -t open-knowledge .
docker run -d --name open-knowledge --restart unless-stopped \
  -p 3000:3000 -v ok_data:/data open-knowledge
```

Pon un proxy inverso delante para el HTTPS — con Caddy es una línea:

```sh
caddy reverse-proxy --from tu-dominio.ejemplo --to :3000
```

Abre tu dominio y **registra la primera cuenta: se convierte en la
administradora**. Guarda su código de recuperación en lugar seguro — sin
correo registrado, ese código es tu camino de vuelta.

**La única regla: el volumen.** Todo lo que importa — base de datos, medios
subidos, la clave de cifrado que protege los secretos TOTP — vive en
`/data`. Monta siempre un volumen persistente ahí, y no ejecutes nunca dos
instancias contra los mismos datos (SQLite quiere un único escritor).

**Operación, honestamente pequeña:**

- *Actualizaciones:* `git pull`, reconstruir la imagen, recrear el
  contenedor con el mismo volumen. Las migraciones corren solas y son
  aditivas.
- *Copias de seguridad:* copia el volumen — o pulsa "Descargar copia" en el
  panel, que produce un zip capaz de restaurar todo tu entorno en cualquier
  instancia nueva. Prueba una restauración una vez; tu yo del futuro te lo
  agradecerá.
- *Plataformas de contenedores* (Fly.io, Railway, Render…) también
  funcionan si montas un volumen persistente en `/data` y mantienes una
  sola instancia. Ojo: las plataformas de pago por uso rara vez ofrecen
  topes de gasto; un VPS de precio fijo no puede darte sustos.
