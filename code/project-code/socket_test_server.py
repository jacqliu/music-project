import socket
import sys
import zmq

#from project import *

current_idx = 0
data_store = [None, None, None]

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8001)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Set up ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:5555")

while True:

	# Wait for a connection
	#print >>sys.stderr, 'waiting for a connection'
	connection, client_address = sock.accept()
	#print >>sys.stderr, 'connection', connection



	try:
	    #print >>sys.stderr, 'connection from', client_address

	    # Receive the data in small chunks and retransmit it
	    #while True:
	    data = connection.recv(128)
	    print data
	    socket.send(data)
	    #on_touch(data)

	    #print >>sys.stderr, 'received "%s"' % data.decode()

	    #print >>sys.stderr, 'sending data back to the client'
	    #connection.sendall(data)
	        # else:
	        #     print >>sys.stderr, 'no more data from', client_address
	        #     break
	        
	finally:
	    # Clean up the connection
	    connection.close()