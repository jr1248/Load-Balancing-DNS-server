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
    word_array = []
    with open('PROJ2-HNS.txt') as data:
        for line in data:
            line.lower()
            word_array.append(line.split())

    for i in range(len(word_array)): 
        cs.send(word_array[i][0].encode('utf-8')) #no it says unexpected token len
        print(word_array[i])


   




    



client()