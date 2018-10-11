"""
Author: ELF
Course: Python
version: Python 2.7
FileName: tcpserver.py
Lab2D
Instructions:
    Write a simple socket program that will ask a user 
    to enter a domain and pull the IP address from a 
    remote website. Then use gethostbyaddr() to pull name information.
"""
from socket import *

domainName=raw_input("Enter a web address: ")
ipaddr=gethostbyname(domainName)
print "Domain Name: {}\nIPAddress: {}".format(domainName,ipaddr)
nameinfo=gethostbyaddr(ipaddr)
print nameinfo