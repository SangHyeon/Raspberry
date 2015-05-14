import RPi.GPIO as GPIO
import time

GPIO.semode(GPIO.BCM)
GPIO.setuo(20, GPIO.OUT)

while True: #infinity loop
	GPIO.output(25, GPIO.HIGH) #pin 25 led on
	time.sleep(1)
	GPIO.output(25, GPIO.LOW)#pin 25 led off
	time.sleep(1)
