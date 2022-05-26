import socket

HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # 192.168.2.40
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg(msg):

    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(f"[CLIENT] echo from server: {client.recv(1024).decode(FORMAT)}")

send_msg("hello")
input()
send_msg("disconnect")