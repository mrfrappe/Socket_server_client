from socket import *

HOST = 'localhost'
PORT = 8888

s = socket(AF_INET, SOCK_STREAM, 0, None)
s.connect((HOST, PORT))

login = input("Podaj login: ")
    #password = input("Podaj hasło: ")
registry = login
    #E +"%"+ password
s.sendall(bytes(registry,"utf-8"))
data = s.recv(1024)
print('Received', repr(data))
