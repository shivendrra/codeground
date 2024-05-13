import PyPDF2

# Open the PDF file in read-binary mode
with open('./Whiplash.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)

    # Get the number of pages in the PDF
    num_pages = len(reader.pages)
    full_page = []

    # Iterate over each page and extract the text
    for page_number in range(num_pages):
        page = reader.pages[page_number]
        text = page.extract_text()
        
        
        # Print the extracted text
        # print(f"Page {page_number+1}:\n{text}\n")

import pyttsx3

# Create a text-to-speech engine
engine = pyttsx3.init()

voices = engine.getProperty('voices') # gets the list with all the voices
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'  # Replace with the desired voice ID

# Print the available voices
# for voice in voices:
#     print("Voice ID:", voice.id)
#     print("Name:", voice.name)
#     print("Languages:", voice.languages)
#     print()

# Set the properties
engine.setProperty('voice', voice_id)
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.8)  # Volume level (0.0 to 1.0)

# Convert the text to speech
engine.say(text)

engine.runAndWait()
