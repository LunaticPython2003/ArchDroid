import os
import sys
from assets import distro_check, kernel_check

class INSTALL:
    def __init__(self, targets):
        if distro_check.get_distro() != 1:
            print("Sorry, the script only works in Arch")
            exit()
        
        if kernel_check.get_kernel() != 1:
            print("Please try with xanmod or zen kernel")
            kernel_check.ensure_kernel()

        for target in targets:
            if hasattr(self, function_name) and callable(getattr(self, function_name)):
                getattr(self, function_name)()

    def libndk():
        print("ARM translation")

    def libhoudini():
        print("ARM translation (non AMD)")
    
    def widevine():
        print("Widevine DRM for Netflix, Prime Video, etc")

def run():
    target = ["libhoudini", "widevine"]
    obj = INSTALL()