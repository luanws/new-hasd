

from typing import List

from src.models.hymn import Hymn
from src.services.video_service import VideoService
from src.utils.string import normalize


class HymnService:
    video_service: VideoService
    hymns: List[Hymn]

    def __init__(self, directory) -> None:
        self.video_service = VideoService(directory)
        self.update_hymns(False)

    def video_to_hymn(self, video: str) -> Hymn:
        hymn_path = self.video_service.get_video_path_from_video(video)
        hymn_name = video
        return Hymn(path=hymn_path, name=hymn_name)

    def update_hymns(self, update_videos: bool = True) -> List[Hymn]:
        if update_videos:
            self.video_service.update_videos()
        self.hymns = [self.video_to_hymn(video) for video in self.video_service.videos]
        return self.hymns

    def search_hymns(self, search_text: str) -> List[Hymn]:
        filtered_hymns = [hymn for hymn in self.hymns if normalize(search_text.lower()) in normalize(hymn.name.lower())]
        return filtered_hymns
