import os
import uuid

from pytube import YouTube

from youtube_to_pdf import settings
from youtube_to_pdf.engine.images.utils import print_progress_bar
from youtube_to_pdf.engine.video import helper
from youtube_to_pdf.models.video import Video


class Downloader:
    def download_video(self, video: Video) -> Video:
        file_md5sum = uuid.uuid4().hex

        def progress_function(stream, chunk, file_handle, bytes_remaining):
            progress = round((1 - bytes_remaining / stream.filesize) * 100, 2)
            print_progress_bar(int(progress), 100, prefix='Download:', suffix='Complete',
                               length=50)

        youtube = YouTube(video.url, on_progress_callback=progress_function)
        stream = youtube.streams.filter(adaptive=True).first()
        stream.download(settings.UPLOADING_DIR, file_md5sum)

        file_md5sum = helper.move_video_to(
            os.path.join(settings.UPLOADING_DIR, file_md5sum + ".mp4"),
            settings.VIDEO_DIR)

        video.md5sum = file_md5sum
        video.video_path = os.path.join(settings.VIDEO_DIR, file_md5sum + ".mp4")

        return video
