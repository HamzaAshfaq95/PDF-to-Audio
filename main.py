import pyttsx3
import os
from PyPDF2 import PdfReader

with open("C:/Users/MuhammadHamzaAshfaq/Desktop/Spain/2958059_A1.pdf", "rb") as pdf_file:
    reader = PdfReader(pdf_file)
    pages = reader.pages[0]
    text = pages.extract_text()

def tts(text, path, gender):
    output_file = os.path.join(path, "output.mp3")
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    if gender == "male":
        engine.setProperty("voice", voices[0].id)
    elif gender == "female":
        engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 145)
    engine.save_to_file(text, output_file)
    engine.runAndWait()

tts(text, "C:/Users/MuhammadHamzaAshfaq/Desktop/New folder", "female")