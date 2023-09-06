import subprocess
import questionary
from OfficeTools.packed_menager import OfficeTools


class OfficeToolsApp:
    def __init__(self):
        self.main_question = questionary.select(
            "Wybierz wersja office do instalacji:",
            choices=[
                "Office 2013",
                "Office 2016",
                "Office 2019",
                "Office 2021",
                "Wyjście",
            ]
        )

    def run(self):
        choice = self.main_question.ask()

        if choice == "Office 2013":
            OfficeTools().run_office2013()
        elif choice == "Office 2019":
            OfficeTools().run_office2019()
        elif choice == "Office 2019":
            OfficeTools().run_office2019()
        elif choice == "Office 2021":
            OfficeTools().run_office2021()
        elif choice == "Wyjscie":
            return "back"
