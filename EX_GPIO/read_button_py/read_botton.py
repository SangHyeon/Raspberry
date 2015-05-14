import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN) #set Input pin - 24

count = 0

while True:
	inputValue = GPIO.input(24) #save 24_pin value
	if (inputValue == True):
		count = count+1
		print("Button pressd " + str(count) + " times")
	time.sleep(.01)
