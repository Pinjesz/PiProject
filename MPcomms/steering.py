import RPi.GPIO as GPIO
import readchar
import time

# pins:
OUTER_STEP = 13
OUTER_DIR = 15
OUTER_M0 = 7
OUTER_M1 = 11

INNER_STEP = 16
INNER_DIR = 12
INNER_M0 = 18

LASER = 19


def setup_pins():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(OUTER_STEP, GPIO.OUT)
    GPIO.setup(OUTER_DIR, GPIO.OUT)
    GPIO.setup(OUTER_M0, GPIO.OUT)
    GPIO.setup(OUTER_M1, GPIO.OUT)
    GPIO.setup(INNER_STEP, GPIO.OUT)
    GPIO.setup(INNER_DIR, GPIO.OUT)
    GPIO.setup(INNER_M0, GPIO.OUT)
    GPIO.setup(LASER, GPIO.OUT)
    GPIO.output(OUTER_M0, GPIO.LOW)
    GPIO.output(OUTER_M1, GPIO.LOW)
    GPIO.output(INNER_M0, GPIO.LOW)
    GPIO.output(LASER, GPIO.LOW)


def left():
    GPIO.output(OUTER_DIR, GPIO.LOW)
    GPIO.output(OUTER_STEP, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(OUTER_STEP, GPIO.LOW)
    time.sleep(0.01)


def right():
    GPIO.output(OUTER_DIR, GPIO.HIGH)
    GPIO.output(OUTER_STEP, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(OUTER_STEP, GPIO.LOW)
    time.sleep(0.01)


def up():
    GPIO.output(INNER_DIR, GPIO.HIGH)
    GPIO.output(INNER_STEP, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(INNER_STEP, GPIO.LOW)
    time.sleep(0.01)


def down():
    GPIO.output(INNER_DIR, GPIO.LOW)
    GPIO.output(INNER_STEP, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(INNER_STEP, GPIO.LOW)
    time.sleep(0.01)


def laser_on():
    GPIO.output(LASER, GPIO.HIGH)


def laser_off():
    GPIO.output(LASER, GPIO.LOW)


def steer(c: str):
    laser_off()
    if c == 'a':
        left()
    elif c == 'd':
        right()
    elif c == 'w':
        up()
    elif c == 's':
        down()
    elif c == ' ':
        laser_on()
    elif c == 'q':
        print("Finished")
        exit()


def main():
    try:
        while True:
            c = readchar.readchar()
            steer(c)
    except KeyboardInterrupt:
        print("exit")


if __name__ == "__main__":
    setup_pins()
    main()
