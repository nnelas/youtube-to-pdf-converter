import logging
import os

from cv2 import cv2

from youtube_to_pdf import settings
from youtube_to_pdf.models.video import Video


class Converter:
    def extract_images(self, video: Video) -> Video:
        count = 0

        logging.debug(video.video_path)
        frames_path = os.path.join(settings.FRAMES_DIR, video.md5sum)

        if not os.path.exists(frames_path):
            os.makedirs(frames_path)

        vidcap = cv2.VideoCapture(video.video_path)
        success, image = vidcap.read()
        while success:
            vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))  # added this line
            success, image = vidcap.read()
            # logging.debug('Read a new frame: {}'.format(success))

            # save frame as JPEG file
            cv2.imwrite(os.path.join(frames_path, "frame%d.jpg" % count), image)
            count = count + 1

        return video
