from unittest import result
import time
import questionary
from NetworkTools.pcinfomodule import UserInfo
from NetworkTools.staticMode import subprocess_cmd_static, staticCommand
from NetworkTools.dynamicMode import subprocess_cmd_dynamic, dynamicComand


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
            subprocess_cmd_static(staticCommand)
        elif choice == "Ustaw IP DHCP":
            subprocess_cmd_dynamic(dynamicComand)
            print(f"Przydzielone IP -> {UserInfo.getIP()} \n"
                  f"Przydzielony MAC -> {UserInfo.getMAC()} \n"
                  f"Nazwa Komputera -> {UserInfo.getHostname()} \n \n")


if __name__ == '__main__':
    app = NetToolsApp()
    app.run()
