import pyautogui as pag
import mss, cv2
import numpy as np

#mabinogi freestyle jam macro

#====1080p small icon setting====
#width = 30
#height = 28

#====1080p note icon setting====
#width = 15
#height = 15

#====1080p window====
#topbar_height = 32
#window_left_border_position = 8
#window_right_border_position = 1912
#window_bottom_border_position = 1008

#dif_width = 1904
#dif_height = 976

#mean_dif_w = 952
#mean_dif_h = 488

#note will be located at 550/976, so 56% apart from the top. 

#icon position
freejam_icon_pos = {'left':978, 'top':86, 'width':30, 'height':28}

#button position
freejam_button = [978,86]

with mss.mss() as sct:
    freejam_img = np.array(sct.grab(freejam_icon_pos))[:,:,:3]

#image loading test
#   cv2.imshow('freejam_img',freejam_img)
#   cv2.waitKey(0)
