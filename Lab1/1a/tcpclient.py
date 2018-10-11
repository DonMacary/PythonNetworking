from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.31.128",1337))
for i in xrange(10):
    msg = "{}: ".format(i)
    s.send(msg)
    data = s.recv(1024)
    print data
s.send("Close")
s.recv(1024)
s.close()