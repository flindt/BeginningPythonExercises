#!/usr/bin/env python
import platform
"""
Fingerprints the following Operating Systems:
*
*
*
*
*
Mac OS X
Ubuntu
Red Hat/Cent OS
FreeBSD
SunOS
"""
class OpSysType(object):

    def __getattr__(self, attr):
        if attr == "osx":
            return "osx"
        elif attr == "rhel":
            return "redhat"
        elif attr == "ubu":
            return "ubuntu"
        elif attr == "fbsd":
            return "FreeBSD"
        elif attr == "sun":
            return "SunOS"
        elif attr == "unknown_linux":
            return "unknown_linux"
        elif attr == "mint":
            return "mint"
        elif attr == "unknown":
            return "unknown"
        else:
            raise AttributeError
        
    def linuxType(self):
        """Uses various methods to determine Linux Type"""
        if platform.dist()[0] == self.rhel:
            return self.rhel
        elif platform.uname()[1] == self.ubu:
            return self.ubu
        elif platform.uname()[0] == self.mint:
            return self.mint
        else:
            return self.unknown_linux
        
    def queryOS(self):
        if platform.system() == "Darwin":
            return self.osx
        elif platform.system() == "Linux":
            return self.linuxType()
        elif platform.system() == self.sun:
            return self.sun
        elif platform.system() == self.fbsd:
            return self.fbsd
    
def fingerprint():
    OStype = OpSysType()
    print( OStype.queryOS() )
    
if __name__ == "__main__":
    fingerprint()
