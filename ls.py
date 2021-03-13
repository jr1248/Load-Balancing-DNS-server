import threading
import time
import random

import socket
import sys

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    #read in args from cmd line
    lsPort = int(sys.argv[1])
    ts1HostName = sys.argv[2]
    ts1Port = int(sys.argv[3])
    ts2HostName = sys.argv[4]
    ts2Port = int(sys.argv[5])

    server_binding = ('', lsPort)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

   #create new clients to send to servers

    ts1 = create_client()
    ts2 = create_client()
    connection(ts1,ts1HostName,ts1Port)
    connection(ts2,ts2HostName,ts2Port)
    ts1.settimeout(5)
    ts2.settimeout(5)

    while True:
        try:
            data_from_client = csockid.recv(1024)
            query_value = data_from_client.decode('utf-8')
            ts1.send(query_value.encode('utf-8'))
            ts2.send(query_value.encode('utf-8')) 
        except:
            break




def create_client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    return cs;
    
 
def connection(clientName,hostName, port):
    server_binding = (hostName, port)
    clientName.connect(server_binding)




server()