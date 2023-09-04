import os
import win32api
import win32con


class OfficeTools:
    def run_office2013(self):
        file_name = "2013.exe"
        full_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), file_name)

        try:
            win32api.ShellExecute(
                0, "open", full_file_path, None, None, win32con.SW_SHOWNORMAL)
        except FileNotFoundError:
            print(
                f"Plik '{full_file_path}' nie został znaleziony.")

    def run_office2016(self):
        file_name = "2016.exe"
        full_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), file_name)

        try:
            win32api.ShellExecute(
                0, "open", full_file_path, None, None, win32con.SW_SHOWNORMAL)
        except FileNotFoundError:
            print(
                f"Plik '{full_file_path}' nie został znaleziony.")

    def run_office2019(self):
        file_name = "2019.exe"
        full_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), file_name)

        try:
            win32api.ShellExecute(
                0, "open", full_file_path, None, None, win32con.SW_SHOWNORMAL)
        except FileNotFoundError:
            print(
                f"Plik '{full_file_path}' nie został znaleziony.")

    def run_office2021(self):
        file_name = "2021.exe"
        full_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), file_name)

        try:
            win32api.ShellExecute(
                0, "open", full_file_path, None, None, win32con.SW_SHOWNORMAL)
        except FileNotFoundError:
            print(
                f"Plik '{full_file_path}' nie został znaleziony.")
