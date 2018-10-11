"""
Author: ELF
Course: Python
version: Python 2.7
FileName: tcpserver.py
Lab2A
Instructions:
    Write a TCP server that receives a string, reverses order of 
    the words, and sends it back to the client.
    Write a TCP client to connect to print the response 
    (build in IPv4).
"""
from socket import *

def reverseString(string):
    """Function which tkaes in a string and return it
    in reverse"""
    #Split the string into a list
    a=string.split()
    #Reverse the order of the list
    a.reverse()
    #Place the elements of the list back into a string separated
    #by spaces
    result=" ".join(a)
    return result

#Create a server socket bound to port 1337
s = socket(AF_INET, SOCK_STREAM)
s.bind(("",1337))
s.listen(5)
print "Server Listening for Incoming Connections press Ctrl+C to Exit"
while True:
    #Trys to take in a new connection unless CTRL C is pressed
    try:
        #Accepts new socket and prints the address
        c,a = s.accept()
        print "Connection found from: {}".format(a)
        #Receive string from client
        data = c.recv(1024)
        #Make sure the data sent was a string and reverse it
        if isinstance(data, str) == True:
            data=reverseString(data)
        else:
            print "Information Received is not a string"
        #Send the reversed string back and close the connection
        c.send(data)
        c.close()
    #If user hits ctrl c then esccape the loop
    except (KeyboardInterrupt):
        break
#Close the server safely
print "Server Terminating"
s.close()

