import logging
import os

from youtube_to_pdf.utils.type import get_file_md5sum


def move_video_to(internal_video_path, destination_dir):
    # Get the Video's MD5 sum and ensure that it does not exist already
    video_md5sum = get_file_md5sum(internal_video_path)
    expected_video_path = os.path.join(destination_dir, video_md5sum + ".mp4")
    if not os.path.exists(destination_dir):     # create destination_dir
        os.makedirs(destination_dir)
    if not os.path.exists(expected_video_path):     # move file if not exists on destination
        os.rename(internal_video_path, expected_video_path)
    else:
        logging.debug("File with md5sum '{}' already exists on destination folder"
                      .format(video_md5sum))
    return video_md5sum
