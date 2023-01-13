import RPi.GPIO as GPIO
import time


STEP = 12
DIR = 16
M0 = 18

GPIO.setmode(GPIO.BOARD)

GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(M0, GPIO.OUT)
GPIO.output(M0, GPIO.LOW)

while True:
    print("one")
    GPIO.output(DIR, GPIO.LOW)
    for i in range(500):
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.01)

    print("two")
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(500):
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.01)
