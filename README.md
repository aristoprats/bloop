## About

About connecting 2 microcontrollers together through computers through a VPN. That's the long term goal anyway.<br>
The short term goal is more about making a chat application?

## TODO

17/7

* f/prats_server_script.py
	* [x] Make Input and Output independent as receiving a message can interrupt input.
	* [x] Check if sendall is more efficient than a for loop (line 57) -- [socket.sendall](https://docs.python.org/3/library/socket.html) doesn't send to all connections, it sends all data to 1 connection

18/7

* README.md
    * [ ] still needs updating on the about section
* f/prats_server_script.py
	* [ ] Look into RSA encryption
	* [ ] If you want to keep the contents of a chat the best way for that is to use a databse server
	* [ ] Make a host/port input, you can default this to a certain value if you want testing to go easily

## Other Notes
