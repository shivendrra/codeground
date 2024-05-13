from youtube_transcript_api import YouTubeTranscriptApi

def get_captions(video_url):
    try:
        # extracting video Id from Url and then fetching the captions
        video_id = video_url.split('v=')[1]
        captions = YouTubeTranscriptApi.get_transcript(video_id)

        # extracting the captions
        text = ' '.join([caption['text'] for caption in captions])

        # saving captions to a file
        with open('captions.txt', 'w', encoding='utf-8') as file:
            file.write(text)

        print(text)

    except Exception as e:
        print(f'Error: {str(e)}')

video_url = 'https://www.youtube.com/watch?v=JOiGEI9pQBs&ab_channel=Kurzgesagt%E2%80%93InaNutshell'
get_captions(video_url)