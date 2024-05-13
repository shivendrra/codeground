# from pytube import YouTube
# from moviepy.editor import AudioFileClip
# import os

# # Replace the video URL with your desired YouTube video
# video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# # Create a YouTube object and get the highest quality audio stream
# yt = YouTube(video_url)
# audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

# # Download the audio stream
# audio_file = audio_stream.download()

# # Convert the downloaded audio to an mp3 file using moviepy
# audio = AudioFileClip(audio_file)
# audio.write_audiofile("audio.mp3")

# # Delete the original downloaded file
# os.remove(audio_file)

# import speech_recognition as sr
# from pydub import AudioSegment

# # convert mp3 file to wav                                                       
# # sound = AudioSegment.from_mp3("transcript.mp3")
# # sound.export("transcript.wav", format="wav")

# # use the audio file as the audio source                       
# r = sr.Recognizer()

# with sr.AudioFile(audio_file) as source:
#   audio = r.record(source)  # read the entire audio file                  
#   print(r.recognize_google(audio))

from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
import speech_recognition as sr

# Replace the video URL with your desired YouTube video
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

try:
    # Create a YouTube object and get the stream with audio (highest quality)
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio stream
    audio_file = audio_stream.download(output_path="downloads")

    # Convert the downloaded audio to an mp3 file using moviepy
    audio = AudioFileClip(audio_file)
    audio.write_audiofile("audio.mp3")

    # Delete the original downloaded file
    os.remove(audio_file)

    # Use the audio file as the audio source
    r = sr.Recognizer()

    with sr.AudioFile("audio.mp3") as source:
        audio = r.record(source)  # Read the entire audio file

    # Perform speech-to-text recognition using Google Web API
    try:
        text = r.recognize_google(audio)
        print("Transcription:")
        print(text)
    except sr.UnknownValueError:
        print("Google Web API could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web API; {e}")

    # Optionally, save the transcription to a text file
    with open("transcription.txt", "w") as text_file:
        text_file.write(text)

except Exception as e:
    print(f"An error occurred: {e}")
