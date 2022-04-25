import socket
from _thread import *
from time import sleep

from sqlalchemy import true

I = 0


def thread_client(conn):
    thisConnection = 0
    check = 1
    while(True):
        if (check):
            thisConnection = I
            check = 0
        print("the %d client" % (I))
        # send data
        data = "message from server."
        conn.send(data.encode())
        # recieve data
        data = conn.recv(1024).decode()
        print("Client: %s" % (data))
        sleep(5)


try:
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print("Error: %s" % (error))

host = socket.gethostname()
port = 9999

end_point = (host, port)

socketServer.bind(end_point)
listen = socketServer.listen(5)

while (True):
    connect, address = socketServer.accept()
    I = I + 1
    start_new_thread(thread_client, (connect,))


socketServer.close()
