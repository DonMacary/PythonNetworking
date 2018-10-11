"""
Author: ELF
Course: Python
version: Python 2.7
FileName: udpSender.py
Lab3B
Instructions:
    Write a UDP receiver that receives a string, and orders the words from longest to shortest in a new string.
    That new string should be sent to the remote port+1.
    (i.e. the source port of message from the SENDER's POV)
    Write a UDP sender that sends the initial string, and receives the response from the receiver above (you can use multiple receivers or combine them).
    Hint: The second step is intentionally ambiguous on how to proceed. There are multiple solutions.
"""
from socket import *
import struct

#Create client socket
s = socket(AF_INET, SOCK_DGRAM)
#Create a string to send
stringtoSend="Mitchell, I'm Sorry about Goose... Everybody Liked him. I'm Sorry"
#Send a connection message to server
s.sendto(stringtoSend, ("192.168.31.128", 1337))
myAddr=s.getsockname()
s.close()

#Open a new socket to receive the information back
s = socket(AF_INET, SOCK_DGRAM)
s.bind((myAddr[0],myAddr[1]+1))
#Receive the data from the Receiver
data, addr = s.recvfrom(1024)
print "Connection Received from {}: ".format(addr)
print data
s.close()