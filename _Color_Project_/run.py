import subprocess
import threading

def run_web_thread():
    subprocess.call(
        ['python3', '/home/pc/SOFT/Color_Project/_Color_Project_/manage.py', 'runserver'])

def run_load_thread():
    subprocess.call(
        ['python3', '/home/pc/SOFT/Color_Project/_Color_Project_/LoadURL.py'])
    

run_thread = threading.Thread(target=run_web_thread)
run_thread.start()


run_thread = threading.Thread(target=run_load_thread)
run_thread.start()
