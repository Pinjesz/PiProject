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
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# ModeSwitch - mode enumerator switch:
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
controlSwitch = {
    0b0000: Controls.NULL,
    0b0001: Controls.RIGHT,
    0b0010: Controls.LEFT,
    0b0011: Controls.INVALID,
    0b0100: Controls.UP,
    0b0101: Controls.RIGHT_UP,
    0b0110: Controls.LEFT_UP,
    0b0111: Controls.INVALID,
    0b1000: Controls.DOWN,
    0b1001: Controls.RIGHT_DOWN,
    0b1010: Controls.LEFT_DOWN
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

    def pollControl(self) -> Controls: # clears _changed flag
        self._mutex.acquire()
        retval = self._control
        self._changed = False
        self._mutex.release()
        return retval

    def lookupControl(self) -> Controls: # leaves _changed flag unchanged
        self._mutex.acquire()
        retval = self._control
        self._mutex.release()
        return retval

    def postControl(self, control: Controls) -> None: # sets _changed flag
        self._mutex.acquire()
        if self._control != control:
            self._control = control
            self._changed = True
        self._mutex.release()

    def setControl(self, control: Controls) -> None: # leaves _changed flag unchanged
        self._mutex.acquire()
        self._control = control
        self._mutex.release()
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---