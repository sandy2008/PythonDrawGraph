import numpy as np
import cv2

drawing = False #鼠标按下为真
mode = True #如果为真，画矩形，按m切换为曲线
ix,iy=-1,-1

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode



    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img,(x,y),30,(0,0,255),-1)


img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m') :
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()
