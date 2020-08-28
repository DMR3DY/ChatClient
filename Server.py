# !/usr/bin/env python3

import threading
import socket

#local for now
host = '127.0.0.1'

port = 44444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(host, port)

server.listen()

clients = []
nicknames = []

def broadcast(message):
	for client in clinets:
		client.send(message)

def handle(client):
	while true: 
		try: 
			message = client.recv(1024)
			broadcast(message)
		eSxcept:
			index = clinets.index(client)
			client.remove(client)
			client.close()
			nickname = nickname[index]
			broadcast(f'{nickname} left the chat'.encode('ascii'))
			nicknames.remove(nickname)
			break

def recieve():
	while true: 
		client, address = server.accept()
		print(f"Connected with {str(address)}")

		client.send("NICK".encode('ascii'))
		nickname = client.recv
		nicknames.append(nickname)
		client.append(client)

		print(f'Nickname of the client is {nickname}')
		broadcast(f'{nickname} joined the chat')
		client.send('Connected to the server'.encode('ascii'))

		thread = threading.Thread(target = handle , args=(client))
		thread.start()

print('Server is active')
recieve()