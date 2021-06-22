import time
import pyautogui
from flask import Flask
import ctypes
import threading
Click_Time = 0
app = Flask(__name__)
@app.route('/')
def hello():
    position = pyautogui.position()
    return str(position[0])+" "+str(position[1])+" "+str(Click_Time)

def click():
    clicked = False
    _clicked = False
    global Click_Time
    Click_Time = 0
    start = time.time()
    end = start
    while end - start < 1:
        end = time.time()
        _clicked = clicked
        if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
            clicked = True
        else:
            clicked = False
        if clicked != _clicked:
            Click_Time += 1
        time.sleep(0.02)
        print(Click_Time)
    Interval()

def Interval():
    target = threading.Thread(target=click)
    target.start()
if __name__ == "__main__":
    Interval()
    app.run(host='0.0.0.0')