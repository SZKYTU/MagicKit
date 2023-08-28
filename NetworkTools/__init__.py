from unittest import result
import time
import os
import questionary
from NetworkTools.pcinfomodule import UserInfo
from NetworkTools.staticMode import subprocess_cmd_static, staticCommand
from NetworkTools.dynamicMode import subprocess_cmd_dynamic, dynamicComand
from NetworkTools.socketclient import clientJsonSend


class NetToolsApp():
    def __init__(self):
        self.static_mode = set_static_ip()  # FIXME:
        pass

    def set_static_ip():
        subprocess_cmd_static(staticCommand)

    def set_dynamic_ip():
        subprocess_cmd_dynamic(dynamicComand)

        ip = UserInfo.getIP()
        mac = UserInfo.getMAC()
        hostname = UserInfo.getHostname()

        os.system('cls')
        time.sleep(2)

        print(f"Przydzielone IP -> {ip} \n"
              f"Przydzielony MAC -> {mac} \n"
              f"Nazwa Komputera -> {hostname} \n \n")

        second_question = questionary.select(
            "Sprawdz dane, i zdecyduj czy wysłać je do arkusza",
            choices=[
                "TAK",
                "NIE",]
        )
        choice = second_question.ask()

        if choice == "TAK":
            clientJsonSend(ip, hostname, mac)
            print("Przesłano dane do formularza")
        elif choice == "NIE":
            print('nie')

# if __name__ == '__main__':
#     app = NetToolsApp()
#     app.run()
