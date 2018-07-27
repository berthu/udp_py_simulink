import socket
import struct

UDP_IP = "0.0.0.0"
UDP_PORT = 2337

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
msgcount = 0
while True:
    data, addr = sock.recvfrom(512)
    print "len", str(len(data))
    output = struct.unpack('ddd',data)
    msgcount += 1
    print "received message:", output
    print "message count:", str(msgcount)
