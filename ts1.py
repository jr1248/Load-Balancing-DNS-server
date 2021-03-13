import os
import socket
import sys
import threading

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    #read in args from cmd line
    ts1Port = int(sys.argv[1])
    server_binding = ('', ts1Port)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    while True:
        try:
            data_from_client = csockid.recv(1024)
            query_value = data_from_client.decode('utf-8')
            print(query_value)

            #send_to_client = table_lookup(query_value)
            #cssockid.send(send_to_client.encode('utf-8'))
        except:
            break



def table_lookup(query):

    content_array = []

    data = open('PROJ2-DNSTS1')
    
    for line in data:
        temp = line.split(' ')
        content_array.append(temp)

    #search and send to client
    for i in range (0, len(content_array)):
        if query == content_array[j][0]:
            word = content_array[j][0] + " " + content_array[j][1] + " " + content_array[j][2]

    return word

server()