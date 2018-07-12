"""
Purpose: recieves inputs from external terminal (same machine), prints inputs
         on host side, then modifies the input and reprints it on guest side
         with modification

Definitions:
host - where this script is being run
guest - terminal where the connection is made from

Exit Mode: press 'z' on script side

terminal prompt: telnet localhost 5555

Requires 2 terminals open
"""

import socket
import sys
from _thread import *

#####Global Variables
host = ''  #left blank to refer to localhost for now
port = 5555     #random port
max_connections = 5
encoding = 'utf-8'    #used for encoding and decoding late
active = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #initializes connection point as (tcp,synchronous)

print("Waiting for Connection")

try:
    s.bind((host,port))
except socket.error as error:
    print(str(error))         #prints out error for troubleshooting

s.listen(max_connections)  #limits max number of queued max_connections

def send_recieve(conn):
    conn.send(str.encode("Enter input \n"))

    while True:
        data = conn.recv(4096)  #something about size of data buffer?
        input = data.decode(encoding)

        #these are seperated for now just to get it working
        guest_output = 'Your input was ' + input
        host_output =  "Guests input was " + input

        if not data:
            break
        print(host_output)
            #prints statement on host side
        conn.sendall(str.encode('\n'))
        conn.sendall(str.encode(guest_output))
            #prints statement on guest side
        conn.sendall(str.encode('\n'))

        if (input.lower() == 'z'):
            #Terminates connection if user inputs 'z' and exits main function loop
            print("Connection ended")
            conn.close()
            active = False
            break

while (active == True):
    conn, addr = s.accept()
        #accepts a connection as it comes in, returns (connection, address)
    print("Connection to ",addr[0]," initialized at ", addr[1])

    start_new_thread(send_recieve,(conn,))
        #requires input of 2 variables with 1 left empty for ......reasons?
