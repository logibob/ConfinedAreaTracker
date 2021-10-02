class Locatable(object):
    def __init__(self, name, macAddress, rssi):
        self.name = name
        self.macAddress = macAddress
        self.rssi = rssi

    def Print(self):
        return "Locatable name: %s\nmacAddress: %s\n rssi: %s" (self.name, self.macAddress, self.rssi)

    def GetRssi(self):
        self.rssi = 0