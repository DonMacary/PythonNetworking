"""
Author: ELF
Course: Python
version: Python 2.7
FileName: tcpclient.py
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
import sys
#Create a new socket for the client and conenct to the server
#On port 1337
try:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("192.168.31.128",1337))
except Exception,msg:
    print "Error Connection to Server"
    sys.exit()
while True:
    try:
        message = raw_input("Enter a message to send to the server: ")
        s.send(message)
    except KeyboardInterrupt:
        break
#Kill connection to server
print "Killing Connection to Server"
s.close()