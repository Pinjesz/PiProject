import RPi.GPIO as GPIO
import time
import readchar

# pins:
OUTER_STEP = 13
OUTER_DIR = 15
OUTER_M0 = 7
OUTER_M1 = 11

INNER_STEP = 16
INNER_DIR = 12
INNER_M0 = 18


def setup_pins():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(OUTER_STEP, GPIO.OUT)
    GPIO.setup(OUTER_DIR, GPIO.OUT)
    GPIO.setup(OUTER_M0, GPIO.OUT)
    GPIO.setup(OUTER_M1, GPIO.OUT)
    GPIO.setup(INNER_STEP, GPIO.OUT)
    GPIO.setup(INNER_DIR, GPIO.OUT)
    GPIO.setup(INNER_M0, GPIO.OUT)
    GPIO.output(OUTER_M0, GPIO.LOW)
    GPIO.output(OUTER_M1, GPIO.LOW)
    GPIO.output(INNER_M0, GPIO.LOW)


def left():
    GPIO.output(OUTER_DIR, GPIO.LOW)
    GPIO.output(OUTER_STEP, GPIO.HIGH)
    # time.sleep(0.0001)
    GPIO.output(OUTER_STEP, GPIO.LOW)
    # time.sleep(0.0001)
    print("left")


def right():
    GPIO.output(OUTER_DIR, GPIO.HIGH)
    GPIO.output(OUTER_STEP, GPIO.HIGH)
    # time.sleep(0.0001)
    GPIO.output(OUTER_STEP, GPIO.LOW)
    # time.sleep(0.0001)
    print("right")


def up():
    GPIO.output(INNER_DIR, GPIO.HIGH)
    GPIO.output(INNER_STEP, GPIO.HIGH)
    # time.sleep(0.0001)
    GPIO.output(INNER_STEP, GPIO.LOW)
    # time.sleep(0.0001)
    print("up")


def down():
    GPIO.output(INNER_DIR, GPIO.LOW)
    GPIO.output(INNER_STEP, GPIO.HIGH)
    # time.sleep(0.0001)
    GPIO.output(INNER_STEP, GPIO.LOW)
    # time.sleep(0.0001)
    print("down")


def steer(c: str):
    if c == 'a':
        left()
    elif c == 'd':
        right()
    elif c == 'w':
        up()
    elif c == 's':
        down()
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
