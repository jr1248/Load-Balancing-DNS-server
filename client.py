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

    i = 0
    while i < len(word_array):
        cs.sendall(word_array[i][0].encode('utf-8'))
        data_from_server = cs.recv(1024)
        response = data_from_server.decode('utf-8')
        if(response != None):
            i+=1
            print(response)
            print(i)
        else:
            cs.sendall(word_array[i][0].encode('utf-8'))
            print('sent')

       

    #while i < len(word_array)
        #send 
        #if(recv != null)
            #i++








    



client()