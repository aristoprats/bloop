import serial
import time

PORT = '/dev/ttyACM0' # REVIEW: figure out how to automate finding this dev path
baud_rate = 9600     #data transmission rate, no idea why its called baud for MCUs
    #IMPORTANT: This has to match the read and write rate on the MC chip
'''Speed testing of data transmission at different bauds (data_size = 73 bytes) for Arduino
    115200 baud  --> 30s = 2.4333 bytes/second
    250000 baud  --> 29.7s = 2.4579 bytes/second
'''

ser = serial.Serial(PORT, baud_rate)
print("Connection established to port: " + PORT)

time.sleep(2)
#needed because opening the serial port resets the MCU so it needs time to reinitialize

#msg = input("Enter input: \n")

msg = str(input("Transmit Message >> "))
print("Transmission Length >> " + str(len(msg)))
msg_chopped = []

def msg_chopper(message):
    #REVIEW: doesn't need to be a function rn but may make things cleaner later
    for letter in message:
        msg_chopped.append(letter)

def main():
    msg_chopped.clear()
    msg_chopper(msg)

    #ser.write(bytes("Z", 'utf-8'))
    for value in msg_chopped:
        ser.write(bytes(value,'utf-8'))
        print(value)
    #ser.write(bytes("Z", 'utf-8'))




main()
ser.close()
quit()
