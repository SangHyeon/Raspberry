import RPi.GPIO as GPIO
import time

# Define LED pin
LED = 20
GPIO.semode(GPIO.BCM)
GPIO.setuo(LED, GPIO.OUT)

while True: #infinity loop
	# Wrap this in a try / except
	try:
		print("###> LED Status: ON")
		GPIO.output(25, GPIO.HIGH) #pin 25 led on
		time.sleep(1)
		
		print("###> LED Status: OFF")
		GPIO.output(25, GPIO.LOW)#pin 25 led off
		time.sleep(1)
		
	# Handle user exit // Ctrl-C
	except KeyboardInterrupt:
		GPIO.output(25, GPIO.LOW) # Turn off the LED when exiting via the keyboard
		sys.exit()
