import socket

try:
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print("Error: %s" % (error))

host = socket.gethostname()
port = 9999
end_point = (host, port)

socketClient.connect(end_point)

while (True):
    pass

socketClient.close()
