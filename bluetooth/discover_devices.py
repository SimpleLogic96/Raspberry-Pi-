#Detecting Nearby Bluetooth Devices

import bluetooth
import time

def check_nearby_devices():
    nearby_devices = []
    if (len(nearby_devices) < 1):
        for x in range(4):
            nearby_devices = nearby_devices + bluetooth.discover_devices(lookup_names = True, duration = 1)
            print('Searching for nearby devices')
            time.sleep(1)
            nearby_devices = nearby_devices + bluetooth.discover_devices(lookup_names = True, duration = 1)
            print('Searching for nearby devices.')
            time.sleep(1)
            nearby_devices = nearby_devices + bluetooth.discover_devices(lookup_names = True, duration = 1)
            print('Searching for nearby devices..')
            time.sleep(1)
            nearby_devices = nearby_devices + bluetooth.discover_devices(lookup_names = True, duration = 1)
            print('Searching for nearby devices...')
            time.sleep(1)

    else:
        print('We found ' + str(len(nearby_devices)) + ' devices around you.')

        for addr, name in nearby_devices:
            print(name + ': '+ addr)
                

check_nearby_devices()




