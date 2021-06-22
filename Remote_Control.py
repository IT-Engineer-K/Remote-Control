from bs4 import BeautifulSoup
import requests
import pyautogui
import time
load_url = "http://192.168.11.11:5000/"
screen_size = [int(pyautogui.size().width / 1920), int(pyautogui.size().height / 1080)]
while True:
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    info = str(soup).split(" ")
    pyautogui.moveTo(int(info[0]) * screen_size[0], int(info[1]) * screen_size[1], duration=1)
    if info[2] == "2":
        pyautogui.click()
    elif info[2] == "4":
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.click()