from googleapiclient.discovery import build   #Дз_4

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
DEVELOPER_KEY = 'AIzaSyDsBEAxo4P9SfFuKeJImC8jgL9sQXfsbq4'


class Video:
    def __init__(self, video_id):
        self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                             developerKey=DEVELOPER_KEY)
        self.video_id = video_id
        video_response = self.youtube.videos().list(part='snippet,statistics', id=video_id).execute()
        self.title = video_response['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.views = video_response['items'][0]['statistics']['viewCount']
        self.likes = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
         return super().__str__()
