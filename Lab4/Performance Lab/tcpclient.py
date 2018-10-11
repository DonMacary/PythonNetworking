"""
Author: ELF
Course: Python
version: Python 2.7
FileName: tcpclient.py
Performance Lab
Instructions:
    Create a TCP client using IPv4. Pack the following values in a 
    struct using network byte order: 12345, 56789, &, *, 0x7d0,
    0b11111010000. Then send the packed struct to a TCP server 
    and print the unpacked values.    

"""
from socket import *
import struct
#Create a new socket for the client and conenct to the server
#On port 1337
s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.31.128",1337))
resp = s.recv(1024)
print resp
#Pack Values and send to server
msg = struct.pack("!iiccii", 12345,56789,'&','*',0x7d0,0b11111010000)
s.send(msg)
#Kill connection to server
print "Killing Connection to Server"
s.close()