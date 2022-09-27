#Interface puxando câmera
import tkinter
from PIL import Image
from PIL import ImageTk
import cv2 


class videoStream:
    
    painel = None
    janela = None
    camera = None 

    def __init__(self):
        self.janela = tkinter.Tk()
        self.janela.title('video')
        self.janela.geometry("1000x1000")

        #Inicializa o painel
        self.painel = tkinter.Label(self.janela)
        self.painel.grid(row=0, column=0, columnspan=3)

        self.button01 = tkinter.Button(self.janela, text="Iniciar Camera", padx=40, pady=20, fg="white", bg="darkblue", command=lambda: self.Camera())
        self.button02 = tkinter.Button(self.janela, text="Interromper Camera", padx=40, pady=20, fg="white", bg="darkblue")
        self.button03 = tkinter.Button(self.janela, text="Cinza", padx=40, pady=20, fg="white", bg="darkblue")

        self.button01.grid(row=1, column=0, columnspan=1)
        self.button02.grid(row=1, column=1, columnspan=1)
        self.button03.grid(row=1, column=2, columnspan=1)

        # Inicializa a câmera
        self.camera = cv2.VideoCapture(0)
        self.janela.mainloop()

    def Camera(self):

        ret, frame = self.camera.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)
        self.painel.configure(image=frame)
        self.painel.image=frame
        self.painel.after(1, self.Camera)

    def CameraCinza(self):
        self.camera = cv2.VideoCapture(0)
        ret, frame = self.camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = Image.fromarray(gray)
        gray = ImageTk.PhotoImage(gray)
        self.painel.configure(image=gray)
        self.painel.image = gray
        self.painel.after(1, self.Camera)


if __name__ == '__main__':
    objVideo = videoStream()
    print("teste")
