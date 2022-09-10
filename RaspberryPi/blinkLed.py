import RPi.GPIO as GPIO
import time

ledPin = 14
buttonPin = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN)

try:
	while 1:
		if GPIO.input(buttonPin):
			GPIO.output(ledPin, GPIO.HIGH)
		else:
			GPIO.output(ledPin, GPIO.HIGH)
			time.sleep(0.25)
			GPIO.output(ledPin, GPIO.LOW)
			time.sleep(0.25)
except KeyboardInterrupt:
	GPIO.cleanup()
