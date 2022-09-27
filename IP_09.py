#Calcular o centro de uma região usando OpenCV
import os
import cv2
import imutils 

os.chdir("./Miscelanias/Imagens")

#Processamento de imagens
img = cv2.imread('peixe.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]


#Detectando contornos
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#Loop sobre os contornos
for c in cnts:
    # Detecta o centro do contorno
    
    M = cv2.moments(c)
    '''
    print (int(M["m10"])) 
    print (int (M["m00"]))
    print (int (M["m01"]))
    print (int (M["m00"]))
    '''
    try:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        # Desenha a borda do contorno e o centro da imagem
        cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
        cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(img, "center", (cX - 20, cY - 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    except:
        print("Ocorreu uma exceção.")


#Exibição de imagem
cv2.imshow("img",img)

#loop para exibição de imagens
while True:
    k = cv2.waitKey(0) & 0xFF     
    if k == 27: break             # ESC key to exit
cv2.destroyAllWindows()