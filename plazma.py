import pyautogui
import cv2
import pyscreenshot
import numpy as np  
from time import sleep
def getTarget():
    p = pyautogui.position()
    sizex = 50
    sizey = 80
    areaOfEffect = [p.x-sizex,p.y-sizey,p.x+sizex,p.y+sizey]
    im = pyscreenshot.grab(areaOfEffect)
    im = np.array(im)
    im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    for i in range(1,3):
        enemy = cv2.imread("enemy%d.png" % i,0)
        w,h = enemy.shape[::-1]

        res = cv2.matchTemplate(im,enemy,cv2.TM_CCOEFF_NORMED)
        threshhold = 0.5
        loc = np.where(res >= threshhold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(im,pt,(pt[0]+w,pt[1]+h), (255,255,255),2)
            pyautogui.click()
    cv2.imshow("window",im)
    cv2.waitKey(25)


while True:
    getTarget()