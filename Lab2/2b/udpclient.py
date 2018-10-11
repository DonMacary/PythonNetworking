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

#Create client socket
s = socket(AF_INET, SOCK_DGRAM)
message = "Connect"
#Send a connection message to server
s.sendto(message, ("192.168.31.128", 1337))
#Receive data from server print the data and its type
data, addr = s.recvfrom(1024)
print type(data)
#Convert JSON string to python dictionary
messageLoaded=json.loads(data)
print messageLoaded
print type(messageLoaded)
s.close()
print "Connection Terminated"
