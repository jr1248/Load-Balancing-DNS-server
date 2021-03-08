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
    ts1Port = sys.argv[3]
    ts2HostName = sys.argv[4]
    ts2Port = sys.argv[5]

    server_binding = ('', rsPort)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))


server()