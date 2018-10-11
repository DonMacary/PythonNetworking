import socket
# Prompt user for a domain
remote_host = raw_input("Enter Domain: ")
PORT = 80 # Default port for HTTP
# I added some additional modules just to show more examples

# Pull fully qualified domain name
try:
    fqdn = socket.getfqdn("8.8.8.8")
    print "Fully Qualified Domain Name: %s" %fqdn
except socket.error, err_msg:
    print "%s: %s" %("8.8.8.8", err_msg)

# All of the socket information: (family, socktype, proto, canonname, sockaddr)
try:
    sock_info = socket.getaddrinfo(remote_host, PORT)
    print "Socket information: %s" %sock_info
except socket.error, err_msg:
    print "%s: %s" %(remote_host, err_msg)

# IP address
try:
    ip_addr = socket.gethostbyname(remote_host)
    print "IP address: %s" %ip_addr
except socket.error, err_msg:
    print "%s: %s" %(remote_host, err_msg)

# Extended version of host info
try:
    hostname, aliaslist, ipaddrlist = socket.gethostbyname_ex(remote_host)
    print "Host name: ", hostname
    print "Alias list: ", aliaslist
    print "Address List: ", ipaddrlist
except socket.error, err_msg:
    print "%s: %s" %(remote_host, err_msg)

# Older version of gethostbyname(), requires there to be a pointer record for domain
try:
    name, alias, addresslist = socket.gethostbyaddr('4.2.2.2')
    print "Name: ", name
    print "Alias: ", alias
    print "Address List: ", addresslist
except socket.herror:
    print None, None, None