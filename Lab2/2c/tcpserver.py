"""
Author: ELF
Course: Python
version: Python 2.7
FileName: tcpserver.py
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

#Create a server socket bound to port 1337
s = socket(AF_INET, SOCK_STREAM)
s.bind(("192.168.31.128",1337))
s.listen(5)
serverHostIP=s.getsockname()
serverIP=gethostbyname(serverHostIP[0])
print "Server IP: {}".format(serverIP)
serverHostName=gethostname()
print "Server Hostname: {}".format(serverHostName)
msg="IP: {}\nHostName: {}".format(serverIP,serverHostName)
print "Server Listening for Incoming Connections press Ctrl+C to Exit"
while True:
    #Trys to take in a new connection unless CTRL C is pressed
    try:
        #Accepts new socket and prints the address
        c,a = s.accept()
        print "Connection found from: {}".format(a)
        #Send host information to client
        c.send(msg)
        hostName=c.recv(1024)
        print "Host Name: {}".format(hostName)
        c.close()
    #If user hits ctrl c then esccape the loop
    except (KeyboardInterrupt):
        break
#Close the server safely
print "Server Terminating"
s.close()