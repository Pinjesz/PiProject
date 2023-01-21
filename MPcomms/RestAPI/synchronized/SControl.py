import threading

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# Control - control container:
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---


class Control:
    control_table = {
        #     0  1  2  3  4  5  6  7  8  9
        0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        0.1: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        0.2: [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        0.3: [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        0.4: [1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        0.5: [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        0.6: [1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        0.7: [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        0.8: [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        0.9: [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }

    def __init__(self, pan: float = 0, tilt: float = 0, laser: bool = False) -> None:
        self.pan: float = Control.to_range(pan)
        self.tilt: float = Control.to_range(tilt)
        self.laser: bool = laser

    def __eq__(self, __o: object) -> bool:
        if type(__o) != Control:
            print("problem")
            return False
        other: Control = __o
        if self.pan != other.pan:
            return False
        if self.tilt != other.tilt:
            return False
        if self.laser != other.laser:
            return False
        return True

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __str__(self) -> str:
        return f'pan {self.pan}, tilt {self.tilt}, laser {"yes" if self.laser else "no"}'

    def to_range(value: float):
        if value >= 1:
            return 1
        if value <= -1:
            return -1
        return round(value, 1)

    def is_control_active(speed: float, i: int) -> bool:
        if Control.control_table[speed][i] == 1:
            return True
        return False

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# SControl - synchronized control class:
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---


class SControl(object):
    def __init__(self) -> None:
        self._changed = False
        self._control = Control()
        self._mutex = threading.Lock()

    def isChanged(self) -> bool:
        self._mutex.acquire()
        retval = self._changed
        self._mutex.release()
        return retval

    def pollControl(self) -> Control:  # clears _changed flag
        self._mutex.acquire()
        retval = self._control
        self._changed = False
        self._mutex.release()
        return retval

    def lookupControl(self) -> Control:  # leaves _changed flag unchanged
        self._mutex.acquire()
        retval = self._control
        self._mutex.release()
        return retval

    def postControl(self, control: Control) -> None:  # sets _changed flag
        self._mutex.acquire()
        if self._control != control:
            self._control = control
            self._changed = True
        self._mutex.release()

    def setControl(self, control: Control) -> None:  # leaves _changed flag unchanged
        self._mutex.acquire()
        self._control = control
        self._mutex.release()
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
