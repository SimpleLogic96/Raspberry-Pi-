#Detecting Nearby Bluetooth Devices

import bluetooth

print('Searching for nearby devices...')

nearby_devices = bluetooth.discover_devices(lookup_names = True, duration = 20)

print('We found ' + str(len(nearby_devices)) + ' devices around you.')

for addr, name in nearby_devices:
    print(name + ': '+ addr)


