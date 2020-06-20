#!C:\Users\sampann\AppData\Local\Programs\Python\Python38-32\Python.exe

import os
import sys

def check_reboot():
      """Returns True if the computer has a pending reboot."""
      return os.path.exists("/run/reboot_required")

def new_fun1():
    """This is new function1"""

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)

main()
