from pynput.keyboard import Key, Listener
import requests
import threading
import sys
import time
import random

directions = {
    'right': 1,
    'left': 2,
    'up': 4,
    'down': 8,
    'laser': 16,
    '_' : 32
}

opposite = {
    'right': 'left',
    'left': 'right',
    'up': 'down',
    'down': 'up',
    'laser' : '_'
}


class Keyboard(object):
    def __init__(self) -> None:
        self._control = {
            'right': 0,
            'left': 0,
            'up': 0,
            'down': 0,
            'laser': 0,
            '_' : 0
        }
        self._changed = False
        self._mutex = threading.Lock()

    def setControl(self, control: str):
        self._mutex.acquire()
        if self._control[control] == 0:
            print(f"set control: {control}")
            self._control[control] = 1
            self._control[opposite[control]] = 0
            self._changed = True
        self._mutex.release()

    def resetControl(self, control: str):
        self._mutex.acquire()
        if self._control[control] == 1:
            print(f"reset control: {control}")
            self._control[control] = 0
            self._changed = True
        self._mutex.release()

    def isChanged(self) -> bool:
        self._mutex.acquire()
        retval = self._changed
        self._mutex.release()
        return retval

    def pollControl(self) -> int:
        self._mutex.acquire()
        retval = 0
        for direction, value in directions.items():
            retval += self._control[direction] * value
        self._changed = False
        self._mutex.release()
        return retval

def connect(address:str) -> int:
    url = f'http://{address}:5000/api/connect'
    try:
        content = {
            'addr': 'localhost',
            'port': '8000',
            'vid': random.randint(0, 100),
            'mgc': 60949
        }
        result = requests.post(url, json=content)
        vid = int(result.json()['vid'])
        print(f"Connected to vehicle number: {vid}")
        return vid
    except Exception as e:
        print("Cannot establish connection", result)
        raise e

def main(address:str, vid: int):
    keyboard = Keyboard()

    def on_press(key):
        if key == Key.left:
            keyboard.setControl('left')
        if key == Key.right:
            keyboard.setControl('right')
        if key == Key.up:
            keyboard.setControl('up')
        if key == Key.down:
            keyboard.setControl('down')
        if key == Key.space:
            keyboard.setControl('laser')

    def on_release(key):
        if key == Key.left:
            keyboard.resetControl('left')
        if key == Key.right:
            keyboard.resetControl('right')
        if key == Key.up:
            keyboard.resetControl('up')
        if key == Key.down:
            keyboard.resetControl('down')
        if key == Key.space:
            keyboard.resetControl('laser')
        if key == Key.esc:
            return False

    try:
        def listen():
            with Listener(
                    on_press=on_press,
                    on_release=on_release) as listener:
                listener.join()

        l = threading.Thread(target=listen)
        l.daemon = True
        l.start()
    except:
        print("Error starting key listener")

    url = f'http://{address}:5000/api/control'
    try:
        while True:
            time.sleep(0.01)
            if keyboard.isChanged():
                control = keyboard.pollControl()

                content = {
                    'vid': vid,
                    'steer': control,
                    'mgc': 43795
                }
                requests.post(url, json=content)
    except KeyboardInterrupt:
        print("Finished")


if __name__ == "__main__":
    address = "192.168.0.108"
    args = sys.argv
    if len(args) == 1:
        vid = connect(address)
    else:
        vid = int(args[1])
    main(address, vid)
