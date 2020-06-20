#!C:\Users\sampann\AppData\Local\Programs\Python\Python38-32\Python.exe

import os
import sys

def check_reboot():
      """Returns True if the computer has a pending reboot."""
      return os.path.exists("/run/reboot_required")

def new_fun1():
    """This is new function1"""

def new_fun2():
    """This is new function2"""

def new_fun3():
    """This is new function3"""

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)

main()
