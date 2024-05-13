# # # first part

from googleapiclient.discovery import build
from googleapiclient.errors import Error
import json
import os

os.chdir('D:/Machine Learning/Python')

api_key = 'AIzaSyBhbYzOh_B3snsiBlCEwI4DdUZbKJVHass'

youtube = build('youtube', 'v3', developerKey=api_key)

channel = input('enter the channel id: ')

try: 
	channelRes = youtube.channels().list(
		part='contentDetails',
		id=channel,
		maxResults=50
	).execute()
	
	print(type(channelRes))

except Error as e:
	print(f"there's and error: {e}")

def converToJson(results):
	with open("sample.json", "w") as outfile:
		json.dump(results, outfile, indent=2)  # added indent for better readability
		print('written in the JSON file')

converToJson(channelRes)


# # # # second part

# video = input('enter the video for search: ')

# search_response = youtube.search().list(
#     q=video, type='video',
#     part='id,snippet', maxResults=50
#   ).execute()

# print(type(search_response))

# def converToJson(results):
#   with open("sample1.json", "w") as outfile:
#     json.dump(results, outfile)
#     print('written in the JSON file')

# converToJson(search_response)

# # # # third part

# from googleapiclient.discovery import build

# api_key = 'AIzaSyBhbYzOh_B3snsiBlCEwI4DdUZbKJVHass'

# channelName = input('Enter the channel for search: ')

# youtube = build('youtube', 'v3', developerKey=api_key)

# def channelToVideos(channelSearch):
#   channelResults = youtube.channels().list(
#     part='contentDetails,contentOwnerDetails,snippet',
#     id=channelSearch,
#     maxResults=50
#   ).execute()

#   for items in channelResults['pageInfo']:
#     print(channelResults['pageInfo']['resultsPerPage'])

# channelToVideos(channelName)


# from googleapiclient.discovery import build
# import json

# # Function to fetch video links for a given channel ID
# def get_video_links(api_key, channel_id):
#     # Build the YouTube API client
#     youtube = build('youtube', 'v3', developerKey=api_key)

#     try:
#         # Get the content details of the channel
#         channels_res = youtube.channels().list(
#             part='contentDetails',
#             id=channel_id
#         ).execute()

#         if 'items' in channels_res and channels_res['items']:
#             # Get the playlist ID of the uploaded videos
#             uploads_playlist_id = channels_res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

#             # Get the videos in the uploads playlist
#             playlist_items_res = youtube.playlistItems().list(
#                 part='contentDetails',
#                 playlistId=uploads_playlist_id,
#                 maxResults=50  # Adjust as needed
#             ).execute()

#             # Extract video links
#             video_links = ['https://www.youtube.com/watch?v=' + item['contentDetails']['videoId'] for item in playlist_items_res.get('items', [])]

#             return video_links
#         else:
#             print("No 'items' found in the response or the list is empty.")
#             return []

#     except Exception as e:
#         print(f"Error fetching video links: {e}")
#         return []

# # Replace 'YOUR_API_KEY' with your actual API key
# API_KEY = 'AIzaSyBhbYzOh_B3snsiBlCEwI4DdUZbKJVHass'
# channel_id = input('Enter the channel ID: ')

# # Get video links and print them
# video_links = get_video_links(API_KEY, channel_id)
# print("Video Links:")
# for link in video_links:
#     print(link)


from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# API KEY
API_KEY = 'AIzaSyBhbYzOh_B3snsiBlCEwI4DdUZbKJVHass'

# youtube api client setup
youtube = build('youtube', 'v3', developerKey=API_KEY)

def getChannelVideos(channelId):
		try:
				# Get playlist ID of the uploaded videos playlist
				channelsRes = youtube.channels().list(
						part='contentDetails',
						id=channelId
				).execute()

				if 'items' in channelsRes and channelsRes['items']:
						playlistId = channelsRes['items'][0]['contentDetails']['relatedPlaylists']['uploads']

						playlistItemsResponse = youtube.playlistItems().list(
								part='contentDetails',
								playlistId=playlistId,
								maxResults=50
						).execute()

						video_ids = [item['contentDetails']['videoId'] for item in playlistItemsResponse.get('items', [])]
						return video_ids
				else:
						print("No videos found for the given channel.")
						return []

		except Exception as e:
				print(f"Error fetching channel videos: {e}")
				return []


def getCaptions(videoId):
		try:
				# get captions for the video
				captionResponse = youtube.captions().list(
						part='snippet',
						videoId=videoId
				).execute()

				captions = [item['snippet']['title'] for item in captionResponse['items']]
				return captions

		except Exception as e:
				print(f"Error fetching the captions: {e}")
				print(f"Captions Response: {captionResponse}")
				raise e

CHANNEL_ID = input('Enter the channel Id: ')

videoIds = getChannelVideos(CHANNEL_ID)

for video_id in videoIds:
		captions = getCaptions(video_id)
		print(f"Captions for video {video_id}: {captions}")


# try: 

#   # calling the search list method to recieve responses
#   search_response = youtube.search().list(
#     q=search_channel, type='video',
#     part='id,snippet', maxResults=50
#   ).execute()

#   # declaring some empty lists
#   videoUrl = []
#   videoId = []

#   # fetches the video urls, verifies them and then stores it in the empty list
#   for search_result in search_response.get('items', []):
#     if search_result['id']['kind'] == 'youtube#channel':
#       video_link = f"https://www.youtube.com/watch?v={search_result['id']['videoId']}"
#       video_id = search_result['videoId']
#       videoUrl.append(video_link)
#       videoId.append(video_id)

#     else:
#       print('there was some error in recieving the videos')
	

# except HttpError as err: 
#   print(f"An error occured: {err}")