## About

Ultimate goal: To create a way to communicate between two physical devices (MCU LCDs) in a manner similar to an Instant Messaging app

En media goals:
1 [ ] Create a 2 way chat connection between two different computers
2 [ ] Create a one way method to display incoming messages on the LCDs
3 [ ] Create a two way method that can display incoming and send outgoing messages
4 [ ] ???
5 [ ] Displace Amazon in the global economy



## TODO

17/7

* f/prats_server_script.py
	* [x] Make Input and Output independent as receiving a message can interrupt input.
	* [x] Check if sendall is more efficient than a for loop (line 57) -- [socket.sendall](https://docs.python.org/3/library/socket.html) doesn't send to all connections, it sends all data to 1 connection

18/7

* README.md
    * [ ] still needs updating on the about section
* f/prats_server_script.py
	* [ ] Look into [RSA](https://medium.com/@ismailakkila/black-hat-python-encrypt-and-decrypt-with-rsa-cryptography-bd6df84d65bc) encryption
				- 20/7 This encrypts the actual transmission en route and doesn't seem very hard to implement, I dig the idea
				       - But also do we have any sort of security measures on the connection itself? (as in to deter some rando from just connecting to the port while its open)
	* [ ] If you want to keep the contents of a chat the best way for that is to use a databse server
				- 20/7 Is this essentially what your brick breaker game was doing? Or are you suggesting we actually get a physical server.....actually I do have one here we might be able to use
	* [ ] Make a host/port input, you can default this to a certain value if you want testing to go easily
				- 20/7 Yup, just left it as a hardcoded value to make testing faster for the moment (that was just a note for myself)

20/7
* Added a separate folder for scripts that deal directly with the microcontrollers (MC_scripts)
* NEW M/arduino_LCD_Reciever
	- Receives a byte-encoded message through a USB line and displays it as an Ascii character on an LCD and as a binary stream on an an LED
* NEW M/python_simple_serial_write.py
	- Simple write to USB test script, sends a simple binary signal through USB port to arduino
	- Requires pySerial library to be installed :(, will look for a more native path
	* [x] Currently can't find COM5 port, file path not available
		- Solved but currently requires knowing the write path and only works on pure linux or pure windows OS (not just bash running on windows)

24/7
* f/prats_server_script.py
	- Now writes directly to Arduino LCD
	[ ] - Has problems exiting, currently requires using 'ctrl+z' and then a 'kill -9' command from terminal
	[ ] - Is now a good time to work on a "recall past messages function" ?

* M/arduino_LCD_Reciever.ino
	[ ] - Writing to LCD program is real slow and innefficient rn, works but can be improved
	[ ] - Display format needs to be changed, kind of aids to read atm, most likely going to require a char limit

## Other Notes
