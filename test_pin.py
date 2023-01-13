import RPi.GPIO as GPIO
import time


PIN = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIN, GPIO.OUT)

while True:
    print(f"low {PIN}")
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(2)
    print(f"high {PIN}")
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(2)
