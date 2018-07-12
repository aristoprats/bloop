"""
Purpose: recieves inputs from external terminal (same machine), prints inputs
         on host side, then modifies the input and reprints it on guest side
         with modification

Definitions:
host - where this script is being run
guest - terminal where the conn is made from

Exit Mode: press 'z' on script side

terminal prompt: telnet localhost 5555

Requires 2 terminals open
"""

import socket
import sys
from _thread import *


def send_recieve(conn):
    conn.send(str.encode("Enter input \n"))

    while True:
        data = conn.recv(4096)  #something about size of data buffer?
        input = str(data.decode('utf-8'))
        print (data,'----',input)
        #input = input[0:len(input)-2]

        #these are seperated for now just to get it working
        guest_output = '\r Your input was ' + input
        host_output =  "Guests input was " + input

        if not data:
            print("err: missing data")
        #print(host_output)
            #prints statement on host side
        conn.sendall(str.encode(guest_output))
            #prints statement on guest side

        if (input.lower() == 'z'):
            #Terminates conn if user inputs 'z' and exits main function loop
            print("Connection ended")
            conn.close()
            active = False
            return


def main():
    host = ''  #left blank to refer to localhost for now
    port = 5555     #random port
    max_conns = 5
    active = True

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #initializes conn point as (tcp,synchronous)

    print("Waiting for Connection")

    try:
        s.bind((host,port))
    except socket.error as error:
        print(str(error))         #prints out error for troubleshooting
        return

    s.listen(max_conns)  #limits max number of queued max_conns
    while (active == True):
        conn, addr = s.accept()
            #accepts a conn as it comes in, returns (conn, address)
        print("Connection to ",addr[0]," initialized at ", addr[1])

        start_new_thread(send_recieve,(conn,))
            #requires input of 2 variables with 1 left empty for ......reasons?


if __name__ == '__main__':
    main()
