#!/usr/bin/python

import argparse
import os

from lib.install import Install
from lib.wireless import Wifi

class Main:
    def __init__(self):
        self.a = self.args()
        self.main()
    @staticmethod
    def add_to_list(filename, ssid, password):
        if not os.path.isfile(filename):
            exit("THe Filename you supplied does not exist.")
        f = open('passwords.txt', 'a')
        f.write(ssid + ':' + password + '\n')
        f.close()
    @staticmethod
    def args():
        p = argparse.ArgumentParser()
        p.add_argument('-s', '--ssid', action='store', help='SSID you want to add to the List.')
        p.add_argument('-p', '--password', action='store', help='Password you want to add to th List.')
        p.add_argument('-f', '--filename', action='store', help='The SSID:Password file you want to use.')
        p.add_argument('-i', '--install', action='store_true', help='Install to Startup.')
        p.add_argument('--uninstall', action='store_true', help='Uninstall from Startup.')
        return p.parse_args()
    
    def main(self):
        if self.a.install:
            i = Install()
            i.install()
        if self.a.uninstall:
            i = Install()
            i.uninstall()
            exit("Uninstall Complete")
        if not self.a.filename:
            self.a.filename = "passwords.txt"
        if self.a.ssid or self.a.password:
            self.add_to_list(self.a.filename, self.a.ssid, self.a.password)
        w = Wifi()
        
if __name__ == '__main__':
    main()