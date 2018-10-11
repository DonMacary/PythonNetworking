from socket import *

s = socket(AF_INET, SOCK_DGRAM)
message = "Hello, my name is Donnie Macary"
s.sendto(message, ("localhost", 1337))
for i in xrange(10):
    message = "{}:".format(i)
    s.sendto(message, ("localhost", 1337))
    data, addr = s.recvfrom(1024)
    print data
message = "Close"
s.sendto(message, ("localhost", 1337))
data, addr = s.recvfrom(1024)
print data
s.close()
print "Connection Terminated"
