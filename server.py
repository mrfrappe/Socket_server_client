
from socket import *
import threading

class Server():
    def __init__(self, host, port, user_number):
        self.host = host
        self.port = port
        self.user_number = user_number
        self.threads = []

    def createSocket(self):
        sock = socket(AF_INET, SOCK_STREAM, 0, None)
        sock.bind((self.host, self.port))
        sock.listen(self.user_number)
        return sock

    def run(self):
        i = 0
        server_sock = self.createSocket()
        conn, addr = server_sock.accept()
        data = str(conn.recv(1024))
        print(addr, "is connected")
        c = Client(1, addr, data)
        print("ID:", c.id)
        print("ADDR:", c.addr)
        print("LOGIN:", c.login)
        c.start()
        self.threads.append(c)

class Client(threading.Thread):
    def __init__(self, id, addr, data):
        threading.Thread.__init__(self)
        self.id = id
        self.addr = str(addr[0]) + ":" + str(addr[1])
        self.login = data[2:-1]

server = Server("localhost", 8888, 2)
server.run();
