import socket
import threading
from Network.Protocol import Protocol
ip_to_listen = input("Enter the ip to listen: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip_to_listen, 5555))
s.listen()
print("Listening...")

clients = []
nicknames = []

class Broadcast:
    def broadcast(message):
        for client in clients:
            Protocol.send_mes(client, message)

class Handling:
    def handle_client(socket):
        while True:
            try:
                mes = Protocol.recv_mes(socket)
                Broadcast.broadcast(mes)
            except:
                pass
class Server:
    def server():
        while True:
            conn, addr = s.accept()
            clients.append(conn)
            print("Connection from {}".format(addr))

            Protocol.send_mes(conn, "NICK")
            nickname = Protocol.recv_mes(conn)
            nicknames.append(nickname)
            Broadcast.broadcast("{} has joined the chat!".format(nickname))

            thread = threading.Thread(target=Handling.handle_client, args=(conn,))
            thread.start()

Server.server()