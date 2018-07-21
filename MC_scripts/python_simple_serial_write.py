import serial
import time

PORT = '/dev/tty.usbmodem1411'
baud_rate = 9600

ser = serial.Serial(PORT, baud_rate)

time.sleep(3)


while True:
    ser.write(b'1')
    time.sleep(1)
    ser.write(b'0')
    time.sleep(1)
