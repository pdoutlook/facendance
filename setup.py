# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 22:27:36 2022

@author: ERA
"""

import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\ERA\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\ERA\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Facendance",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'images','data','database','attendances']}},
    version = "5.0",
    description = "Facendance | Developed By Prince Dwivedi(LNCT-E 0176CS191122)",
    executables = executables
    )