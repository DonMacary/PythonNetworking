"""
Author: ELF
Course: Python
version: Python 2.7
FileName: tcpclient.py
Lab2A
Instructions:
    Write a TCP server that receives a string, reverses order of 
    the words, and sends it back to the client.
    Write a TCP client to connect to print the response 
    (build in IPv4).
"""
from socket import *
#Create a new socket for the client and conenct to the server
#On port 1337
s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.31.128",1337))
#Accept user string to send to server
msg = raw_input("Enter a string to send to the server: ")
#send message to server and receive response
s.send(msg)
resp = s.recv(1024)
#Print response and close connection
print "Server Response"
print resp
print "Killing Connection to Server"
s.close()