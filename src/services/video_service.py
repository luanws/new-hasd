import os
from typing import List

from src.utils.string import normalize


class VideoService:
    directory: str

    def __init__(self, directory: str) -> None:
        self.directory = os.path.join(os.getcwd(), directory)

    def remove_file_extension(self, file_name: str) -> str:
        return ''.join(file_name.split('.')[:-1])

    def get_videos(self) -> List[str]:
        videos = os.listdir(self.directory)
        videos = [self.remove_file_extension(v) for v in videos]
        videos.sort()
        return videos

    def search_videos(self, search_text: str) -> List[str]:
        videos = self.get_videos()
        filtered_videos = [video for video in videos if normalize(search_text.lower()) in normalize(video.lower())]
        return filtered_videos
