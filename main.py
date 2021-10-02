from ClLocatable import *
from FcnBTScan import *
from fcnTimestamp import fcnTimestamp

# create empty list of devices
dctDevices = {}
scanLoopCtrl = 10

# start scan loop with break by key press
while scanLoopCtrl > 0:
    # call function to wait for 1s steps
    fcnTimestamp()

    # call fcn to scan for devices
    dctDevices = BTScan()
    print(dctDevices)

    scanLoopCtrl -= 1