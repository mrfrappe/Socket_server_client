from socket import *

HOST = "localhost"
PORT = 8888

with socket(AF_INET, SOCK_STREAM, 0, None) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print("Connected by",  addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
