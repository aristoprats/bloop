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

'''(1)
def receive(conn):
    #Recieves an input from the guest side and prints said input to host
    #console

    conn.send(str.encode("Enter input \n"))

    while True:
        recieved = conn.recv(4096)
        input = str(recieved.decode('utf-8'))
        input = input[0 : len(input) - 2]
        input = '---------- ' + input
        conn.sendall(str.encode('\n'))

        if not recieved:
            print("Error: Missing Data")
        print(input)

        if (input.lower()[-1] == 'z'):
            print("Guest terminated Connection")
            conn.close()
            break
'''
'''(2)
def send(conn):
    #exports an input from host side and prints it on guest side
    print("Waiting for input\n")
    output_last = ''
    while True:
        output = str(input(""))
        output = '---------- ' + output
        if (output == output_last):
            pass
        else:

            conn.sendall(str.encode(output))
            conn.sendall(str.encode('\n'))
        output_last = output

        if (output.lower()[-1] == 'z'):
            print("Host terminated Connection")
            conn.close()
            break
'''

def main():
    host = ''
    port = 5551
    max_conns = 5

    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Waiting for Guest to connect")

    try:
        s.bind((host,port))
    except socket.error as sError:
        print(str(sError))
        return

    s.listen(max_conns)
    while True:
        conn, addr = s.accept()
        print("Connection to ",addr[0]," initialized at ",addr[1])
        #(1) start_new_thread(receive,(conn,))
        #(2) start_new_thread(send,(conn,))

if __name__ == '__main__':
    main()
