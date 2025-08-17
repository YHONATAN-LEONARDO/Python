import serial
import time

ser = serial.Serial('COM6', 9600, timeout=1)

while True:
    if ser.readline() != 0:
        print(ser.readline())
        time.sleep(0.1)
