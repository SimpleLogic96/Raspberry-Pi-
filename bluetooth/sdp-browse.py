#Display services being advertised on a specific bluetooth device

import sys
import bluetooth


if(len(sys.argv) < 2):
    print('usage: sdp-brose <addr>')
    print('   addr can be a bluetooth address, \'localhost\', or \'all\'')
    sys.exit(2)
    

target = sys.argv[1]
print(target)

if (target == 'all'):
    target = None

services = bluetooth.discover_devices(address = target)

if len(services) > 0:
    print('Found' + str(len(services)) + 'services on' + str(sys.argv[1]))
    print('')
else:
    print('No services found')
    
for svc in services:
    print('Service Name: ' + svc['name'])
    print('Host: ' + svc['host'])
    print('Description: ' + svc['description'])
    print('Provided by: ' + svc['provider'])
    print('Protocol: ' + svc['protocol'])
    print('channel/PSM: ' + svc['port'])
    print('svc classes: ' + svc['service-classes'])
    print('Profiles: ' + svc['profiles'])
    print('Service ID: ' + svc['service id'])
    print('')
    
