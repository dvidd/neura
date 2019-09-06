import bluetooth

# setup server

port = 0
target_addr = '44:44:1B:04:13:7D'
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.bind((target_addr,port))
sock.listen(1)

# setup client


client_sock,address = sock.accept()
print("Accepted connection from ",address)

data = client_sock.recv(1024)
print("received [%s]" % data)

client_sock.close()
sock.close()

