import subprocess
import time


class DomainManager:
    def __init__(self, new_computer_name):
        self.new_computer_name = new_computer_name

    def rename_computer(self):
        rename_command = f'wmic computersystem where name="%COMPUTERNAME%" call rename name="{self.new_computer_name}"'
        subprocess.run(rename_command, shell=True, check=True)

        try:
            subprocess.run(rename_command, shell=True, check=True)
            print("Zmiana nazwy komputera została zakończona pomyślnie.")
        except subprocess.CalledProcessError:
            print("Wystąpił błąd podczas zmiany nazwy komputera.")

    def join_domain():
        domain_command = f'@powershell Add-Computer tf1.pl'

        try:
            subprocess.run(domain_command, shell=True, check=True)
            print("Wpinanie do domeny przebiegło pomyślnie.")
        except subprocess.CalledProcessError:
            print("Wystąpił błąd podczas wpinania do domeny.")
