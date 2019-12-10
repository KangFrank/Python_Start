"""
import cv2
import numpy as np
img=cv2.imread("c:\lsy.jpg")
cv2.imshow("lsy",img)
cv2.waitKey(1000)
""""""
import numpy as np
import cv2

img=cv2.imread("c:\lsy.jpg",1000)
cv2.imshow("image",img)


k=cv2.waitKey(0)&0xFF
if k==27:
    cv2.destroyAllWindows() #wait for ESC to kill all and exit
elif k==ord('s'):
    cv2.imwrite('1.png',img) #wait for s key to save and exit
    cv2.destroyAllWindows()

img=cv2.imread("1.png",1000)
cv2.imshow("image",img)
"""
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
	#capture frame-by-frame
    ret , frame = cap.read()
    
    #our operation on the frame come here
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    
    #display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) &0xFF ==ord('q'):  #按q键退出
    	break
#when everything done , release the capture
cap.release()
cv2.destroyAllWindows()
