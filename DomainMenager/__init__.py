import subprocess
import time


class DomainManager:
    def __init__(self, new_computer_name, domain_name):
        self.new_computer_name = new_computer_name
        self.domain_name = domain_name

    def rename_computer(self):
        rename_command = f'WMIC computersystem where caption="%computername%" rename {self.new_computer_name}'
        subprocess.run(rename_command, shell=True, check=True)

        try:
            subprocess.run(rename_command, shell=True, check=True)
            print("Zmiana nazwy komputera została zakończona pomyślnie.")
        except subprocess.CalledProcessError:
            print("Wystąpił błąd podczas zmiany nazwy komputera.")

    def join_domain(self):
        domain_command = f'@powershell Add-Computer tf1.pl'

        try:
            subprocess.run(domain_command, shell=True, check=True)
            print("Wpinanie do domeny przebiegło pomyślnie.")
        except subprocess.CalledProcessError:
            print("Wystąpił błąd podczas wpinania do domeny.")


# :FIXME
new_computer_name = "autowpiecie"
domain_name = "-"  # :TODO
computer_manager = DomainManager(new_computer_name, domain_name)


computer_manager.join_domain()
time.sleep(2)
computer_manager.rename_computer()
