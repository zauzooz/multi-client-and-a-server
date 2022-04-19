import socket
from _thread import *

from sqlalchemy import true

I = 0


def thread_client(conn):
    check = 1
    while(True):
        if (check):
            print("the %d client" % (I))
            check = 0


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
