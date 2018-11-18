import bluetooth

target_name = 'iPhone'
target_address = None

nearby_devices = bluetooth.discover_devices()

for addr in nearby_devices:
	if target_name == bluetooth.lookup_name( aadr ):
		target_address = addr
		break
if(target_address != None):
	print('Found target bluetooth device with address: ' + str(target_address))
else:
	print("Couldn't find target bluetooth devices nearby")