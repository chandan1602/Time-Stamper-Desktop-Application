import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def build():
    subprocess.check_call(r"py -m PyInstaller --noconsole --name Stamper --onefile F:\TimeStamperPython\stamper.py")

# install("pyinstaller")
build()