import pyautogui as pag
import mss, cv2
import numpy as np

#mabinogi freestyle jam macro

#small icon setting
#width = 30
#height = 28

#icon position
freejam_icon_pos = {'left':978, 'top':86, 'width':30, 'height':28}

#button position
freejam_button = [978,86]

with mss.mss() as sct:
    freejam_img = np.array(sct.grab(freejam_icon_pos))[:,:,:3]

#image loading test
#   cv2.imshow('freejam_img',freejam_img)
#   cv2.waitKey(0)
