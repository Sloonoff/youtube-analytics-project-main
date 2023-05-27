import json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    API_KEY = 'AIzaSyDsBEAxo4P9SfFuKeJImC8jgL9sQXfsbq4'

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = ""
        self.description = ""
        self.url = ""
        self.subscriber_count = 0
        self.video_count = 0
        self.view_count = 0
        self.get_channel_info()


    def get_channel_info(self) -> None:
        """Получает информацию о канале по API и заполняет соответствующие атрибуты"""
        channel = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = channel["items"][0]["snippet"]["title"]
        self.description = channel["items"][0]["snippet"]["description"]
        self.url = 'https://www.youtube.com/channel/' + self.channel_id
        self.subscriber_count = int(channel["items"][0]["statistics"]["subscriberCount"])
        self.video_count = int(channel["items"][0]["statistics"]["videoCount"])
        self.view_count = int(channel["items"][0]["statistics"]["viewCount"])

    def __str__(self) -> str:
        """Возвращает название и ссылку на канал в формате <название_канала> (<ссылка_на_канал>)"""
        return f"{self.title} ({self.url})"

    def __add__(self, other: "Channel") -> int:
        """Возвращает количество подписчиков двух каналов, если их сложить"""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other: "Channel") -> int:
        """Возвращает разницу в количестве подписчиков двух каналов"""
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other: "Channel") -> bool:
        """Проверяет, что первый канал имеет больше подписчиков, чем второй"""
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other: "Channel") -> bool:
        """Проверяет, что первый канал имеет больше или равное количество подписчиков, чем второй"""
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other: "Channel") -> bool:
        """Проверяет, что первый канал имеет меньше подписчиков, чем второй"""
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other: "Channel") -> bool:
        """Проверяет, что первый канал имеет меньше или равное количество подписчиков, чем второй"""
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other: "Channel") -> bool:
        """Проверяет, что количество подписчиков двух каналов равно"""
        return self.subscriber_count == other.subscriber_count

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
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=cls.API_KEY)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(f'Title: {self.title}')
        print(f'Description: {self.description}')
        print(f'URL: {self.url}')
        print(f'Subscriber count: {self.subscriber_count}')
        print(f'Video count: {self.video_count}')
        print(f'View count: {self.view_count}')