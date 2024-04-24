"""
INTERNET
========

IP - Internet Protocol
----------------------
Every computer connected to the internet has its own unique IP address.

IPv4 address value has 32 bits.
e.g. - 172.217.21.206

Alternative - IPv6 values are stored on 128 bit addresses which reduce the
risk of running out of supply - sadly it is not so widely supported
e.g. - 2a00:1450:4001:818::200e

TCP - Transmission Control Protocol
-----------------------------------
More popular than UDP it is used for visiting internet sites.
- Bilateral communication - for every message sent through a connection,
  a response may be received via the same connection.
- confirmation of message receipt for every message sent through such a
  connection
- receive and order of messages are guaranteed

UDP - User Datagram Protocol
----------------------------
- Messages are sent one-way and the computer instantly forgets about them
- There is no guarantee that the messages will be received in the order in
  which they were sent or at all
- Offers less delay than TCP
- Used in multiplayer games

DNS - Domain Name System
------------------------
When you type an address like google.com or sdacademy.com, you do not know
the IP address.
Your computer will know the address of a DNS server.
The information provided by the server corresponds but is not limited to the IP
address corresponding to the domain.

HTTP - Hypertext transfer protocol
-----------------------------------
After the TCP connection to the domain you want to visit has been realized,
the way will be visiting the website is defined by the HTTP protocol.
This is a protocol that acts on a request-and-response basis.
Your browser sends a request to HTTP server which responds to it

HTTP requests (Methods)
-----------------------
GET - method used for requesting the contents of a website
HEAD
POST

e.g.
Simple request of HTTP website google.com/mail (sent by TCP)
GET/mail HTTP/1.1 => method name, http protocol version
Host:google.com   => host (receiver of the request)
/mail => path to the content we request
The server will send us the response in the form of an HTML document
"""