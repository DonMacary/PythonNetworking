"""
Author: ELF
Course: Python
version: Python 2.7
FileName: chatServer.py
Bonus Lab 3
Instructions:
    Create a simple TCP chat server that connects to multiple clients
    using IPv4 and either Select() or Threading. Then echo back data 
    to all clients using broadcasts (Use multiple VM's and track 
    traffic in Wireshark).
""" 
import socket
import sys
from thread import *

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 1337 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

#Start listening on socket
s.listen(10)
print 'Socket now listening'

list_of_clients = []
#Function for handling connections. This will be used to create threads
def clientthread(conn, addr):
    #Sending message to connected client
    conn.send('Welcome to Homestar Runner.com Its DOT COM!\n') #send only takes string

    #infinite loop so that function do not terminate and thread do not end.
    while True:
        try:
            message = conn.recv(2048) 
            if message:
                
                """prints the message and address of the 
                user who just sent the message on the server 
                terminal"""
                print "<" + addr[0] + "> " + message 

                # Calls broadcast function to send message to all 
                message_to_send = "<" + addr[0] + "> " + message 
                broadcast(message_to_send, conn)

            else: 
                remove(conn) 
        except: 
                continue

    #came out of loop

    conn.close()

"""Using the below function, we broadcast the message to all 
clients who's object is not the same as the one sending 
the message """
def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                clients.send(message) 
            except: 
                clients.close() 

                # if the link is broken, we remove the client 
                remove(clients)

def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 

while True: 
    conn, addr = s.accept() 

    """Maintains a list of clients for ease of broadcasting 
    a message to all available people in the chatroom"""
    list_of_clients.append(conn) 

    # prints the address of the user that just connected 
    print addr[0] + " connected"

    # creates and individual thread for every user  
    # that connects 
    start_new_thread(clientthread,(conn,addr))

conn.close() 
s.close()