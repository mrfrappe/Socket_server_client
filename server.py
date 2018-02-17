
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
        running = True
        server_sock = self.createSocket()
        conn, addr = server_sock.accept()
        while running:
            data = str(conn.recv(1024))
            c = Client(conn, addr, data)
            print("ID:", c.id, end =" ")
            print("ADDR:", c.addr, end = " ")
            print("LOGIN:", c.login)
            c.start()
            self.threads.append(c)
            for t in self.threads:
                t.join()
        conn.close()


class Client(threading.Thread):
    def __init__(self, conn, addr, data):
        threading.Thread.__init__(self)
        self.conn = conn
        self.id = threading.get_ident()
        self.addr = str(addr[0]) + ":" + str(addr[1])
        self.login = data[2:-1]

    def run(self):
        login = True
        while login:
            message = str(self.conn.recv(1024))
            print(self.login + ":", message[2:-1])
            if message[2:-1] == "exit":
                login = False


server = Server("localhost", 8888, 2)
server.run()
