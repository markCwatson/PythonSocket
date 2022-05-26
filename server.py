import socket
import threading
import time

HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # 192.168.2.40
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    
    time.sleep(0.2)
    print(f"[SERVER] {addr} connected.")

    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[SERVER] Message from {addr}: {msg}")

            conn.send(f"{msg}".encode(FORMAT))

            if msg == DISCONNECT_MESSAGE:
                break

    print(f"[SERVER] {addr} disconnected.")
    conn.close()

def start():
    
    server.listen()
    print(f"[SERVER] Listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[SERVER] Thread count: {threading.active_count() - 1}")


print("[SERVER] Starting...")
start()