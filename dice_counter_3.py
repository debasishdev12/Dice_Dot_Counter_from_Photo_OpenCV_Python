import cv2
import numpy as np
import pyttsx

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',70)

image = cv2.imread("dice7.jpg")
image = cv2.GaussianBlur(image,(5,5),0)
lower = np.array([0,0,0])
upper = np.array([80,80,80])
shapeMask = cv2.inRange(image,lower,upper)
kernel = np.ones((5,5),np.uint8)
shapeMask = cv2.morphologyEx(shapeMask,cv2.MORPH_CLOSE,kernel)

(cnts, _) = cv2.findContours(shapeMask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print "I found %d black shapes" %(len(cnts))

for c in cnts:
    cv2.drawContours(image,[c],-1,(0,255,0),2)
    cv2.imshow("Output",image)
command = "I found %d black dots" %(len(cnts))
engine.say(command)
engine.runAndWait()
cv2.waitKey(5)
cv2.destroyAllWindows()
