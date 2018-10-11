"""
Author: ELF
Course: Python
version: Python 2.7
FileName: tcpserver.py
Lab3A
Instructions:
    Using the struct package from the python library, pack the values (1, 2, -3, -4) as the following data types (unsigned short, unsigned int, signed short, signed int)
    1 as an unsigned short
    2 as an unsigned int
    -3 as a signed short
    -4 as a signed int
    Write a TCP client that packs those values, sends the packed string to a server.
    Write a TCP server that receives the string, unpacks it using little endian and prints it, then unpacks it again using big endian and prints it.
"""
from socket import *
import struct

#Create a server socket bound to port 1337
s = socket(AF_INET, SOCK_STREAM)
s.bind(("192.168.31.128",1337))
s.listen(5)
msg="Connection Established"
print "Server Listening for Incoming Connections press Ctrl+C to Exit"
while True:
    #Trys to take in a new connection unless CTRL C is pressed
    try:
        #Accepts new socket and prints the address
        c,a = s.accept()
        print "Connection found from: {}".format(a)
        #Send connection message to client.
        c.send(msg)
        #Receive packed information from client
        data=c.recv(1024)
        #unpack using correct format
        allData=struct.unpack("<HIhi", data)
        print "Correct Data: {}".format(allData)
        #unpack using incorrect format
        wrongData=struct.unpack(">HIhi", data)
        print "Incorrect Data: {}".format(wrongData)
        c.close()
    #If user hits ctrl c then esccape the loop
    except (KeyboardInterrupt):
        break
#Close the server safely
print "Server Terminating"
s.close()