#!/usr/bin/python
# Filename: client.py

import socket

remoteIP = raw_input("Enter remote IP: ");
if len(remoteIP) == 0:
	remoteIP = socket.gethostbyname(socket.gethostname())

PORT = 8088

print('Connect to IP ' + remoteIP )

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((remoteIP,PORT))
while 1:
	str = raw_input("Enter your command: ");
	if(str != 'quit'):
		s.send(str)
	else:
		break

s.close()
print('end of connect')