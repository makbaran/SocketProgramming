import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT = "!DC"

# print(SERVER)
# print(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.SOCK_STREAM )
server.bind(ADDR)

def handleClient(conn, addr):
    print(f"New connection: {addr} connected\n")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            if (msg == DISCONNECT):
                connected = False
                print("Server disconnecting...")
            
            conn.send("Msg received".encode(FORMAT))
    
    conn.close()

    

def start():
    server.listen()
    print(f"Listening... {SERVER}\n")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.active_count() -1}\n")
        

print("Server starting...")
start()


