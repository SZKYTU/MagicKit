from unittest import result
import time
import os
import questionary
from NetworkTools.pcinfomodule import UserInfo
from NetworkTools.staticMode import subprocess_cmd_static, staticCommand
from NetworkTools.dynamicMode import subprocess_cmd_dynamic, dynamicComand
from NetworkTools.socketclient import clientJsonSend
from main import CLIApp


class NetToolsApp:
    def __init__(self):
        self.main_question = questionary.select(
            "Wybierz opcję:",
            choices=[
                "Ustaw IP statyczne",
                "Ustaw IP DHCP",
                "Wyjscie",]
        )

    def run(self):
        choice = self.main_question.ask()

        if choice == "Ustaw IP statyczne":
            os.system('cls')
            subprocess_cmd_static(staticCommand)

        elif choice == "Ustaw IP DHCP":
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
        elif choice == "Wyjscie":
            CLIApp.run()

            choice = second_question.ask()

            if choice == "TAK":
                clientJsonSend(ip, hostname, mac)
                print("Przesłano dane do formularza")
            elif choice == "NIE":
                self.main_question_loop()

    def main_question_loop(self):
        while True:
            self.run()


if __name__ == '__main__':
    app = NetToolsApp()
    app.run()
