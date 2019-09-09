
import socket
from _thread import *
import threading


logs = open("log.txt", "w")

TCP_IP = '0.0.0.0'
TCP_PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)
print_lock = threading.Lock()
write_lock = threading.Lock()


def handle_client(c, client_address):
    while True:

        # data received from client
        data = c.recv(1024)
        data = data.decode('utf-8').strip()
        write_lock.acquire()
        logs = open("log.txt", "a")
        logs.write(":".join(map(str, client_address)) + " | "+data+"\n")
        logs.close()
        write_lock.release()

        respuesta = "Exito\n"
        # Respuesta
        c.send(respuesta.encode("utf-8"))

    # connection closed
    c.close()


while True:
    connection, client_address = s.accept()
    print_lock.acquire()
    print('connection from', client_address)
    print_lock.release()
    start_new_thread(handle_client, (connection, client_address,))

    # Clean up the connection
