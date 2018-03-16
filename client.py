from socket import *
import time

HOST = 'localhost'
PORT = 5000

s = socket(AF_INET, SOCK_STREAM, 0, None)
s.connect((HOST, PORT))

login = input("Username: ")
s.sendall(login.encode("utf-8"))
while True:
    message = input("Send:")
    data = s.sendall(message.encode("utf-8"))
    if message == "exit":
        break;
s.close()
