import socket
from _thread import *
import threading
from random import randrange
import struct
import time
from datetime import datetime


TCP_IP = '0.0.0.0'
TCP_PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)
send_lock = threading.Lock()

BUFFER_SIZE = 1024

ips_nodes = ['172.16.1.101',  '172.16.1.102', '172.16.1.103']
nodes_active = [False, False, False]


def handle_client(c, client_address):
    global nodes_active
    while True:
     # Leer data del cliente
        data = c.recv(1024)
        if not data:
            print("Closing connection with", client_address)
            c.close()
            break
        # Elegir nodo activo
        node = randrange(3)
        while not nodes_active[node]:
            #print("Cheking if node ", node, "is active")
            node = randrange(3)
        print("Seleccionado nodo ", node)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((ips_nodes[node], TCP_PORT))

        s.send(data)

        response = s.recv(BUFFER_SIZE)
        response = response.decode('utf-8').strip()
        if response == "SUCCESS":
            logs = open("registro_server.txt", "a")
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            logs.write("["+dt_string+"] Guardado en datanode " +
                       (str(node+1))+"\n")
            logs.close()
            respuesta = "Guardado en datadone  "+(str(node+1))+"\n"
            # Respuesta
            c.send(respuesta.encode("utf-8"))


def operational():
    global nodes_active
    message = b'Operativo?'
    multicast_group = ('224.3.29.71', 10000)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.settimeout(1)

    ttl = struct.pack('b', 2)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    try:
        while True:
            time.sleep(5)
            for i in range(len(nodes_active)):
                nodes_active[i] = False
            sent = sock.sendto(message, multicast_group)
            while True:

                try:
                    data, server = sock.recvfrom(1024)
                    response = data.decode('utf-8').strip()

                    server = response.split("-D")
                    server = int(server[-1])-1
                    nodes_active[server] = True

                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    logs2 = open("hearbeat_server.txt", "a")
                    logs2.write("["+dt_string+"] "+response+"\n")
                    logs2.close()
                except socket.timeout:
                    break

    finally:
        print('closing socket')
        logs2.close()
        sock.close()


start_new_thread(operational, ())

while True:
    connection, client_address = s.accept()
    print('connection from', client_address)
    start_new_thread(handle_client, (connection, client_address,))
