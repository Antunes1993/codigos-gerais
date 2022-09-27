#Trabalhando com trackbars

import numpy as np
import cv2

#Callback
def nothing(x):
    pass

#Criando uma janela de controles 
cv2.namedWindow('controls')

#Criando uma trackbar
cv2.createTrackbar('r1','controls',1,100,nothing)
cv2.createTrackbar('r2','controls',1,200,nothing)



capture = cv2.VideoCapture(0)
while (True):
    ret, frame = capture.read()    
    radius1 = int(cv2.getTrackbarPos('r1', 'controls'))
    radius2 = int(cv2.getTrackbarPos('r2', 'controls'))
   
    #Canny Edges
    edges = cv2.Canny(frame,radius1,radius2)      
    cv2.imshow('frame',edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

capture.release()
cv2.destroyAllWindows()

