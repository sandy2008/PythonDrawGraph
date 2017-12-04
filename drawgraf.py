import numpy as np
import cv2


ix,iy=-1,-1

def draw_circle(event,x,y,flags,param):
    global ix,iy



    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img,(x,y),30,(0,0,255),-1)


img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)

cv2.destroyAllWindows()
