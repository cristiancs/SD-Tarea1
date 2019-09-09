import socket


TCP_IP = '172.16.1.100'
TCP_PORT = 5000
BUFFER_SIZE = 1024

log = open("respuestas.txt", "a")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send("Saludos\n".encode("utf-8"))
data = s.recv(BUFFER_SIZE)
data = data.decode('utf-8').strip()
log.write(data+"\n")
log.close()
s.close()
