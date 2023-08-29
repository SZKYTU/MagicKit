

import os
import time
import questionary

from NetworkTools import NetToolsApp
from AppInstall import AppInstall


class CLIApp:
    def __init__(self):
        self.main_question = questionary.select(
            "Wybierz opcję:",
            choices=[
                "NetTools",
                "Konfiguracja stanowiska",
                "Raporty",
                "OfficeTools"
            ]
        )

    def run(self):
        choice = self.main_question.ask()

        if choice == "NetTools":
            self.net_tools()
        elif choice == "Konfiguracja stanowiska":
            self.configure_workstation()
        elif choice == "Raporty":
            self.reports()
        elif choice == "OfficeTools":
            self.office_tools()

    def configure_workstation(self):
        configure_question = questionary.select(
            "Wybierz opcję konfiguracji:",
            choices=[
                "Instalacja pakietów",
                "Działania na domenie"
            ]
        )
        configure_choice = configure_question.ask()

        if configure_choice == "Instalacja pakietów":
            self.install_packages()
        elif configure_choice == "Działania na domenie":
            self.domain_actions()

    def net_tools(self):
        nettools_question = questionary.select(
            "Wybierz opcję:",
            choices=[
                "Ustaw IP statyczne",
                "Ustaw IP DHCP",
                "Wyjscie",]
        )
        choise = nettools_question.ask()

        if choise == "Ustaw IP statyczne":
            os.system('cls')
            NetToolsApp.set_static_ip()

        elif choise == "Ustaw IP DHCP":
            NetToolsApp().set_dynamic_ip()

    def install_packages(self):
        print("Uruchomiono opcję Instalacja pakietów.")
        AppInstall().run()

    def domain_actions(self):
        print("Uruchomiono opcję Działania na domenie.")

    def reports(self):
        print("Uruchomiono opcję Raporty.")

    def office_tools(self):
        print("Uruchomiono opcję OfficeTools.")


if __name__ == '__main__':
    app = CLIApp()
    app.run()
