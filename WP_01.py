import os
import pymem 
import smtplib
import subprocess 

try:
    mem = pymem.Pymem("notepad.exe")
except:
    subprocess.Popen("notepad.exe")
    mem = pymem.Pymem("notepad.exe")


mem.inject_python_interpreter()

code = """
import tkinter as tk
win = tk.Tk()
win.mainloop()
"""


mem.inject_python_shellcode(code)
