from pytube import YouTube
import sys
import os

def download_audio(video_url, output_path):
  try:
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    out_file = audio_stream.download(output_path=output_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(f"Download completed: {new_file}")
  except Exception as e:
    print(f"Error: {str(e)}")

if __name__ == "__main__":
  video_url = sys.argv[1]
  output_path = sys.argv[2]
  download_audio(video_url, output_path)