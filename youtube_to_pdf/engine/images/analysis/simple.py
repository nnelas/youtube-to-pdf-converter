import logging
import os

from youtube_to_pdf.engine.images.utils import get_images_diff
from youtube_to_pdf.models.compare import ImageCompare
from youtube_to_pdf.utils.transfer import silently_move, silently_remove


class SimpleImageAnalysis:
    def __init__(self, removed_path: str):
        self.removed_path = removed_path

    def simple_image_analysis(self, frames_path: str, image_list: list, report):
        def remove(compare: ImageCompare):
            if compare.diff == 0:   # totally equal file
                silently_move(compare.path, self.removed_path, compare.img_one)
                logging.debug("Moved file: '{file}' since diff is equal to 0"
                              .format(file=compare.img_one))

            elif compare.diff < 10:   # not much a difference
                silently_move(compare.path, self.removed_path, compare.img_one)
                logging.debug("Moved file: '{file}' since diff is less than 10"
                              .format(file=compare.img_one))

            elif compare.diff < 20:   # starting to get dangerous
                silently_move(compare.path, self.removed_path, compare.img_one)
                logging.debug("Moved file: '{file}' since diff is less than 20"
                              .format(file=compare.img_one))

        for idx, image in enumerate(image_list):
            if idx == len(image_list)-2:
                # last file seems to be always corrupted
                silently_remove(os.path.join(frames_path, image_list[idx+1]))
                break

            img_cmp = ImageCompare(img_one=image_list[idx], img_two=image_list[idx+1],
                                   diff=get_images_diff(frames_path, image_list, idx),
                                   path=frames_path)

            report.write("{}, {}, {}\n".format(img_cmp.img_one, img_cmp.img_two, img_cmp.diff))

            if not idx == 0:
                remove(img_cmp)
