import RPi.GPIO as GPIO
import time
from pynput.keyboard import Key, Listener


#pins:
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
    GPIO.setup(INNER_M0, GPIO.OUT)
    GPIO.setup(INNER_M0, GPIO.OUT)
    GPIO.output(OUTER_M0, GPIO.LOW)
    GPIO.output(OUTER_M1, GPIO.LOW)
    GPIO.output(INNER_M0, GPIO.LOW)


def on_press(key):
    info = False
    if key == Key.left:
        GPIO.output(OUTER_DIR, GPIO.LOW)
        GPIO.output(OUTER_STEP, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(OUTER_DIR, GPIO.LOW)
        time.sleep(0.01)
        info = True

    if key == Key.right:
        GPIO.output(OUTER_DIR, GPIO.HIGH)
        GPIO.output(OUTER_STEP, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(OUTER_DIR, GPIO.LOW)
        time.sleep(0.01)
        info = True

    if key == Key.up:
        GPIO.output(INNER_DIR, GPIO.HIGH)
        GPIO.output(INNER_STEP, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(INNER_STEP, GPIO.LOW)
        time.sleep(0.01)
        info = True

    if key == Key.down:
        GPIO.output(INNER_DIR, GPIO.LOW)
        GPIO.output(INNER_STEP, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(INNER_STEP, GPIO.LOW)
        time.sleep(0.01)
        info = True

    if info:
        print(f'{key} pressed')


def on_release(key):
    if key == Key.esc:
        return False

def main():
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
