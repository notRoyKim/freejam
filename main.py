import pyautogui as pag
import keyboard as kb
import mss, cv2
import numpy as np
import time

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

def freestyle_jam(com, pos) : 
    count = 0
    
    while count < com :
        with mss.mss() as sct :
            img = np.array(sct.grab(pos))[:,:,:3]
            compute_note_type(img)
      
        pos['left'] = pos['left'] + 46
        count = count + 1



def compute_note_type(img):
    mean = np.mean(img, axis = (0,1))
    
    if mean[0] < 80 and mean[1] < 80 :
        print("a",mean[0],mean [1])
        #pag.keyDown('a')
        #pag.keyUp('a')
    elif mean[0] < 90 and mean[1] < 90 :
        print("d",mean[0],mean [1])
    elif mean[0] < 110 and mean[1] < 110 :
        print("s",mean[0],mean [1])
    else :
        print("w",mean[0],mean [1])

#icon position
freejam_icon_pos = {'left':978, 'top':86, 'width':30, 'height':28}

#button position
freejam_button = [978,86]

#combo position
#com_1_icon_pos = {'left':861, 'top':593, 'width':16, 'height':16}
com_1_icon_pos = {'left':815, 'top':593, 'width':18, 'height':18}
com_2_icon_pos = {'left':837, 'top':593, 'width':18, 'height':18}
com_3_icon_pos = {'left':815, 'top':593, 'width':18, 'height':18}
com_4_icon_pos = {'left':791, 'top':593, 'width':18, 'height':18}
com_5_icon_pos = {'left':746, 'top':593, 'width':18, 'height':18}

#combo note count
com1 = 5
com2 = 6
com3 = 7
com4 = 8
com5 = 10


pag.moveTo(x = 200,y = 200, duration = 0.0)
pag.mouseDown()
pag.mouseUp()

kb.press_and_release('1')
print("jam is now on!")
time.sleep(1)

kb.press_and_release('f1')
print("go!")
time.sleep(15)

freestyle_jam(com1,com_1_icon_pos)
freestyle_jam(com2,com_2_icon_pos)
freestyle_jam(com3,com_3_icon_pos)
freestyle_jam(com4,com_4_icon_pos)
freestyle_jam(com5,com_5_icon_pos)
