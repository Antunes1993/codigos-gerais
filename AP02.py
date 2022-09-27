#Converter texto em audio

# #Importação de módulos
import PyPDF2 
import pyttsx3

#Inicialização de objetos
pdfReader = PyPDF2.PdfFileReader(open('file.pdf','rb'))
speaker = pyttsx3.init()

#Seletor de vozes. 
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[2].id)

#Leitor de arquivo pdf
for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extract_text()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

#Salva arquivo de audio mp3.
speaker.save_to_file(text,'audio.mp3')
speaker.runAndWait()