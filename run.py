import os
import subprocess
import time
import webbrowser
import sys

VENV_PATH = os.path.join(os.getcwd(), 'venv')

is_windows = os.name == 'nt'

if is_windows:
    activate_path = os.path.join(VENV_PATH, 'Scripts', 'activate.bat')
    command = f'call "{activate_path}" && python manage.py runserver'
    shell = True
else:
    # Caminho para o activate do Linux/macOS
    activate_path = os.path.join(VENV_PATH, 'bin', 'activate')
    command = f'source "{activate_path}" && python manage.py runserver'
    shell = True  

url = 'http://127.0.0.1:8000/'

print("[INFO] Iniciando o servidor Django com venv...")

server = subprocess.Popen(command, shell=shell, executable='/bin/bash' if not is_windows else None)

time.sleep(2)

webbrowser.open(url)

server.wait()
