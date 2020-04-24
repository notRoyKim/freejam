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
#note_diff = 46

#1com : 848 , 5
#2com : 834 , 6
#3com : 802 , 7
#4com : 788 , 8
#5com : 744 , 10

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


def compute_note_type(img):
    mean = np.mean(img, axis = (0,1))
    
    if mean[0] < 75 and mean[1] < 75 :
        print("a")
        #pag.keyDown('d')
        #pag.keyUp('d')
    elif mean[0] < 90 and mean[1] < 90 :
        print("d")
    elif mean[0] < 110 and mean[1] < 110 :
        print("s")
    else :
        print("w")

#icon position
freejam_icon_pos = {'left':978, 'top':86, 'width':30, 'height':28}

#button position
freejam_button = [978,86]

#combo position
#com_1_icon_pos = {'left':861, 'top':593, 'width':16, 'height':16}
com_1_icon_pos = {'left':815, 'top':593, 'width':16, 'height':18}
com_2_icon_pos = {'left':837, 'top':593, 'width':16, 'height':18}
com_3_icon_pos = {'left':815, 'top':593, 'width':16, 'height':18}
com_4_icon_pos = {'left':791, 'top':593, 'width':16, 'height':18}
com_5_icon_pos = {'left':746, 'top':593, 'width':16, 'height':18}

#combo note count
com1 = 5
com2 = 6
com3 = 7
com4 = 8
com5 = 10

"""
with mss.mss() as sct:
    freejam_img = np.array(sct.grab(freejam_icon_pos))[:,:,:3]
    
    com_1_img = np.array(sct.grab(com_1_icon_pos))[:,:,:3]
    com_2_img = np.array(sct.grab(com_2_icon_pos))[:,:,:3]
    com_3_img = np.array(sct.grab(com_3_icon_pos))[:,:,:3]
    com_4_img = np.array(sct.grab(com_4_icon_pos))[:,:,:3]
    com_5_img = np.array(sct.grab(com_5_icon_pos))[:,:,:3]
    
#image loading test
#   cv2.imshow('freejam_img',freejam_img)
    compute_note_type(com_5_img)
    cv2.imshow('com_5_img',com_5_img)
    cv2.waitKey(0)
    
"""

count = 0
while count < com5 :
    with mss.mss() as sct :
        com_1_img = np.array(sct.grab(com_1_icon_pos))[:,:,:3]
        compute_note_type(com_1_img)
        
    com_1_icon_pos['left'] = com_1_icon_pos['left'] + 46
    
    count = count + 1
