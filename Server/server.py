#!/usr/bin/python
# Filename: server.py

import socket
import sys
import time
from car import *


commands ={'forward':Car.forward,  
  'back':Car.back,   
  'stop':Car.stop,  
  'left':Car.left,  
  'right':Car.right  
}

def execute(command):
	print command
	commands[command]()

localIP = socket.gethostbyname(socket.gethostname())
#HOST = '192.168.1.140'
PORT = 8088

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((localIP,PORT))
s.listen(1)
print('listening on 8088')
while 1:
	conn,addr = s.accept()
	print('Connected by:',addr)
	while 1:
		command = conn.recv(1024).replace('\n','')
		if not command:break
		execute(command)
	conn.close()