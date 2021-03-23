import threading
import time
import random

import socket
import sys

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    #read in cmd line arguments
    lsHostName = sys.argv[1]
    lsPort = int(sys.argv[2])

    #connect to the server on local machine
    server_binding = (lsHostName, lsPort)
    cs.connect(server_binding)

    #Read in HNS file to send over
    #Read HNS file and send data over
    data = open('PROJ2-HNS.txt')
    info = data.read()
    infoL = info.lower()
    cs.sendall(infoL.encode('utf-8'))
   


   




    



client()