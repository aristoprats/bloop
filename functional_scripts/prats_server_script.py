import socket
from threading import *
from _thread import *

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
        \# FIXME: CURRENTLY FUCKS UP IF YOU RECIEVE A MESSAGE WHILE TYPING
    '''
    username = guest.recv(buffer_size).decode("utf8")
    username = username[0:len(username)-2]
    print(username)
        #makes tagging people a lot easier than knownig IPs
    message_welcome = 'Welcome %s, to exit type "[exit]"\n' %username
    guest.send(bytes(message_welcome, "utf8"))
        #\# FIXME: look into using encode and decode, easier for encryption
    msg_connected = "%s has connected" %username
    broadcast(bytes(msg_connected, "utf8"))
    guests[guest] = username

    while True:
        msg_recieved = guest.recv(buffer_size)
        msg_fixed = str.encode((str( msg_recieved.decode("utf-8"))))

        if msg_fixed != b'[exit]\r\n':
            broadcast(msg_fixed, username+": ")
            print(msg_fixed)
        else:
            guest.send(bytes("[exit]", "utf8"))
            guest.close()
                #terminates guest thread to conserve system memory
                #\# FIXME: Currently disposes of all data, find way to store
            del guests[guest]
            del addresses[guest]
            broadcast(bytes("%s has left the chat." %username, "utf8"))
            return

def broadcast(msg, prefix=""):
    print((bytes(prefix, "utf8")+msg))
    '''adding the prefix empty string seems to make it work for some reason?
        WILL not work if that value is just left blank'''
    for connection in guests:
        #\# FIXME: Check if sendall is more efficient than for loop
        connection.send(bytes(prefix, "utf8")+msg)

guests = {}
addresses = {}

#\# FIXME: Make these interchangeable, currently fixed for easy testing

################ Initialize Globals
host = ''
    #defers to localhost
port = 5556
buffer_size = 4096
max_connections = 5
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
    #Initializes a TCP, asynchronous socket

if __name__ == '__main__':
    s.listen(max_connections)

    print("Waiting for connections")
    accept_thread = Thread(target= create_connection)
    accept_thread.start()
    accept_thread.join()

s.close()
