### Blink LED example in Raspberry Pi.

Blink LED example in Raspberry Pi.
This is a small example to demo how to blink led in Raspberry Pi. When pressing the push button, the LED is constantly on. When not pressing the push button, the LED blinks. Following is the Python Code and demo Video.


####blinkLED.py


```python
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
```
[![Everything Is AWESOME](https://img.youtube.com/vi/gCGUx7r9BfI/0.jpg)](https://www.youtube.com/watch?v=gCGUx7r9BfI "Everything Is AWESOME")
