import time
import psutil
import subprocess

InterfaceName= list(psutil.net_if_stats())[0]

dynamicComand = f'netsh interface ip set address "{InterfaceName}" dhcp | netsh interface ip set dns "{InterfaceName}" dhcp'

def subprocess_cmd_dynamic(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    for line in proc_stdout.decode().split('\n'):
        print (line)
        
 