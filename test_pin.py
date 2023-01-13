import RPi.GPIO as GPIO
import time


PIN = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIN, GPIO.OUT)

while True:
    print("low")
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(3)
    print("high")
    GPIO.output(PIN, GPIO.high)
    time.sleep(3)
