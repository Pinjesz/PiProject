import RPi.GPIO as GPIO
import time

# STEP_z = 13
# DIR_z = 15

STEP_z = 16
DIR_z = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(STEP_z, GPIO.OUT)
GPIO.setup(DIR_z, GPIO.OUT)

while True:
    GPIO.output(DIR_z, GPIO.HIGH)
    for i in range(20):
        time.sleep(0.1)
        GPIO.output(STEP_z, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(STEP_z, GPIO.LOW)

    GPIO.output(DIR_z, GPIO.LOW)
    for i in range(20):
        time.sleep(0.1)
        GPIO.output(STEP_z, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(STEP_z, GPIO.LOW)
