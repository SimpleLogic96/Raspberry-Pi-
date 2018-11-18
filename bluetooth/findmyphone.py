import bluetooth 

target_name = raw_input('Enter target name: ')
#target_address = raw_input('Enter target addr: ')

nearby_devices = bluetooth.discover_devices(lookup_names=True)

for addr, name in nearby_devices:
	if target_name == name:
		target_address = addr
		return target_address
		break

print('The target address of ' + target_name + ' is ' + str(target_address))