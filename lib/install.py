from os import getcwd
from os import system
from os.path import isdir
from shutil import copytree
from shutil import rmtree

class Install:
    def __init(self, name="WifiConnect"):
        self.name = name
        self.fname = __file__
        self.path = getcwd()
    def install(self):
        copytree(get.cwd(), "/etc/init.d/wificonnect")
        system("chmod +x /etc/init.d/wificonnect/main.py")
    
    def uninstall(self):
        if isdir("/etc/init.d/wificonnect"):
            rmtree("/etc/init.d/wificonnect")
        else:
            exit("Could not find the WifiConnect executable.")

        