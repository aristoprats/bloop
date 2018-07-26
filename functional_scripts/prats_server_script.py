import socket
from threading import *
from _thread import *
import serial
import time
import sys

################ Initialize Globals
host = ''
    #defers to localhost
try:
    port = int(input("TCP Port >> "))
except:
    print("Port must be an integer, Try again")
    quit()

buffer_size = 4096
max_connections = 5
addr = (host, port)
ardPORT = '/dev/ttyACM0'
baud_rate = 20000

guests = {}
addresses = {}

############## Script Functions
def create_connection():
    '''Creates connection to socket for each guest and indexes them into
       a dictionary for future reference
       Has central (HOST) terminal act as intermediary for independent guests
    '''
    while True:
        guest, guest_address = s.accept()
            #accepts socket connection
        print("%s at %s has connected." %guest_address)
        guest.send(bytes("Enter Username: \n", "utf8"))
        addresses[guest] = guest_address
            #indexes all guests
        Thread(target=guest_side, args=(guest,)).start()
            #starts a new thread for all guests making process asynchronous

def guest_side(guest):
    '''Client side handler for both sending and recieving data
    '''
    username = guest.recv(buffer_size).decode("utf8")
    username = username[0:len(username)-2]
    print(username)
        #makes tagging people a lot easier than knownig IPs
    message_welcome = 'Welcome %s, to exit type "[exit]"\n' %username
    guest.send(bytes(message_welcome, "utf-8"))
        #\# FIXME: look into using encode and decode, easier for encryption
    msg_connected = "%s has connected\n" %username
    broadcast(bytes(msg_connected, "utf8"))
    guests[guest] = username

    while True:
        msg_recieved = guest.recv(buffer_size)
        msg_decoded = str(msg_recieved.decode("utf-8"))
        msg_fixed = str.encode(msg_decoded)

        ser.write(bytes(username[0], "utf-8"))
        ser.write(bytes("-"        , "utf-8"))
        if msg_fixed != b'[exit]\r\n':
            broadcast(msg_fixed, '\n'+username+": ")
            print(msg_fixed)
            for byte in msg_decoded[:-2]:
                #Writes msg to USB Port and displays on LCD
                ser.write(bytes(byte, 'utf-8'))
            ser.write(bytes("|", "utf-8"))
                #Adds a limiter to make seeing the break between msgs easier
                # REVIEW: Clean up LCD display method later to make this better
        else:
            guest.send(bytes("[exit]\n", "utf8"))
            guest.close()
                #terminates guest thread to conserve system memory
                #\# FIXME: Currently disposes of all data, find way to store
            del guests[guest]
            del addresses[guest]
            broadcast(bytes("%s has left the chat.\n" %username, "utf8"))
            return

def broadcast(msg, prefix="\n"):
    print((bytes(prefix, "utf8")+msg))
    ''' adding the prefix empty string seems to make it work for some reason?
        will NOT work if that value is just left blank
    '''
    for connection in guests:
        connection.send(bytes(prefix, "utf8")+msg)

def close_server():
    '''Closes server port from command line without forcibly breaking it (cltr+z)
       Currently disconnects the guests but hangs in the terminal # FIXME:
    '''
    while True:
        server_input = str(input("Host CMD >> "))
        if (server_input.lower() == "k"):
            print("Exit command accepted")
            s.close()
            ser.close()
            sys.exit()
        else:
            print("Command Not recognized")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(addr)
    #Initializes a TCP, asynchronous socket
except:
    print("Socket Binding Error")
    quit()


ser = serial.Serial(ardPORT, baud_rate)
print("Connection established to arduino port: " + ardPORT)
time.sleep(3)
'''This opens a serial port through a USB mount to the MC but it will
    reset the MC for a moment so some delay time is added to deal with it
'''



################ Script main call/executor
if __name__ == '__main__':
    s.listen(max_connections)

    print("Waiting for connections")
    accept_thread = Thread(target= create_connection)
    exit_thread   = Thread(target= close_server)
    accept_thread.start()
    exit_thread.start()
    accept_thread.join()
    exit_thread.join()


#############Script close out
s.close()
ser.close()
quit()
