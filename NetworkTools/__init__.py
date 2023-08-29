import time
import os
import questionary
from NetworkTools.pcinfomodule import UserInfo
from NetworkTools.staticMode import subprocess_cmd_static, staticCommand
from NetworkTools.dynamicMode import subprocess_cmd_dynamic, dynamicComand
from NetworkTools.socketclient import clientJsonSend


class NetToolsApp():
    def __init__(self):
        self.ip = UserInfo.getIP()
        self.mac = UserInfo.getMAC()
        self.hostname = UserInfo.getHostname()

    def set_static_ip():
        subprocess_cmd_static(staticCommand)

    def set_dynamic_ip(self):
        subprocess_cmd_dynamic(dynamicComand)

        os.system('cls')
        time.sleep(2)

        print(f"Przydzielone IP -> {self.ip} \n"
              f"Przydzielony MAC -> {self.mac} \n"
              f"Nazwa Komputera -> {self.hostname} \n \n")

        second_question = questionary.select(
            "Sprawdz dane, i zdecyduj czy wysłać je do arkusza",
            choices=[
                "TAK",
                "NIE",]
        )
        choice = second_question.ask()

        if choice == "TAK":
            clientJsonSend(self.ip, self.hostname, self.mac)
            print("Przesłano dane do formularza")
        elif choice == "NIE":
            print('nie')  # :TODO
