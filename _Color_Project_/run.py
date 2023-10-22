import subprocess
import threading

def run_web_thread():
    subprocess.call(
        ['python', 'manage.py', 'runserver'])
    
def run_load_thread():
    subprocess.call(
        ['python', 'LoadURL.py'])
    

run_thread = threading.Thread(target=run_web_thread)
run_thread.start()


run_thread = threading.Thread(target=run_load_thread)
run_thread.start()
