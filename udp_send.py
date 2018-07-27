import socket
import struct

my_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDP_IP = "127.0.0.1"
UDP_PORT = 4337

v1,v2,v3 = 1.0, 2.0, -10000000
while True:
    #my_socket.sendto(bytes(MESSAGE).encode("utf-8"), (UDP_IP, UDP_PORT))
    my_socket.sendto(struct.pack('ddd',v1, v2,v3), (UDP_IP, UDP_PORT))
my_socket.close()
