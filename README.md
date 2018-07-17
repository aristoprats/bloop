## About

About connecting 2 microcontrollers together through computers through a VPN. That's the long term goal anyway.<br>
The short term goal is more about making a chat application?

## TODO

* README.md
	* [ ] update the about section of this file
* f/prats_server_script.py
	* [ ] Look into using encode and decode, easier for encryption
	      - Going to look into how to implement an SSH protocol for a bit more security
	* [x] Make Input and Output independent as receiving a message can interrupt input.
	      - Seems to be sending alright as you mentioned in Issues?
	* [ ] Currently disposes of all data, find a way to store (line 46) -- I don't get it, what
data?
				- As in the messages aren't currently stored outside of the terminal so
					we can't recall messages (one of the later goals) aside from what's the
					most recently received. The MCs won't have access to the terminal to pull
					past messages
	* [x] Check if sendall is more efficient than a for loop (line 57) -- [socket.sendall](https://docs.python.org/3/library/socket.html) doesn't send to all connections, it sends all data to 1 connection
	* [x] Make guests[] and addresses[] interchangeable (line 63) -- Why would you? guests and addresses hold different data from each other.
				- Bad explanation on my part, supposed to be settable as in you can configure
				  a port and host without changing the script. Easily fixed by including a
					input() call in the script, not implementing right now to make running
					the script fast and easy

## Other Notes
