import sys
from cx_Freeze import setup, Executable
build_exe_options = {"packages":["os"],"includes":["tkinter"]}
base = None 
if sys.platform == "win32":
    base = "win32GUI"

    setup(name = "Contas a Pagar e Receber",
          version = "1.0", 
          description = "Pagar Receber Caixa",
          options= {"build_exe": build_exe_options},
          executables= [Executable(".\contasapagar\modulos\contaspagar.py",base=base)]
          )