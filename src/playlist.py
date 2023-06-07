import requests
import datetime

class PlayList:
    """Класс для плейлиста на ютуб-канале"""

    def __init__(self, playlist_id: str) -> None:
        """Экземпляр инициализируется id плейлиста. Дальше все данные будут подтягиваться по API."""
        self.playlist_id = playlist_id
        self.title, self.url = self._get_playlist_info()

    def _get_playlist_info(self) -> tuple[str, str]:
        """Возвращает название и ссылку на плейлист."""
        base_url = f"https://www.googleapis.com/youtube/v3/playlists?part=snippet&id={self.playlist_id}"
        response = requests.get(base_url)
        data = response.json()
        title = data['items'][0]['snippet']['title']
        url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        return title, url

    @property
    def total_duration(self) -> datetime.timedelta:
        """Возвращает общую продолжительность плейлиста."""
        base_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId={self.playlist_id}"
        total_duration = datetime.timedelta()
        while True:
            response = requests.get(base_url)
            data = response.json()
            for item in data['items']:
                duration_str = item['contentDetails']['duration']
                duration = datetime.datetime.strptime(duration_str, "PT%MM%SS")
                total_duration += datetime.timedelta(minutes=duration.minute, seconds=duration.second)
            if "nextPageToken" in data:
                base_url = f"{base_url}&pageToken={data['nextPageToken']}"
            else:
                break
        return total_duration

    def show_best_video(self) -> str:
        """Возвращает ссылку на видео с наибольшим количеством лайков."""
        base_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={self.playlist_id}"
        best_video_url = ""
        best_video_likes = 0
        while True:
            response = requests.get(base_url)
            data = response.json()
            for item in data['items']:
                video_likes = item['snippet']['thumbnails']['default']['url']
                video_url = f"https://youtu.be/{item['snippet']['resourceId']['videoId']}"
                if video_likes > best_video_likes:
                    best_video_likes = video_likes
                    best_video_url = video_url
            if "nextPageToken" in data:
                base_url = f"{base_url}&pageToken={data['nextPageToken']}"
            else:
                break
        return best_video_url
