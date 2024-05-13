from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from pytube import YouTube
from moviepy.editor import AudioFileClip

# API key
API_KEY = "ApiKey"

# get the string to be searched
search_string = input("Enter the search string: ")

# Youtube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

try:
  # calling the video links from the search result
  search_response = youtube.search().list(
    q=search_string, type='video',
    part='id,snippet', maxResults=50
  ).execute()

  # declaring the empty dictonary to store the link of the video
  video_url = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      video_link = f"https://www.youtube.com/watch?v={search_result['id']['videoId']}"
      video_url.append(video_link)
    else:
      print("there is some error")

  no = 0
  for url in video_url:
    # Create a YouTube object for the video
    yt = YouTube(url)
    no = no+1
    
    # Get the highest quality audio stream
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    
    # Download the audio
    audio_file = audio_stream.download()
    
    # Convert the downloaded audio to an mp3 file using moviepy
    audio = AudioFileClip(audio_file)
    audio.write_audiofile(f"audio{no}.mp3")

except HttpError as err:
  print(f'an error has occurd: {err}')
