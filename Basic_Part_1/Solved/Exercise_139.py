# Write a Python program to valid a IP address.

import socket
addr = '127.0.0.251'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")


# inet_aton(ip_address)
# As per IPv4, an IP Address is a 32-bit number. 
# These IPv4 addresses are represented as four decimal numbers. 
# Each number is separated by a dot and each number ranges from 0 to 255. 
# The function inet_aton() converts an IPv4 address from the dotted-quad string format to 32-bit packed binary format. 
# The binary format returned could be passed to any program that requires IP address as an object of C type struct in_addr.