import requests
import subprocess

# Replace the video URL with your desired YouTube video
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Fetch the YouTube video page
response = requests.get(video_url)
html_content = response.text

print(html_content)

# Find the audio stream URL in the HTML content
start_index = html_content.index('"url":"') + 7
end_index = html_content.index('","', start_index)
audio_url = html_content[start_index:end_index].replace('\\u0026', '&')

# Download the audio using ffmpeg
output_file = "audio.mp3"
subprocess.call(['ffmpeg', '-i', audio_url, output_file])
