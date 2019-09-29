# Actividad 1

Se encuentra en la carpeta parte1, dentro de esto las rutas y comandos son los siguientes

## Rutas

### Logs Cliente

    client/respuestas.txt

### Logs Servidor

    server/logs.txt

## Uso

### Iniciar

    docker-compose up

Tanto el cliente como el servidor se ejecutaran en primer plano, el cliente enviara un mensaje al servidor, el servidor responderá y ambos cerraran la conexión.

Para pararlo, se debe presionar dos veces ctrl + c (Forzar cierre)

### Borrar

    docker-compose down

# Actividad 1

Se encuentra en la carpeta parte2, dentro de esto las rutas y comandos son los siguientes

## Rutas

### Logs headnode (Ubicación guardado archivo)

    headnode/registro_server.txt.txt

### Logs headnode (Respuestas Heartbeat)

    headnode/hearbeat_server.txt

### Archivos datanode i

    datanode{i}/data.txt

## Uso

### Iniciar

    docker-compose up

Se inician los 3 datanode y el headnode en primer plano, el cliente enviara un mensaje al servidor, el servidor responderá y el cliente cierra la conexión

Para pararlo, se debe presionar dos veces ctrl + c (Forzar cierre)

### Borrar

    docker-compose down
