from socket import *

s = socket(AF_INET6, SOCK_DGRAM)
s.bind(("",1337))
resp = "Go Away"
while True:
    data, addr = s.recvfrom(1024)
    if data == "Close":
        print data
        break
    else:
        print data
        s.sendto(resp,addr)
s.sendto("GoodBye", addr)
s.close()