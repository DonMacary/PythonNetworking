from socket import *

s = socket(AF_INET6, SOCK_STREAM)
s.connect(("fe80::9f4f:704:e78b:cd5a",1337))
for i in xrange(10):
    msg = "{}: ".format(i)
    s.send(msg)
    data = s.recv(1024)
    print data
s.send("Close")
s.recv(1024)
s.close()