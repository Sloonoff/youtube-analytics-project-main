import json
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    API_KEY = 'AIzaSyDsBEAxo4P9SfFuKeJImC8jgL9sQXfsbq4'

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = ''
        self.description = ''
        self.url = ''
        self.subscriber_count = 0
        self.video_count = 0
        self.view_count = 0

        # получение соответствующих значений из словаря channel
        channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = channel["items"][0]["snippet"]["title"]
        self.description = channel["items"][0]["snippet"]["description"]
        self.url = 'https://www.youtube.com/channel/' + channel_id
        self.subscriber_count = int(channel["items"][0]["statistics"]["subscriberCount"])
        self.video_count = int(channel["items"][0]["statistics"]["videoCount"])
        self.view_count = int(channel["items"][0]["statistics"]["viewCount"])

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=cls.API_KEY)

    def to_json(self, filename: str) -> None:
        """Сохраняет в файл значения атрибутов экземпляра Channel"""
        data = {
            'id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(f'Title: {self.title}')
        print(f'Description: {self.description}')
        print(f'URL: {self.url}')
        print(f'Subscriber count: {self.subscriber_count}')
        print(f'Video count: {self.video_count}')
        print(f'View count: {self.view_count}')
        print(f'View count: {self.view_count}')