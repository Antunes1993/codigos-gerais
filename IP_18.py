#Image viewer
import os 
import cv2
import glob
from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title("Image Viewer")

dir1 = "C:/Users/feoxp7/Desktop/Códigos/Miscelanias/Imagens/csharp.png"
dir2 = "C:/Users/feoxp7/Desktop/Códigos/Miscelanias/Imagens/python.png"
dir3 = "C:/Users/feoxp7/Desktop/Códigos/Miscelanias/Imagens/Fig2.jpg"
dir4 = "C:/Users/feoxp7/Desktop/Códigos/Miscelanias/Imagens/pout2.jpeg"
dir5 = "C:/Users/feoxp7/Desktop/Códigos/Miscelanias/Imagens/pout.jpg"
dir6 = "C:/Users/feoxp7/Desktop/Códigos/Miscelanias/Imagens/teste1.png"

#Cria o objeto imagem
myImg1 = ImageTk.PhotoImage(Image.open(dir1))
myImg2 = ImageTk.PhotoImage(Image.open(dir2))
myImg3 = ImageTk.PhotoImage(Image.open(dir3))
myImg4 = ImageTk.PhotoImage(Image.open(dir4))
myImg5 = ImageTk.PhotoImage(Image.open(dir5))
myImg6 = ImageTk.PhotoImage(Image.open(dir6))

imageList = [myImg1, myImg2, myImg3, myImg4, myImg5, myImg6]


myLabel = Label(image=myImg1)
myLabel.grid(row=0, column=0, columnspan=3)


def foward(imgNumber):
    global myLabel
    global buttonFoward
    global buttonBack

    myLabel.grid_forget()    
    myLabel = Label(image=imageList[imgNumber - 1])
    buttonFoward = Button(root, text=">>", command=lambda: foward(imgNumber + 1))
    buttonBack = Button(root, text="<<", command=lambda: backwards(imgNumber - 1))
    print (imgNumber)

    if imgNumber == 6:
        buttonFoward = Button(root, text=">>", state=DISABLED)


    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=2, column=0)
    buttonExit.grid(row=2, column=1)
    buttonFoward.grid(row=2, column=2)




def backwards(imgNumber):
    global myLabel
    global buttonFoward
    global buttonBack

    myLabel.grid_forget()    
    myLabel = Label(image=imageList[imgNumber - 1])
    buttonFoward = Button(root, text=">>", command=lambda: foward(imgNumber + 1))
    buttonBack = Button(root, text="<<", command=lambda: backwards(imgNumber - 1))
    print (imgNumber)
    
    if imgNumber == 1:
        buttonBack = Button(root, text="<<", state=DISABLED)
    
    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBack.grid(row=2, column=0)
    buttonFoward.grid(row=2, column=2)
  




buttonBack = Button(root, text="<<", command=lambda: backwards(2))
buttonExit = Button(root, text="EXIT", command=root.quit)
buttonFoward = Button(root, text=">>", command=lambda: foward(2))

buttonBack.grid(row=2, column=0)
buttonExit.grid(row=2, column=1)
buttonFoward.grid(row=2, column=2)

#Inicializa a janela
root.mainloop()



