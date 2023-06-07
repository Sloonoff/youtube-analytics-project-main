import requests

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self._api_key = "your_api_key" # замените на свой API ключ
        self._base_url = "https://www.googleapis.com/youtube/v3"
        self._data = self._get_channel_data()

    def _get_channel_data(self) -> dict:
        """Метод для получения данных о канале по его id"""
        url = f"{self._base_url}/channels?part=snippet&id={self.channel_id}&key={self._api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_title = self._data["items"][0]["snippet"]["title"]
        channel_description = self._data["items"][0]["snippet"]["description"]
        print(f"Название канала: {channel_title}")
        print(f"Описание канала: {channel_description}")

    def get_playlists(self) -> list:
        """Метод для получения списка плейлистов канала"""
        url = f"{self._base_url}/playlists?part=snippet&channelId={self.channel_id}&key={self._api_key}"
        response = requests.get(url)
        data = response.json()
        playlists = []
        for item in data["items"]:
            playlist_id = item["id"]
            playlist_title = item["snippet"]["title"]
            playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
            playlists.append({"id": playlist_id, "title": playlist_title, "url": playlist_url})
        return playlists

    def get_most_popular_video(self) -> str:
        """Метод для получения ссылки на самое популярное видео канала"""
        url = f"{self._base_url}/search?part=snippet&channelId={self.channel_id}&type=video&order=viewCount&maxResults=1&key={self._api_key}"
        response = requests.get(url)
        data = response.json()
        video_id = data["items"][0]["id"]["videoId"]
        video_url = f"https://youtu.be/{video_id}"
        return video_url
