import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def uninstall(package):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package])

def build():
    subprocess.check_call(r"py -m PyInstaller --noconsole --name Stamper32 --onefile F:\TimeStamperPython\stamper.py")

def build32():
    subprocess.check_call(r"py -3.7-32 -m PyInstaller --noconsole --name Stamper32 --onefile F:\TimeStamperPython\stamper.py")

# uninstall("pyinstaller")
# install("pyinstaller")
build()