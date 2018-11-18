import time

#Motor on and off for loop with time interval of 1s between them
for x in range(3):
	print('Motor On')
	time.sleep(1)
	print('Motor Off')
	time.sleep(1)
