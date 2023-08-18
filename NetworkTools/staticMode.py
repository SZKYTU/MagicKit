import psutil
import subprocess
from pythonping import ping
from config import IP,DNS,mask,getway



def ipCheck():
    for ip in IP:
        pingComand = ping(ip, count=1,verbose=True)
        string = str(pingComand)
        
        if "out" in string:
            FREEIP = ip
            break
    return FREEIP
    

InterfaceName= list(psutil.net_if_stats())[0]

staticCommand = f'netsh interface ip set dns "{InterfaceName}" static {DNS} | netsh interface ip set address name= "{InterfaceName}" static {ipCheck()} {mask} {getway}'


def subprocess_cmd_static(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    for line in proc_stdout.decode().split('\n'):
        print (line)




