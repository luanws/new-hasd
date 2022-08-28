import os
from typing import List


class VideoService:
    directory: str

    def __init__(self, directory: str) -> None:
        self.directory = os.path.join(os.getcwd(), directory)

    def get_videos(self) -> List[str]:
        videos = os.listdir(self.directory)
        videos.sort()
        return videos

    def search_videos(self, search_text: str) -> List[str]:
        videos = self.get_videos()
        filtered_videos = [video for video in videos if search_text in video]
        return filtered_videos
