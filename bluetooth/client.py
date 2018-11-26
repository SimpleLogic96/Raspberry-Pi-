from bluetooth import *

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect(("fb8:27:eb:af:fb:bf", 3))

client_socket.send("Hello World")

print ("Finished")

client_socket.close()