## About

About connecting 2 microcontrollers together through computers through a VPN. That's the long term goal anyway.<br>
The short term goal is more about making a chat application?

## TODO

* README.md
	* [ ] update the about section of this file
* f/prats_server_script.py
	* [ ] Look into using encode and decode, easier for encryption
	* [ ] Make Input and Output independent as recieving a message can interrupt input.
	* [ ] Currently disposes of all data, find a way to store (line 46) -- I don't get it, what data?
	* [x] Check if sendall is more efficient than a for loop (line 57) -- [socket.sendall](https://docs.python.org/3/library/socket.html) doesn't send to all connections, it sends all data to 1 connection
	* [x] Make guests[] and addresses[] interchangeable (line 63) -- Why would you? guests and addresses hold different data from each other.

## Other Notes
