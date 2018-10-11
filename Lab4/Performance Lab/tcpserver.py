"""
Author: ELF
Course: Python
version: Python 2.7
FileName: tcpserver.py
Performance Lab
Instructions:
    Create a TCP client using IPv4. Pack the following values in a 
    struct using network byte order: 12345, 56789, &, *, 0x7d0,
    0b11111010000. Then send the packed struct to a TCP server 
    and print the unpacked values.    

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
        client, address = s.accept()
        print "Connection found from: {}".format(address)
        #Send connection message to client.
        client.send(msg)
        #Receive packed information from client
        data=client.recv(1024)
        #unpack the data
        allData=struct.unpack("!iiccii", data)
        print "Correct Data: {},{},{},{},{}.{}".format(allData[0],allData[1],allData[2],allData[3],hex(allData[4]),bin(allData[5]))
        client.close()
    #If user hits ctrl c then esccape the loop
    except (KeyboardInterrupt):
        break
#Close the server safely
print "Server Terminating"
s.close()