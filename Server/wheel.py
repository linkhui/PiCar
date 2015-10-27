#!/usr/bin/python
# Filename: wheel.py

class Wheel:
	pins = {'a':[13,15],'b':[16,18],'c':[19,21],'d':[22,24]} 
	def __init__(self,name):
		self.name = name
		self.pin = Wheel.pins[self.name]
		#GPIO.setmode(GPIO.BOARD)
		#GPIO.setup(self.pin[0],GPIO.OUT)
		#GPIO.setup(self.pin[1],GPIO.OUT)
		#self.stop()

	def forward(self):
		print('wheel ' + self.name + ' move forward')
		#print('GPIO.output(self.pin[0],GPIO.HIGH)')
		#print('GPIO.output(self.pin[1],GPIO.LOW)')

	#def stop(self):
		#print('wheel ' + self.name + ' stop')
		#print('GPIO.output(self.pin[0],False)')
		#print('GPIO.output(self.pin[1],False)')

	def back(self):
		print('wheel ' + self.name + ' move back')
		#print('GPIO.output(self.pin[0],False)')
		#print('GPIO.output(self.pin[1],True)')


#wheel = Wheel('a')
#wheel.forward()		