import RPi.GPIO as GPIO
import time


STEP = 13
DIR = 15
M0 = 7
M1 = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(M0, GPIO.OUT)
GPIO.setup(M1, GPIO.OUT)
GPIO.output(M0, GPIO.LOW)
GPIO.output(M1, GPIO.LOW)

while True:
    print("one")
    GPIO.output(M0, GPIO.LOW)
    GPIO.output(DIR, GPIO.LOW)
    for i in range(100):
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.01)

    print("two")
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(100):
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.01)

    print("three")
    GPIO.output(DIR, GPIO.LOW)
    GPIO.output(M0, GPIO.HIGH)
    for i in range(100):
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.01)

    print("four")
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(100):
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.01)
