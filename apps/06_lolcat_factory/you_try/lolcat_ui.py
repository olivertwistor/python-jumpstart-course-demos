"""
UI functionality for the lolcat app.
"""
import platform
import subprocess


def print_header():
    print("--------------")
    print("LOLCAT FACTORY")
    print("--------------")
    print()


def show_files(folder: str):
    if platform.system() == "Windows":    # Windows
        subprocess.call(["explorer", folder])
    elif platform.system() == "Linux":    # Linux
        subprocess.call(["xdg-open", folder])
    elif platform.system() == "Darwin":   # Mac OS X
        subprocess.call(["open", folder])
    else:
        print("Sorry. Your OS is not supported to automatically show the image "
              "folder {}".format(folder))
