#!/usr/bin/python
# Filename: car.py

from wheel import *

class Car:
	wheels = [Wheel('a'),Wheel('b'),Wheel('c'),Wheel('d')]
	@staticmethod
	def init():
		#GPIO.setmode(GPIO.BOARD)
		print('init')

	@staticmethod
	def forward():
		print('Car forward')
		for wheel in Car.wheels:
			wheel.forward()

	@staticmethod
	def back():
		print('Car back')
		for wheel in Car.wheels:
			wheel.back()
	
	@staticmethod
	def stop():
		print('Car stop')
		for wheel in Car.wheels:
			wheel.stop()			

	@staticmethod
	def left():
		Car.wheels[0].forward()
		Car.wheels[1].forward()
		Car.wheels[3].back()
		Car.wheels[2].back()

	@staticmethod
	def right():
		Car.wheels[2].forward()
		Car.wheels[3].forward()
		Car.wheels[0].back()
		Car.wheels[1].back()
