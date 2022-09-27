#Processamento de imagem básico
import numpy as np
import cv2

capture = cv2.VideoCapture(0)
bgr = cv2.createBackgroundSubtractorKNN()
out = cv2.VideoWriter('output.mp4', -1, 20.0, (640,480))


while(True):
    ret, frame = capture.read()
    #Conversão espaço de cores (escala de cinza e espaço de cores hsv)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Corte espacial
    cornerRegion = frame [200:400, 200:400]
    frame [0:200, 0:200] = cornerRegion 
    #Threshold
    retval, threshold = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #Canny Edges
    edges = cv2.Canny(frame,100,100)
    #Smoothed Filter
    kernel = np.ones((15,15), np.float32)/325
    smoothed = cv2.filter2D(frame,-1,kernel)
    #Bilateral Filter
    bilateral = cv2.bilateralFilter(smoothed,15,75,75)
    #Background Reduction
    bgrMask = bgr.apply(frame)
    #Cartoon 
    color = cv2.bilateralFilter(frame,9,250,250)
    cartoon = cv2.bitwise_and(color,color, mask=edges)

    # write the flipped frame
    out.write(frame) 
    
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',bgrMask)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
out.release()
cv2.destroyAllWindows()


