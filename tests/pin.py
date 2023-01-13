import RPi.GPIO as GPIO
import time

# STEP_z = 13
# DIR_z = 15

STEP_z = 16
DIR_z = 12
M0_z = 18

GPIO.setmode(GPIO.BOARD)

GPIO.setup(STEP_z, GPIO.OUT)
GPIO.setup(DIR_z, GPIO.OUT)
GPIO.setup(M0_z, GPIO.OUT)
GPIO.output(M0_z, GPIO.LOW)

while True:
    GPIO.output(DIR_z, GPIO.HIGH)
    print("left")
    for i in range(50):
        time.sleep(0.01)
        GPIO.output(STEP_z, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(STEP_z, GPIO.LOW)

    GPIO.output(DIR_z, GPIO.LOW)
    print("right")
    for i in range(50):
        time.sleep(0.01)
        GPIO.output(STEP_z, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(STEP_z, GPIO.LOW)