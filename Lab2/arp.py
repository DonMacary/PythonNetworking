# bonus-client.py
# Networking Bonus Lab
# Robert John Graham III
# September 21 2018

'''
    Raw sockets on Linux
'''
import socket
import struct

raw_connect = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
raw_connect.bind(("ens33", socket.htons(0x0800)))

source_mac = "00:0c:29:28:f1:cd"
source_ip = "192.168.31.128"
dest_mac = "\xbb\xbb\xbb\xbb\xbb\xbb"
dest_ip = socket.gethostbyname('www.google.com')

# Ethernet Header
protocol = 0x0806                       # 0x0806 for ARP
eth_hdr = struct.pack("!6s6sH", dest_mac, source_mac, protocol)

# ARP header
htype = 1                               # Hardware_type ethernet
ptype = 0x0800                          # Protocol type TCP
hlen = 6                                # Hardware address Len
plen = 4                                # Protocol addr. len
operation = 1                           # 1=request/2=reply
src_ip = socket.inet_aton(source_ip)
dst_ip = socket.inet_aton(dest_ip)
arp_hdr = struct.pack("!HHBBH6s4s6s4s", htype, ptype, hlen, plen, operation, source_mac, src_ip, dest_mac, dst_ip)

packet = eth_hdr + arp_hdr
raw_connect.send(packet)