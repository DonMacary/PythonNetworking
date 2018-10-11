"""
Author: ELF
Course: Python
version: Python 2.7
FileName: udpserver.py
Lab2B
Instructions:
    Write a UDP sender that takes a dictionary, turns it into a JSON string, and sends it to a listener.

    Write the UDP receiver to receive the JSON string and turns it back into a dictionary.

    Validate by printing the type of your dictionary variable (build in IPv4).
"""
from socket import *
import json

#Create a dictionary to send
sendDict={1:"Hello", 2:"My", 3:"Name", 4:"Is", 5:"Donnie"}
print sendDict
print type(sendDict)
#Dump the dictionary into a JSON string
dumpJ=json.dumps(sendDict)
print dumpJ
print type(dumpJ)
#Create server socket on port 1337
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("",1337))
print "Server is awaiting connections hit CRTL+C to Exit"
while True:
    #Try to receive connections exit if user presses Ctrl C
    try:
        #If a connection is made send the JSON string
        data, addr = s.recvfrom(1024)
        print "Connection Received from {}: ".format(addr)
        s.sendto(dumpJ, addr)
    #exit loop if user hits ctrl c
    except (KeyboardInterrupt):
        break
print "Closing Server"
s.close()