import json
import socket
import sys

def setupSocket(ip):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverAddress = (ip, 12345)
	print 'starting up on %s port %s' % serverAddress
	sock.bind(serverAddress)

	sock.listen(10)
	return sock

def listen(sock):
	while True:
		print 'waiting for a connection'
		connection, clientAddress = sock.accept()

		try:
			print 'connection from', clientAddress
			msgReceived = connection.recv(256)

		finally:
			connection.close()
			return(clientAddress, msgReceived)

def send(ip, m):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	address = (ip, 12345)
	print 'connecting to %s port %s' % address
	sock.connect(address)

	try:
	    sock.sendall(m)

	    # Look for the response
	    amount_received = 0
	    amount_expected = 0

	    while amount_received < amount_expected:
	        msg = sock.recv(256)
	        amount_received += len(msg)
	        print 'received "%s"' % msg

	finally:
	    print 'closing socket'
	    sock.close()


def alternate(data):
	leader = False
	myId = data["id"]
	turn = 0
	alive = True
	sock = setupSocket(data["ip"])
	while True:
		(sender, message) = listen(sock)
		print sender
		print message

		if("LEADER" in message and not leader):
			notification = 'Leader found, node ' + str(data["id"]) + ' terminating'
			send('104.131.160.21', notification)
			send(data["right"], "LEADER")
			sys.exit(0)

		elif("LEADER" in message and leader):
			sys.exit(0)

		if(alive):
			if(int(message) == int(data["id"])):
				leader = True
				notification = 'I, node ' + str(data["id"]) + 'am the leader'
				send('104.131.160.21', notification)
				send(data["right"], "LEADER")

			else:
				notification = 'msg:"' + message + '" from ' + str(sender)
				send('104.131.160.21', notification)

				send(data["right"], str(myId)) if turn%2 == 0 else send(data["left"], str(myId))
				turn+=1

				if(int(message) < int(myId)):
					alive = False
		else:
			notification = 'msg:"' + message + '" from ' + str(sender)
			send('104.131.160.21', notification)

			if(sender[0] == data["left"]):
				send(data["right"], message)
			elif(sender[0] == data["right"]):
				send(data["left"], message)

json_data = open('node.json')
data = json.load(json_data)
print data["ip"]

alternate(data)