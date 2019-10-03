import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

log = open("registro_cliente.txt", "a")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
mensaje = input("Ingrese mensaje o SALIR para salir: ")
while mensaje != "SALIR":
    s.send((mensaje).encode("utf-8"))
    data = s.recv(BUFFER_SIZE)
    data = data.decode('utf-8').strip()
    log.write(data+"\n")

    mensaje = input("Ingrese mensaje o SALIR para salir: ")
log.close()
s.close()
