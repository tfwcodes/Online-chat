import socket
import threading
from Network.Protocol import Protocol

ip = input("Enter the ip to connect: ")
nickname = input("Enter your nickname: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 5555))

class Receive:
    def receive():
        while True:
            mes = Protocol.recv_mes(s)
            if mes == "NICK":
                Protocol.send_mes(s, nickname)
            else:
                print(mes)

class Write:
    def write():
        while True:
            message = "{}: {}".format(nickname, input(""))
            Protocol.send_mes(s, message)

t = threading.Thread(target=Receive.receive)
t.start()

t2 = threading.Thread(target=Write.write)
t2.start()