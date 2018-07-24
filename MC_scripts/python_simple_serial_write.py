import serial
import time

PORT = '/dev/ttyACM0' # REVIEW: figure out how to automate finding this dev path
baud_rate = 9600      #data transmission rate, no idea why its called baud for MCUs
    #IMPORTANT: This has to match the read and write rate on the MC chip

ser = serial.Serial(PORT, baud_rate)
print("Connection established to port: " + PORT)

time.sleep(3)
#needed because opening the serial port resets the MCU so it needs time to reinitialize

#msg = input("Enter input: \n")

msg = "Hello, World!"
msg_chopped = []

def msg_chopper(message):
    #REVIEW: doesn't need to be a function rn but may make things cleaner later
    for letter in message:
        msg_chopped.append(letter)

msg_chopped.clear()
msg_chopper(msg)

for value in msg_chopped:
    ser.write(bytes(value,'utf-8'))
    print(value)
    time.sleep(.5)


ser.close()
quit()
