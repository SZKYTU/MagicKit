import questionary
from NetworkTools.dynamicMode import subprocess_cmd_dynamic


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
        print("Uruchomiono opcję NetTools.")

    def install_packages(self):
        print("Uruchomiono opcję Instalacja pakietów.")

    def domain_actions(self):
        print("Uruchomiono opcję Działania na domenie.")

    def reports(self):
        print("Uruchomiono opcję Raporty.")

    def office_tools(self):
        print("Uruchomiono opcję OfficeTools.")


if __name__ == '__main__':
    app = CLIApp()
    app.run()
