class DeviceBT(object):
    def __init__(self, mac, rssi):
        self.mac = mac
        self.rssi = rssi

    def Print(self):
        print(self.mac, " : ", self.rssi)

    def GetRssi(self):
        self.rssi = 0

