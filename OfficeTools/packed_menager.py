import subprocess
import questionary


class OfficeTools:
    def run_office2013(self):
        try:
            subprocess.run(["OfficeTools\2013.exe"])
        except FileNotFoundError:
            print("Plik nie został znaleziony.")

    def run_office2016(self):
        try:
            subprocess.run(["2016.exe"])
        except FileNotFoundError:
            print("Plik nie został znaleziony.")

    def run_office2019(self):
        try:
            subprocess.run(["2019.exe"])
        except FileNotFoundError:
            print("Plik nie został znaleziony.")

    def run_office2021(self):
        try:
            subprocess.run(["2021.exe"])
        except FileNotFoundError:
            print("Plik nie został znaleziony.")
