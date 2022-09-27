#Detecção de borda e contador de objetos
import imutils
import cv2

#img
img2 = cv2.imread('tetris.png')
img = cv2.imread('pout2.jpeg')

#gray
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#edge
edge = cv2.Canny(gray, 130, 150)

#threshold
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

#Detectando borda dos objetos
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = img2.copy()

#Texto com contador de objetos
text = "Econtrados {} objetos!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(0, 0, 159), 2)

#Desenho de borda
for c in cnts:
	cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
	cv2.imshow("Contours", output)

#Exibição de imagem
cv2.imshow("img",thresh)

#loop para exibição de imagens
while True:
    k = cv2.waitKey(0) & 0xFF     
    if k == 27: break             # ESC key to exit
cv2.destroyAllWindows()