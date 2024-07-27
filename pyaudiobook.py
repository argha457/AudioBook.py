import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Open a file dialog to select a PDF file
book = askopenfilename()

# Open the selected PDF file
with open(book, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pages = len(pdf_reader.pages)

    # Initialize text-to-speech engine
    player = pyttsx3.init()

    # Iterate through each page and read text
    for num in range(pages):
        page = pdf_reader.pages[num]
        text = page.extract_text()
        if text:  # Check if there is any text on the page
            player.say(text)
            player.runAndWait()
