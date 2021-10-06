from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

def BTScan():

    # scan and register in object list "devices"
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(1.0)

    dctDeviceRSSI = {}

    # cycle through 
    for dev in devices:

        # print all device information
        # print ("Device", dev.addr, "(", dev.addrType, ") RSSI", dev.rssi)  #"Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
        # v = 0
        # for (adtype, desc, value) in dev.getScanData():
        #     print (v, "-", desc, "=", value)
        #     v=v+1
        # print ("")

        dctDeviceRSSI[dev.addr] = dev.rssi

    #print(dctDeviceRSSI)

    return(dctDeviceRSSI)