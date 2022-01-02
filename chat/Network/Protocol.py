import base64
import hashlib

class Protocol:
    # send message
    def send_mes(conn, message):
        encoded = message.encode()
        mes_base64 = base64.b64encode(encoded)
        hashed = hashlib.sha256(mes_base64).hexdigest()

        conn.send(hashed.encode())
        conn.send("\n".encode())

        conn.send(mes_base64)
        conn.send("\n".encode())
        

    # receive message
    def recv_mes(conn):
        mes = ""
        hash_sha256 = ""

        while "\n" not in hash_sha256:
            message = conn.recv(1).decode()
            hash_sha256 += message
        
        while "\n" not in mes:
            mes_b64 = conn.recv(1).decode()
            mes += mes_b64
        
        mes_b64 = base64.b64decode(mes.encode())
        return mes_b64.decode()

if __name__ == "__main__":
    Protocol()