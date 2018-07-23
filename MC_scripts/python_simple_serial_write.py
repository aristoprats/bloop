import serial
import time

PORT = '/dev/ttyACM0'
baud_rate = 9600

ser = serial.Serial(PORT, baud_rate)
print("Connection established to port: " + PORT)

time.sleep(3)
counter = 0;

#msg = input("Enter input: \n")

msg = "Hello, How are you today?!"
msg_chopped = []

def msg_chopper(message):
    for letter in message:
        msg_chopped.append(letter)

while (counter < 25):
    msg_chopped.clear()
    msg_chopper(msg)
    for value in msg_chopped:
        ser.write(bytes(value,'utf-8'))
        time.sleep(.5)
    counter += 1

ser.close()
