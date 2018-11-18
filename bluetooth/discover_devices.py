#Detecting Nearby Bluetooth Devices

import bluetooth
import time

def check_nearby_devices():
        nearby_devices = []
        while len(nearby_devices) < 2:
            print('Searching for nearby devices')
            print('Searching for nearby devices.')
            print('Searching for nearby devices..')
            print('Searching for nearby devices...')
            nearby_devices = bluetooth.discover_devices(lookup_names = True)


        print('We found ' + str(len(nearby_devices)) + ' devices around you.')

        for addr, name in nearby_devices:
            print(name + ': '+ addr)
                

check_nearby_devices()




