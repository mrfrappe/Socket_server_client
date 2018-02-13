from socket import *

HOST = 'localhost'
PORT = 8888

with socket(AF_INET, SOCK_STREAM, 0, None) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))
