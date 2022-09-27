# AP01 - Captura audio e, caso a palavra capturada seja igual a "Google", abre um navegador com o endereço do google. 
# Autor: Leonardo Antunes dos Santos
import speech_recognition as sr
import webbrowser as wb

'''
Este programa irá:
Converter fala para texto usando reconhecimento de fala.
Usar o para abrir uma URL usando Web Browser.
Buscar uma query usando voz dentro de uma URL.
'''

voiceRecorder = sr.Recognizer()
print ("Escutando...")
with sr.Microphone() as source:
    audio = voiceRecorder.listen(source)
    try:
        query = voiceRecorder.recognize_google(audio, language='pt')
        print(query)
        if (query == "Lopes"):
            wb.open('https://www.Lopes.com.br')

    except Exception as e:
        print ("try again")
