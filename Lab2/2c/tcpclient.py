"""
Author: ELF
Course: Python
version: Python 2.7
FileName: tcpclient.py
Lab2C
Instructions:
    Write a simple socket program that will send back your 
    machine's Host name and IP Address. 
    (Don't forget to use your resources (Pydocs, Man pages). 
    You can also get formatting help from the python interpreter by 
    using help(socket.gethostname) and help(socket.gethostbyname)
    after importing the socket library.)
"""
from socket import *
#Create a new socket for the client and conenct to the server
#On port 1337
s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.31.128",1337))
resp = s.recv(1024)
#Print response and close connection
print "Server Response"
print resp
hostName=gethostname()
print "Send back to Server:"
print hostName
s.send(hostName)
print "Killing Connection to Server"
s.close()