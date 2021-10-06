from ClDeviceBT import *
from FcnBTScan import *
from fcnOutputRSSIList import *
from fcnTimestamp import fcnTimestamp
import os

# create empty list of devices
dctDevices = {}
scanLoopCtrl = 10

# scan loop with break by key press
while scanLoopCtrl > 0:

    # call function to wait for 1s steps
    timestamp = fcnTimestamp()

    # call fcn to scan for devices
    dctDevices = BTScan()

    # clear terminal, keep directly before output of next data
    os.system('cls' if os.name == 'nt' else 'clear')
    # output the devices and rssi formated
    print(timestamp)
    fcnOutputRSSIList(dctDevices)

    
    for nDevice in dctDevices:
        # IF macAddress already exists in any device object -> pass
        if 1 = 0:
            # update rssi
        # IF macAddress DOES NOT yes exist
        else:
            # create new object with mac and rssi

    # NEXT: logic to check, which mac addresses/objects timed out...


    scanLoopCtrl -= 1