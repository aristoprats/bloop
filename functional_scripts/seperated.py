"""
Purpose: recieves inputs from external terminal (same machine), prints inputs
         on host side, then modifies the input and reprints it on guest side
         with modification

Definitions:
host - where this script is being run
guest - terminal where the conn is made from

Exit Mode: press 'z' on script side

terminal prompt: telnet localhost 5551

Requires 2 terminals open
"""

import socket
import sys
from _thread import *
import threading
import time

'''(1)
def receive_host(conn):
    #Recieves an input from the guest side and prints said input to host
    #console

    conn.send(str.encode("Enter input \n"))

    while True:
        recieved = conn.recv(4096) #sets buffer size to 4096 bytes
        input = str(recieved.decode('utf-8'))
        input = input[0 : len(input) - 2]
        input = '---------- ' + input #distinguishes input from output on host side
        conn.sendall(str.encode('\n'))

        if not recieved:
            print("Error: Missing Data")
        print(input)

        if (input.lower()[-1] == 'z'):
            # FIXME: terminates connection when last letter is 'z'
            print("Guest terminated Connection")
            conn.close()
            break
'''
'''(2)
def send_host(conn):
    #exports an input from host side and prints it on guest side
    print("Waiting for input\n")
    output_last = ''
    while True:
        output = str(input(""))
        output = '---------- ' + output
            #helps distinguish input from output on guest terminal
        if (output == output_last):
            #speeds up program and reduces memory use by only acting upon change
            pass
        else:

            conn.sendall(str.encode(output))
            conn.sendall(str.encode('\n'))

        output_last = output        #used to limt send to only on change of state

        if (output.lower()[-1] == 'z'):
            # FIXME: Breaks connection when last letter is 'z'
            print("Host terminated Connection")
            conn.close()
            break
'''

def worker_host():
    tick = 0
    while True:
        print('Tick: ', tick, '\t', threading.currentThread().getName)
        tick += 1
        time.sleep(1)

def worker_guest(conn):
    tick = 0
    while True:
        outbound = 'Tick: ' + str(tick) + '\n'
        conn.sendall(str.encode(outbound))
        tick += 1
        time.sleep(1)



def main():
    host = ''
    port = 5552
    max_conns = 5

    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #establishes connection as TCP and asynchronous

    print("Waiting for Guest to connect")

    try:
        s.bind((host,port))
    except socket.error as sError:
        #returns socket binding error in text form to help debug if needed
        print(str(sError))
        return

    s.listen(max_conns)
    while True:
        conn, addr = s.accept()
        print("Connection to ",addr[0]," initialized at ",addr[1])
        #(1) start_new_thread(receive_host,(conn,))
            #starts thread for host to recieve from guest
        #(2) start_new_thread(send_host,(conn,))
            #starts thread for guest to receive from host
        for i in range(1):
            t= threading.Thread(target = worker_host)
            w = threading.Thread(target = worker_guest, args =(conn,))
            t.daemon = True
            w.daemon = True
            t.start()
            w.start()

if __name__ == '__main__':
    main()
