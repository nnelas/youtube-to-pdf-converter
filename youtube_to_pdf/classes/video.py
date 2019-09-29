import logging

import colorlog

from youtube_to_pdf.engine.video import converter as v
from youtube_to_pdf.engine.video.downloader import Downloader
from youtube_to_pdf.engine.images import compare as images
from youtube_to_pdf.engine.pdf import converter as p
from youtube_to_pdf.models.video import Video


def make_logger(level=logging.DEBUG):
    log_format = ("%(asctime)s %(log_color)s%(levelname)-8s"
                  "%(reset)s %(white)s%(message)s")
    date_format = "%Y-%m-%d %H:%M:%S"
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        log_format, datefmt=date_format, reset=True))

    logger = colorlog.getLogger()
    logger.handlers = []
    logger.addHandler(handler)
    logger.setLevel(level)

    return logger


class ManagedApp:
    def __init__(self, video: Video):
        self.video = video
        self.downloader = Downloader()
        self.video_converter = v.Converter()
        self.compare = images.Compare()
        self.pdf_converter = p.Converter()
        self.logger = make_logger()

    def download_video(self) -> Video:
        self.logger.info("Downloading video...")
        video = self.downloader.download_video(self.video)
        return video

    def video_to_frames(self, video: Video) -> Video:
        self.logger.info("Converting video to frames...")
        video = self.video_converter.extract_images(video)
        return video

    def compare_frames(self, video: Video) -> Video:
        self.logger.info("Comparing frames...")
        self.compare.setup(video)
        video = self.compare.compare_images(video)
        return video

    def frames_to_pdf(self, video: Video) -> Video:
        self.logger.info("Converting frames to pdf...")
        video = self.pdf_converter.from_image_to_pdf(video)
        return video

    def run(self) -> Video:
        video = self.download_video()
        video = self.video_to_frames(video)
        video = self.compare_frames(video)
        video = self.frames_to_pdf(video)
        logging.debug("Converted video: {}".format(video.__str__()))
        return video
