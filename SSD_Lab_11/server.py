import socket
import sys
from datetime import datetime
import threading


def con(cli,no_of_clients):
    while True:
        msg = cli.recv(1024)
        msg = msg.decode('ascii')
        if(msg == ""):
            cli.close()
            break
        print("Message from client",no_of_clients,msg)
        if(len(msg) > 0):
            rmsg = msg [::-1]
            cli.send(rmsg.encode())

port = sys.argv[1]
soc = socket.socket()
host = socket.gethostname()
soc.bind((host,int(port)))
soc.listen(5)
no_of_clients = 0


threads= []
while True:

    cli, addr = soc.accept()
    no_of_clients += 1
    print("client",no_of_clients,"connected")
    print("clint connected at ",datetime.now())
    t1 = threading.Thread(target=con, args=(cli,no_of_clients))
    threads.append(t1)
    t1.start()
soc.close()

    