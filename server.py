import socket 
import threading

#first message to the server contains the lenght of the message
first_msg = 16
#free port from the system
PORT = 80
#get the socket server IP address
ADDRESS = (socket.gethostbyname(socket.gethostname()), PORT)
DISCONNECT_MESSAGE = "The client has been disconnected from the server"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDRESS)

def handle_client(conn, addr):
    print(f"[NEW USER] {addr} has been connected.")
    connected = True
    while connected:
        try:
            msg_length = conn.recv(first_msg).decode('utf-8')
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode('utf-8')
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode('utf-8'))
        except socket.error:
            print("[EXITING]You're exiting the server!!!!")
            break
        conn.close()
        

def start():
    s.listen()
    print(f"The IP Address of the server is {socket.gethostbyname(socket.gethostname())}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"There are {threading.activeCount() - 1} active connection in the chat room!!!!")


print("[STARTING] The server is starting...")
start()
