import subprocess
import socket
import wmi

class UserInfo():  # wrap
    def getIP():
        IP = socket.gethostbyname(socket.gethostname())
        return IP

    def getHostname():
        Hostname = socket.gethostname()
        return Hostname

    def getMAC():
        print(subprocess.call(["ipconfig", "/release"], shell=True))
        print(subprocess.call(["ipconfig", "/renew"], shell=True))
        wmiObj = wmi.WMI()
        temp = wmiObj.Win32_NetworkAdapterConfiguration(IPEnabled=True)[0]
        mac = temp.MACAddress
        return mac
        
