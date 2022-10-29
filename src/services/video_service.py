import os
import re
from typing import List

from src.utils.string import normalize


class VideoService:
    directory: str
    video_extension: str = 'mp4'
    videos: List[str] = []

    def __init__(self, directory: str) -> None:
        self.directory = os.path.join(os.getcwd(), directory)
        self.update_videos()

    def remove_file_extension(self, file_name: str) -> str:
        return ''.join(file_name.split('.')[:-1])

    def update_videos(self) -> List[str]:
        self.videos = os.listdir(self.directory)
        self.videos = [self.remove_file_extension(v) for v in self.videos]
        self.videos.sort(key=self.__get_sort_videos_key())
        return self.videos

    def __get_sort_videos_key(self):
        size = len(self.videos)

        def sort_videos_key(video: str) -> int:
            match = re.search(r'^(\d+)', video)
            video_number = match.group(0) if match else size + 1
            return int(video_number)
        return sort_videos_key

    def search_videos(self, search_text: str) -> List[str]:
        filtered_videos = [video for video in self.videos if normalize(search_text.lower()) in normalize(video.lower())]
        return filtered_videos

    def get_video_path_from_video(self, video: str) -> str:
        return os.path.join(self.directory, f'{video}.{self.video_extension}')
