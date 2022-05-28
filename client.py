import socket
import pickle
import time
import random

HEADER_SIZE = 5
FORMAT = "utf-8"

ID = int(random.random()*1000)
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg(data):

    message = pickle.dumps(data)
    message = bytes(f'{len(message):<{HEADER_SIZE}}', FORMAT) + message
    client.send(message)
    print(f"[CLIENT] message sent to server: {data}")

for i in range(3):
    
    data = {"ID":ID, "IP":SERVER, "port":PORT, "time":time.strftime("%H:%M:%S"), "data":f'this is data {i}', "disconnect":False}
    send_msg(data)
    time.sleep(2)

data = {"ID":ID, "IP":SERVER, "port":PORT, "time":time.strftime("%H:%M:%S"), "data":None, "disconnect":True}
send_msg(data)
