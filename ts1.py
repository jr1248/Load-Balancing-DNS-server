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

    store_data = []
    while True:
        data_from_client = csockid.recv(1024)
        query = data_from_client.decode('utf-8')
        print("This is what I recieved",query)
        send_ts1 = table_lookup(query)
        csockid.send(send_ts1.encode('utf-8'))
        if not query:
            break
        

    ss.close();




def table_lookup(query):

    content_array = []

    data = open('PROJ2-DNSTS1.txt')
    
    for line in data:
        temp = line.split(' ')
        content_array.append(temp)

    #search and send to client
    word = ""
    for j in range (0, len(content_array)):
        print("This is what i'm comparing to:" , content_array[j][0])
        print("This is my query:", query)
        if query in content_array[j][0]:
            word = content_array[j][0] + " " + content_array[j][1] + " " + content_array[j][2]
            break;
       
    print("This is the word we reply with:",word)

    return word

server()