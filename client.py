import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT = "!DC"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))


message = input("Enter a message to send: ")
send(message)
while message != DISCONNECT:
    message = input("Enter another message to send: ")
    send(message)

        
    
