import socket
import threading
import time
import pickle

HEADER_SIZE = 5
MESSAGE_PACKET_SIZE = 32
FORMAT = "utf-8"

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    
    time.sleep(0.2)
    print(f"[SERVER] {addr} connected at " + time.strftime("%H:%M:%S"))
    full_msg = b''
    new_msg = True

    while True:
        
        msg = conn.recv(MESSAGE_PACKET_SIZE)

        if new_msg is True:
            msg_length = int(msg[:HEADER_SIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADER_SIZE >= msg_length:
            data = pickle.loads(full_msg[HEADER_SIZE:])
            print(f"[SERVER] Message from {addr}: {data}")
            full_msg = b''
            new_msg = True
            
            if data["disconnect"] is True:
                break

    print(f"[SERVER] {addr} disconnected at " + time.strftime("%H:%M:%S"))
    conn.close()

def start():
    
    server.listen()
    print(f"[SERVER] Listening on {SERVER} at " + time.strftime("%H:%M:%S"))

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[SERVER] Thread count: {threading.active_count() - 1}")


print("[SERVER] Starting...")
start()
