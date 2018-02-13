from socket import *

class Server():
    def __init__(self, host, port, user_number):
        self.host = host
        self.port = port
        self.user_number = user_number

    def createSocket(self):
        sock = socket(AF_INET, SOCK_STREAM, 0, None)
        sock.bind((self.host, self.port))
        sock.listen(self.user_number)
        return sock

def acceptConnection(server_sock):
    conn, addr = server_sock.accept()
    print(addr, "is connected")
    while True:
        data = str(conn.recv(1024))
        return str(addr[0]) + ":" + str(addr[1]), data[2:-1]
        conn.sendall(data)

class Client():
    def __init__(self, id, data):
        #self.addr = addr
        self.id = id
        self.addr = data[0]
        self.login = data[1]

server = Server("localhost", 8888, 1)
server_sock = server.createSocket()
client1 = Client(1, acceptConnection(server_sock))
print("ID:", client1.id)
print("ADDR:", client1.addr)
print("LOGIN:", client1.login)
