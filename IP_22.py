#Processamento de imagem básico
import numpy as np
import cv2
from datetime import datetime 



class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        
        ret, frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mensagem = "foi 10 "
        ret2, jpeg = cv2.imencode('.jpg', frame)

        return frame,gray, mensagem, jpeg.tobytes()




camera1 = VideoCamera()
while (True):
    frame,gray,mensagem, frame2 = camera1.get_frame()
    cv2.imshow('frame',gray)
    print (camera1.get_frame[0])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera1.video.release()
cv2.destroyAllWindows()










'''
while(True):
    ret, frame = capture.read()
    #Conversão espaço de cores (escala de cinza e espaço de cores hsv)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Corte espacial
    cornerRegion = frame [200:400, 200:400]
    #frame [0:200, 0:200] = cornerRegion 
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
    #out.write(frame) 
    now = datetime.now()
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

    cv2.imshow('frame',frame)
    #cv2.imshow('mask',bgrMask)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
out.release()
cv2.destroyAllWindows()
'''

