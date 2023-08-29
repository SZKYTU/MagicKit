import subprocess
import questionary
import os
# from menu_menager import CLImenager
# from main import CLIApp


class AppInstall():
    def __init__(self):
        self.main_question = questionary.select(
            "Jakie pakiety chcesz zainstalowac:",
            choices=[
                "Pakiety dla laptopow DELL",
                "Pakiety dla laptopow HP",
                "Pakiety dla komputerów stacjonarnych",
                "Wyjście"  # ::FIXME
            ]
        )

    def run(self):
        choice = self.main_question.ask()

        if choice == "Pakiety dla laptopow DELL":
            self.install_dell_app()
        elif choice == "Pakiety dla laptopow HP":
            self.install_hp_app()
        elif choice == "Pakiety dla komputerów stacjonarnych":
            self.install_pc_app()
        elif choice == "Wyjście":
            pass

    def install_dell_app(self):
        os.system('cls')
        subprocess.run(["Appinstall\install-dell.bat"], shell=True)

    def install_hp_app(self):
        os.system('cls')
        subprocess.run(["Appinstall\install-hp.bat"], shell=True)

    def install_pc_app(self):
        os.system('cls')
        subprocess.run(["Appinstall\install-PC.bat"], shell=True)
