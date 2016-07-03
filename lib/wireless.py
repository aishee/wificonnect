import os

from wifi import Cell, Scheme

class Wifi:
    def __init__(self, iface="wlan0", pwlist='passwords.txt'):
        self.ssids = []
        self.passwords = []
        self.iface = iface
        
        self.networks = []
        self.get_ssid_passwords(pwlist)
        self.get_near_networks()
        
    def get_ssid_passwords(self, pwlist):
        if not os.path.isfile(pwlist):
            exit("[-] Password: SSID List not found.")
        for line in open(pwlist, 'r'):
            self.ssids.append(line.split(':')[0])
            self.passwords.append(line.split(':')[1])
    def get_near_networks(self):
        cells = Cell.all(self.iface)
        for cell in cells:
            if cell.ssid in self.ssids:
                if self.find_scheme(cell.ssid):
                    print("Found a network to connect to.")
                    self.activate_scheme(cell.ssid)
                else:
                    print "Connecting to: %s" % cell.ssid
                    self.create_scheme(cell.ssid, self.passwords[self.ssids.index(cell.ssid)])
            else:
                print "Found no Network to connect to."
    def find_scheme(self, ssid):
        scheme = Scheme.find(self.iface, ssid)
        if scheme is None:
            return False
        else:
            return True
                
    def activate_scheme(self, ssid):
        scheme = Scheme.find(self.iface, ssid)
        if scheme is None:
            return False
        else:
            scheme.activate()
    
    def create_scheme(self, ssid, password):
        cell = Cell.all(self.iface)
        scheme = Scheme.for_cell(self.iface, ssid, cell, password)
        scheme.save()
        scheme.activate()
            