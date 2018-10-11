"""
Author: ELF
Course: Python
version: Python 2.7
FileName: udpReceiver.py
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
        print data
        orderWords=data.split()
        orderWords.sort(key=len, reverse=True)
        newString=" ".join(orderWords)
        print newString
        newaddr=(addr[0],addr[1]+1)
        print newaddr
        #Send the Data back 
        d=socket(AF_INET, SOCK_DGRAM)
        d.sendto(newString, newaddr)
        d.close()
    #exit loop if user hits ctrl c
    except (KeyboardInterrupt):
        break
print "Closing Server"
s.close()
