import questionary
import os
from DomainMenager.domain_menager import DomainManager


class DomainManagerApp:
    def __init__(self):
        self.main_question = questionary.select(
            "Wybierz opcję:",
            choices=[
                "Dodaj do domey tf1",
                "Zmien nazwe komputera",
                "Wyjscie",
            ]
        )

    def run(self):
        choice = self.main_question.ask()

        if choice == "Dodaj do domey tf1":
            DomainManager().join_domain()
        elif choice == "Zmien nazwe komputera":
            computer_name = input("Podaj nazwe komputera")
            DomainManager(computer_name).rename_computer()
            os.system("shutdown /r /t 0")
        elif choice == "Wyjscie":
            pass  # :FIXME
