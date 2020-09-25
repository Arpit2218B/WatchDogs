
# Python program to take 
# screenshots 
  
  
import numpy as np 
import cv2 
import pyautogui
import time

counter = 1
 
def screenshot():
    # take screenshot using pyautogui 
    image = pyautogui.screenshot() 
       
    # since the pyautogui takes as a  
    # PIL(pillow) and in RGB we need to  
    # convert it to numpy array and BGR  
    # so we can write it to the disk 
    image = cv2.cvtColor(np.array(image), 
                         cv2.COLOR_RGB2BGR)
   
    # writing it to the disk using opencv
    filepath = "screenshots/image_"+ str(int(time.time())) +".png"
    print(filepath, end=' : ')
    cv2.imwrite(filepath, image)

while(True):
    screenshot()
    print(counter)
    counter = counter + 1
    time.sleep(4)
