import RPi.GPIO as GPIO
import readchar
import time

# pins:
PAN_STEP = 13
PAN_DIR = 15
PAN_M0 = 7
PAN_SWITCH = 11

TILT_STEP = 16
TILT_DIR = 12
TILT_SWITCH = 18

LASER = 19


def setup_pins():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(PAN_STEP, GPIO.OUT)
    GPIO.setup(PAN_DIR, GPIO.OUT)
    GPIO.setup(PAN_M0, GPIO.OUT)
    GPIO.setup(PAN_SWITCH, GPIO.IN)
    GPIO.setup(TILT_STEP, GPIO.OUT)
    GPIO.setup(TILT_DIR, GPIO.OUT)
    GPIO.setup(TILT_SWITCH, GPIO.IN)
    GPIO.setup(LASER, GPIO.OUT)

    GPIO.output(PAN_M0, GPIO.HIGH)
    GPIO.output(LASER, GPIO.LOW)


def left():
    GPIO.output(PAN_DIR, GPIO.HIGH)
    GPIO.output(PAN_STEP, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(PAN_STEP, GPIO.LOW)
    time.sleep(0.001)


def right():
    GPIO.output(PAN_DIR, GPIO.LOW)
    GPIO.output(PAN_STEP, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(PAN_STEP, GPIO.LOW)
    time.sleep(0.001)


def up():
    GPIO.output(TILT_DIR, GPIO.LOW)
    GPIO.output(TILT_STEP, GPIO.HIGH)
    GPIO.output(TILT_STEP, GPIO.LOW)


def down():
    GPIO.output(TILT_DIR, GPIO.HIGH)
    GPIO.output(TILT_STEP, GPIO.HIGH)
    GPIO.output(TILT_STEP, GPIO.LOW)


def laser_on():
    GPIO.output(LASER, GPIO.HIGH)


def laser_off():
    GPIO.output(LASER, GPIO.LOW)


def pan_limit_reached() -> bool:
    return GPIO.input(PAN_SWITCH)


def tilt_limit_reached() -> bool:
    return GPIO.input(TILT_SWITCH)


def basing():
    while not tilt_limit_reached():
        time.sleep(0.001)
        down()

    # for _ in range(1400):
    #     time.sleep(0.001)
    #     up()

    # for _ in range(1400):
    #     time.sleep(0.001)
    #     up()

    # while not pan_limit_reached():
    #     time.sleep(0.001)
    #     right()

    # for _ in range(600):
    #     time.sleep(0.001)
    #     left()



def main():
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
    try:
        while True:
            c = readchar.readchar()
            steer(c)
    except KeyboardInterrupt:
        print("exit")


if __name__ == "__main__":
    setup_pins()
    basing()
    main()
