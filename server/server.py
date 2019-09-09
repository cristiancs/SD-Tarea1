
import socket
from _thread import *
import threading


TCP_IP = '0.0.0.0'
TCP_PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)
write_lock = threading.Lock()


def handle_client(c, client_address):
    while True:

        # data received from client
        data = c.recv(1024)
        if not data:
            c.close()
            break
        data = data.decode('utf-8').strip()
        write_lock.acquire()
        logs = open("log.txt", "a")
        logs.write(":".join(map(str, client_address)) + " | "+data+"\n")
        print(data)
        logs.close()
        write_lock.release()

        respuesta = "Exito\n"
        # Respuesta
        c.send(respuesta.encode("utf-8"))
       
    # connection closed


while True:
    connection, client_address = s.accept()
    print('connection from', client_address)
    start_new_thread(handle_client, (connection, client_address,))
