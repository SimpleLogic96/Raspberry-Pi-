#Detecting Nearby Bluetooth Devices

import bluetooth
import time

search = bluetooth.discover_devices(lookup_names=True, duration=2)
def check_nearby_devices():
        nearby_devices = []
        for x in range(4):
            if (len(nearby_devices) < 1):
                nearby_devices = nearby_devices + bluetooth.discover_devices(lookup_names=True, duration=2)
                print('Searching for nearby devices')
                nearby_devices = nearby_devices + bluetooth.discover_devices(lookup_names=True, duration=2)
                print('Searching for nearby devices.')
                nearby_devices = nearby_devices + bluetooth.discover_devices(lookup_names=True, duration=2)
                print('Searching for nearby devices..')
                nearby_devices = nearby_devices + bluetooth.discover_devices(lookup_names=True, duration=2)
                print('Searching for nearby devices...')

            else:
                print('We found ' + str(len(nearby_devices)) + ' devices around you.')

        for addr, name in nearby_devices:
            print(name + ': '+ addr)
                

check_nearby_devices()




