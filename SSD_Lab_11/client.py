import socket
import sys


port = sys.argv[1]
soc = socket.socket()
host = socket.gethostname()
soc.connect((host,int(port)))

while True:
    msg = input("Enter string: ")
    if(msg == "exit"):
        break
    soc.send(msg.encode())
    recmsg = soc.recv(1024).decode('ascii')
    print("Received: ",recmsg)
soc.close()