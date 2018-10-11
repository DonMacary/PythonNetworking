from socket import *

s = socket(AF_INET6, SOCK_STREAM)
s.bind(("",1337))
s.listen(5)
c,a = s.accept()
while True:
    c.send("Go Away!")
    data = c.recv(1024)
    if data == "Close":
        print data
        break
    else:
        print data
c.send("Terminating Session")
c.close()
