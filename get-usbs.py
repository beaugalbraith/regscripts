import sys
from Registry import Registry

class Usbdevice:
    def __init__(self, key): # Registry.Registry.RegistryKey
        self.key = key
        self.name = key.name()
        self.vendor = ""
        self.product = ""
        self.version =""
        self.serial = key.subkeys()[0].name()
        self.get_vendor_product_version()

    def get_vendor_product_version(self):
        self.vendor = self.key.name().split('Disk&Ven_')[1].split('&')[0]
        self.product = self.key.name().split('Prod_')[1].split('&')[0]
        self.version = self.key.name().split('Rev_')[1]

reg = sys.argv[1]
"""
Receives system hive and returns usb device info from usbstor
"""

#ntuser = Registry.Registry("D:\FTK\Users\Beau\NTUSER.DAT")
#mountpoints2 = ntuser.open('Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2')

system_hive = Registry.Registry(reg) #'D:\FTK\system'
#
# CurrentControlSet or ControlSet001
usbstor = system_hive.open('ControlSet001\Enum\USBSTOR')
subkeys = usbstor.subkeys()

usb_devices = [key for key in usbstor.subkeys()]


devices = [Usbdevice(device) for device in usb_devices]
for device in devices:
    print(device.name)
    print("\t" + "Product: " + device.product)
    print("\t" + "Vendor: " + device.vendor)
    print("\t" + "Version: " + device.version)
    print("\t" + "Serial: " + device.serial)
print(reg)
