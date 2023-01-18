import threading
from enum import Enum

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# Controls - control enumerator:
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---


class Controls(Enum):
    INVALID = -1

    NULL = 0
    RIGHT = 1
    LEFT = 2
    UP = 4
    DOWN = 8

    RIGHT_UP = 5
    RIGHT_DOWN = 9
    LEFT_UP = 6
    LEFT_DOWN = 10

    LASER = 16
    LASER_RIGHT = 17
    LASER_LEFT = 18
    LASER_UP = 20
    LASER_DOWN = 24

    LASER_RIGHT_UP = 21
    LASER_RIGHT_DOWN = 25
    LASER_LEFT_UP = 22
    LASER_LEFT_DOWN = 26
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---


# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# ModeSwitch - mode enumerator switch:
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
controlSwitch = {
    0b00000: Controls.NULL,
    0b00001: Controls.RIGHT,
    0b00010: Controls.LEFT,
    0b00011: Controls.INVALID,
    0b00100: Controls.UP,
    0b00101: Controls.RIGHT_UP,
    0b00110: Controls.LEFT_UP,
    0b00111: Controls.INVALID,
    0b01000: Controls.DOWN,
    0b01001: Controls.RIGHT_DOWN,
    0b01010: Controls.LEFT_DOWN,
    0b01011: Controls.INVALID,
    0b01100: Controls.INVALID,
    0b01101: Controls.INVALID,
    0b01110: Controls.INVALID,
    0b01111: Controls.INVALID,
    0b10000: Controls.LASER,
    0b10001: Controls.LASER_RIGHT,
    0b10010: Controls.LASER_LEFT,
    0b10011: Controls.INVALID,
    0b10100: Controls.LASER_UP,
    0b10101: Controls.LASER_RIGHT_UP,
    0b10110: Controls.LASER_LEFT_UP,
    0b10111: Controls.INVALID,
    0b11000: Controls.LASER_DOWN,
    0b11001: Controls.LASER_RIGHT_DOWN,
    0b11010: Controls.LASER_LEFT_DOWN,
    0b11011: Controls.INVALID,
    0b11100: Controls.INVALID,
    0b11101: Controls.INVALID,
    0b11110: Controls.INVALID,
    0b11111: Controls.INVALID,
}
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# SControl - synchronized control class:
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---


class SControl(object):
    def __init__(self) -> None:
        self._changed = False
        self._control = Controls.NULL
        self._mutex = threading.Lock()

    def isChanged(self) -> bool:
        self._mutex.acquire()
        retval = self._changed
        self._mutex.release()
        return retval

    def pollControl(self) -> Controls:  # clears _changed flag
        self._mutex.acquire()
        retval = self._control
        self._changed = False
        self._mutex.release()
        return retval

    def lookupControl(self) -> Controls:  # leaves _changed flag unchanged
        self._mutex.acquire()
        retval = self._control
        self._mutex.release()
        return retval

    def postControl(self, control: Controls) -> None:  # sets _changed flag
        self._mutex.acquire()
        if self._control != control:
            self._control = control
            self._changed = True
        self._mutex.release()

    def setControl(self, control: Controls) -> None:  # leaves _changed flag unchanged
        self._mutex.acquire()
        self._control = control
        self._mutex.release()
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
