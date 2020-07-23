import socket

#first message to the server contains the lenght of the message
first_msg = 16
#free port from the system
PORT = 80
#Message for disconnecting from the server
DISCONNECT_MESSAGE = "The client has been disconnected from the server!"
ADDRESS = (socket.gethostbyname(socket.gethostname()), PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDRESS)

def file(msg: str):
    pass



def send(msg: str):
    try:
        message = msg.encode('utf-8')
        print(msg)
        msg_length = len(message)
        send_length = str(msg_length).encode('utf-8')
        send_length += b' ' * (first_msg - len(send_length))
        s.send(send_length)
        s.send(message)
        print(s.recv(2048).decode('utf-8'))
    except socket.error:
        print("The connection is closing!!!!")


while True:
    try:
        msg = input("Message: ")
        if not msg:
            print("[EXITING] You are exiting the server ")
            send(DISCONNECT_MESSAGE)
            break
        send(msg)
        input()
    except socket.error:
        print("[ERROR] You're exiting the server ......")
        break
