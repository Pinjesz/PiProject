import serial
import time
import numpy as np

ser = serial.Serial(
    port="/dev/serial0",
    baud_rate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)


def read():
    while True:
        counter = ser.in_waiting  # count the number of bytes of the serial port
        if counter > 0:
            bytes_serial = ser.read()
            print(bytes_serial)


if ser.isOpen() == False:
    ser.open()  # open serial port if not open
    print("serial opened")

try:
    read()
except:
    ser.close()
