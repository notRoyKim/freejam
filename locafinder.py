import pyautogui as pag
import time

while True:
    x, y = pag.position()
    position_str = 'X: ' + str(x) + 'Y: ' + str(y)
    
    print(position_str)
    time.sleep(1)
