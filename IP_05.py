#Detecção de Face e sorrisos com equaização de histogramas

import os
import cv2
import numpy as np
import time


teste = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
strteste = str(teste)

#Acessa os arquivos com as haar-cascades
os.chdir("C:\\Users\\feoxp7\\Desktop\\PROJETOS_2\\codigos-gerais\\Miscelanias\\ArquivosReferencia")

#Detecta webcam 
capture = cv2.VideoCapture(0)

#Instancia os classificadores em cascata com os haar-cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

while 1:
    ret, img = capture.read()
    #Escala de cinza    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Equaliza o histograma
    hist_equalization_detection = cv2.equalizeHist(gray)
    #Converte para espaço de cores YUV
    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])   
    hist_equalization_result = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
    #Detecta faces e sorrisos com histograma equalizado        
    faces = face_cascade.detectMultiScale(img, 1.1 , 5)  #hist_equalization_detection
    smiles = smile_cascade.detectMultiScale(hist_equalization_detection, 2.1, 18)
    eyes = eye_cascade.detectMultiScale(hist_equalization_detection, 2.1, 5)
    '''
    #Detecção de faces
    for (x,y,w,h) in faces:
        cv2.rectangle(hist_equalization_result,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(hist_equalization_result,'Face detectada',(x-20,y-20), font, 1, (0,255,0), 2, cv2.LINE_AA)
        cv2.putText(img,'Face detectada',(x-20,y-20), font, 1, (0,255,0), 2, cv2.LINE_AA)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    '''
    '''
    #Detecção de sorrisos
    for (x,y,w,h) in smiles:
        cv2.rectangle(hist_equalization_result,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(hist_equalization_result,'Sorriso detectado',(x-20,y-20), font, 1, (0,255,0), 2, cv2.LINE_AA)
        cv2.putText(img,'Sorriso detectado',(x-20,y-20), font, 1, (0,255,0), 2, cv2.LINE_AA)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    '''

    #Detecção de olhos
    for (x,y,w,h) in eyes:
        cv2.rectangle(hist_equalization_result,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.rectangle(img,((x+2),(y+2)),(x+w,y+h),(255,0,0),2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(hist_equalization_result,'Detector de olhos',(x-20,y-20), font, 1, (0,255,0), 2, cv2.LINE_AA)
        #cv2.putText(img,'Detector de olhos',(x-20,y-20), font, 1, (0,255,0), 2, cv2.LINE_AA)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #cv2.putText(img, strteste ,(20,40), font, 1, (0,0,255), 2, cv2.LINE_AA)

    
    #Loop para exibição de imagens
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()

