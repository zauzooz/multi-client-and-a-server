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
    # recieve data
    data = socketClient.recv(1024).decode()
    print("Server: %s" % (data))
    # send data
    data = "message from client."
    socketClient.send(data.encode())

socketClient.close()
