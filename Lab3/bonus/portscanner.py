"""
Author: ELF
Course: Python
version: Python 2.7
FileName: portscanner.py
Bonus Lab 3
Instructions:
    Create a port scanner. Code it in Python, C, or Raw Sockets. 
    Use IPv4 or IPv6, TCP and/or UDP.
    NOTES: This port scanner sends a single SYN packet to a target port via
    RAW SOCKET, It then receives a TCP packet from the host and parses the 
    flags from that packet. The only check I do is if the flag=18 then
    it must be a SYNACK, meanign the port is open and if the flag is 20
    then it is an RST ACK which means the port is closed. I realize this is 
    probably not error proof, as if any other flags were set then This wouldnt
    work, however based off my limited knowledge of flags I have no reason to 
    believe any flag would be set at this point.
""" 
from socket import *
import struct
import sys


# checksum functions needed for calculation checksum
def checksum(msg):
    s = 0
     
    # loop taking 2 characters at a time
    for i in range(0, len(msg), 2):
        w = ord(msg[i]) + (ord(msg[i+1]) << 8 )
        s = s + w
     
    s = (s>>16) + (s & 0xffff)
    s = s + (s >> 16)
     
    #complement and mask to 4 byte short
    s = ~s & 0xffff
     
    return s
def scan_port(destip, destport):
    #create a raw socket
    try:
        s = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)
    except error , msg:
        print( 'Socket could not be created. Error Code : ' 
        + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    source_ip = "192.168.31.128"
    dest_ip = destip

    #ip header fields
    ip_ihl=5
    ip_ver=4
    ip_tos=0
    ip_tot_len=0
    ip_id=54321
    ip_frag_off=0
    ip_ttl=255
    ip_proto=IPPROTO_TCP
    ip_check=0
    ip_saddr=inet_aton(source_ip)
    ip_daddr=inet_aton(dest_ip)

    ip_ihl_ver = (ip_ver << 4) + ip_ihl

    ip_header = struct.pack("!BBHHHBBH4s4s", ip_ihl_ver, ip_tos, ip_tot_len,
                            ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, 
                            ip_saddr, ip_daddr)

    # tcp header fields
    tcp_source = 1337   # source port
    tcp_dest = destport   # destination port
    tcp_seq = 454
    tcp_ack_seq = 0
    tcp_doff = 5    #4 bit field, size of tcp header, 5 * 4 = 20 bytes
    #tcp flags
    tcp_fin = 0
    tcp_syn = 1
    tcp_rst = 0
    tcp_psh = 0
    tcp_ack = 0
    tcp_urg = 0
    tcp_window = htons (5840)    #   maximum allowed window size
    tcp_check = 0
    tcp_urg_ptr = 0
    
    tcp_offset_res = (tcp_doff << 4) + 0
    tcp_flags = (tcp_fin + (tcp_syn << 1) + (tcp_rst << 2) + (tcp_psh <<3)
            + (tcp_ack << 4) + (tcp_urg << 5))
    
    # the ! in the pack format string means network order
    tcp_header = struct.pack('!HHLLBBHHH' , tcp_source, tcp_dest, tcp_seq,
                            tcp_ack_seq, tcp_offset_res, tcp_flags, 
                            tcp_window, tcp_check, tcp_urg_ptr)

    data = "Hey dude whats going on?"

    source_address = inet_aton(source_ip)
    dest_address = inet_aton(dest_ip)
    placeholder=0
    protocol=IPPROTO_TCP
    tcp_length= len(tcp_header) + len(data)

    psh = struct.pack("!4s4sBBH", source_address, dest_address, 
                        placeholder, protocol, tcp_length)
    psh = psh + tcp_header + data

    tcp_check=checksum(psh)
    tcp_header=(struct.pack('!HHLLBBH' , tcp_source, tcp_dest, tcp_seq, 
                            tcp_ack_seq, tcp_offset_res, tcp_flags,  
                            tcp_window) + struct.pack('H' , tcp_check) + 
                struct.pack('!H' , tcp_urg_ptr))

    packet = ip_header + tcp_header +data

    s.sendto(packet, (dest_ip, 0))

    sniff = socket(AF_INET, SOCK_RAW, IPPROTO_TCP)

    while True:
        packet = sniff.recvfrom(65565)
        
        #packet string from tuple
        packet = packet[0]
        
        #take first 20 characters for the ip header
        ip_header = packet[0:20]
        
        #now unpack them :)
        iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)
        
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        
        iph_length = ihl * 4

        tcp_header = packet[iph_length:iph_length+20]
        
        #now unpack them :)
        tcph = struct.unpack('!HHLLBBHHH' , tcp_header)
        
        tcph_flags=tcph[5]
        if tcph_flags == 18:
            print "Remote Port {} is Open!".format(destport)
        elif tcph_flags == 20:
            print "Remote Port {} is Closed!".format(destport)
        
        sniff.close()
        break
    s.close()

destIp = raw_input("Enter the target IP: ")
if destIp == "":
    print "You must enter a valid Ip address!"
    sys.exit()
destPort = raw_input("Enter the port range 'port-port' you would like to scan: ")
if destPort == '':
    print('You must specify a port range!')
    sys.exit(0)
port_range=destPort.split("-")
if len(port_range) <2:
    scan_port(destIp, int(destPort))
else:
    for port in range(int(port_range[0]), int(port_range[1])+1):
        scan_port(destIp, int(port))