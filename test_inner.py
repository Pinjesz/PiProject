import RPi.GPIO as GPIO
import time


STEP = 16
DIR = 12
M0 = 18

GPIO.setmode(GPIO.BOARD)

GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(M0, GPIO.OUT)
GPIO.output(M0, GPIO.LOW)

while True:
    GPIO.output(DIR, GPIO.LOW)
    time.sleep(1)
    GPIO.output(DIR, GPIO.HIGH)
    time.sleep(1)
