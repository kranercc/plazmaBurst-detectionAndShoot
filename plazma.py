import pymouse
from keyboard import is_pressed
import cv2
import pyscreenshot
import numpy as np  
from time import sleep
def getTarget():
    p = pymouse.PyMouse().position()
    sizex = 200
    sizey = 200
    areaOfEffect = [p[0]-sizex,p[1]-sizey,p[0]+sizex,p[1]+sizey]
    #areaOfEffect= [1041,231,1822,502] # based on canvas
    im = pyscreenshot.grab(areaOfEffect)
    im = np.array(im)
    im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    return im,areaOfEffect
    
def shoot(im,areaOfEffect):
    for i in range(1,3):
        enemy = cv2.imread("enemy%d.png" % i,0)
        w,h = enemy.shape[::-1]
        res = cv2.matchTemplate(im,enemy,cv2.TM_CCOEFF_NORMED)
        threshhold = 0.6
        loc = np.where(res >= threshhold)
        for pt in zip(*loc[::-1]):
            hitX = areaOfEffect[0] + pt[0]
            hitY = areaOfEffect[1] + pt[1]
            pymouse.PyMouse().click(hitX+5,hitY+5)
            #pymouse.PyMouse().move(hitX,hitY)
            #cv2.rectangle(im,pt,(pt[0]+w,pt[1]+h), (255,255,255),2)
    #cv2.imshow("window",im)
    #cv2.moveWindow("window",0,0)
    #cv2.waitKey(25)
while True:
    shoot(getTarget()[0],getTarget()[1])
    if is_pressed("esc"):
        exit()
