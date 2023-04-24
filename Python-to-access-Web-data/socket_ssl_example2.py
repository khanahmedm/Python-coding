#!/usr/bin/python3

import socket, ssl

HOST = "mathworld.wolfram.com"
PORT = 443

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock = context.wrap_socket(s, server_hostname=HOST)
s_sock.connect((HOST, PORT))
s_sock.send("GET / HTTP/1.1\r\nHost: mathworld.wolfram.com\r\n\r\n".encode())

while True:
    data = s_sock.recv(512)
    #print(data, end='')
    if len(data) < 1:
        break
    print(data.decode(), end='')

s_sock.close()
