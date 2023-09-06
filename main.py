import os
import time
import questionary

from NetworkTools import NetToolsApp
from AppInstall import AppInstall
from DomainMenager import DomainManagerApp
from OfficeTools import OfficeToolsApp


class CLIApp:
    def __init__(self):
        self.main_question = questionary.select(
            "Wybierz opcję:",
            choices=[
                "NetTools",
                "Konfiguracja stanowiska",
                "Raporty",
                "OfficeTools",
                "Zakończ"
            ]
        )

    def run(self):
        while True:
            choice = self.main_question.ask()

            if choice == "NetTools":
                if self.net_tools() == "back":  # allows you to return to the main questionnaire
                    continue
            elif choice == "Konfiguracja stanowiska":
                if self.configure_workstation() == "back":
                    continue
            elif choice == "Raporty":
                if self.reports() == "back":
                    continue
            elif choice == "OfficeTools":
                if self.office_tools() == "back":
                    continue
            elif choice == "Zakończ":
                break

    def configure_workstation(self):
        configure_question = questionary.select(
            "Wybierz opcję konfiguracji:",
            choices=[
                "Instalacja pakietów",
                "Działania na domenie",
                "Wyjście"
            ]
        )
        configure_choice = configure_question.ask()

        if configure_choice == "Instalacja pakietów":
            self.install_packages()
        elif configure_choice == "Działania na domenie":
            self.domain_actions()
        elif configure_choice == "Wyjście":
            return "back"

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
            os.system('cls')
            NetToolsApp().set_dynamic_ip()

    def install_packages(self):
        print("Uruchomiono opcję Instalacja pakietów.")
        os.system('cls')
        return AppInstall().run()

    def domain_actions(self):
        os.system('cls')
        return DomainManagerApp().run()

    def reports(self):
        os.system('cls')
        print("Uruchomiono opcję Raporty.")

    def office_tools(self):
        os.system('cls')
        return OfficeToolsApp().run()


if __name__ == '__main__':
    app = CLIApp()
    app.run()
