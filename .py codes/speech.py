import speech_recognition as sr
import nltk 

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say: ')
    audio = r.listen(source)
    text = r.recognize_google(audio)

    word = nltk.word_tokenize(text)

    bad_words = {'Harsh', 'Shivendra', 'Shivansh', 'Arpit', 'Tejas'}
    i = 0
    new_sentence = set()
    while i < len(word):
        if word[i] in bad_words:
            word.replace(word[i], '####')
        new_sentence = new_sentence.add(word)
        i = i+1
        print(new_sentence)

import pyttsx3

# Create a text-to-speech engine
engine = pyttsx3.init()

# Set the properties for the speech
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.8)  # Volume level (0.0 to 1.0)

# Get the text input from the user
text = input("Enter the text to convert to speech: ")

# Convert the text to speech
engine.say(text)
engine.runAndWait()
