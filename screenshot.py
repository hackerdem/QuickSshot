from pynput import keyboard
import os
import subprocess,datetime
import pyscreeze,winsound
from playsound import playsound
repository='C:\Screenshot_Repository'
def warning():
    winsound.Beep(440, 500)
    #playsound('\Projects\QuickShot\camsound.mp3')
def numbering():  
    return len([name for name in os.listdir(repository) if os.path.isfile(os.path.join(repository, name))])+1

def screenshot(shot,scrshot_time):
    number_item=numbering()
    shot.save('{}\{}-{}.jpeg'.format(repository,number_item,scrshot_time),'jpeg')
  
def repo():
    
    
    if not os.path.isdir(repository):os.makedirs(repository)
    scrshot_time=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    shot=pyscreeze.screenshot()
    if shot:
        warning()
        screenshot(shot,scrshot_time)
    
    
def on_press(key):
    try:
        shot=None
        if str(key)=="Key.print_screen":
            repo()
    except Exception as e:
        print("error")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    

        
        