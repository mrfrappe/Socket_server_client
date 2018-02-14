from socket import *

HOST = 'localhost'
PORT = 8888

s = socket(AF_INET, SOCK_STREAM, 0, None)
s.connect((HOST, PORT))

login = input("Username: ")
s.sendall(bytes(login.encode("utf-8"))
#if recive usercreate go to while loop
while True:
    message = input("Send:")
    data = s.sendall(message.encode("utf-8"))
    if message == "exit":
        break;
s.close()
