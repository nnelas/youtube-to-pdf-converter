import logging

from youtube_to_pdf.engine.images.utils import get_images_diff
from youtube_to_pdf.models.compare import ImageCompare
from youtube_to_pdf.utils.transfer import silently_move


class AdvanceImageAnalysis:
    def __init__(self, removed_path: str):
        self.removed_path = removed_path

    def advance_image_analysis(self, frames_path: str, image_list: list, report) -> bool:
        """
            Diff between frame13.jpg and frame14.jpg: 58.010416666666664
            Diff between frame14.jpg and frame15.jpg: 58.923502604166664

            Given frame_a, frame_b and frame_c
            if diff_a && diff_b == diff_b && diff_c:
                # remove frame_b
        """

        def remove(compare_one: ImageCompare, compare_two: ImageCompare):
            if abs(compare_one.diff - compare_two.diff) < 1:
                silently_move(compare_two.path, self.removed_path,
                              compare_two.img_one)
                logging.debug("Moved file: '{file}' while advanced analysis"
                              .format(file=compare_two.img_one))
                return True

        for idx, image in enumerate(image_list):
            if idx == len(image_list)-2:
                # no need to compare last 3 files
                break

            img_cmp_one = ImageCompare(img_one=image_list[idx], img_two=image_list[idx+1],
                                       diff=get_images_diff(frames_path, image_list, idx),
                                       path=frames_path)
            img_cmp_two = ImageCompare(img_one=image_list[idx+1], img_two=image_list[idx+2],
                                       diff=get_images_diff(frames_path, image_list, idx+1),
                                       path=frames_path)

            report.write("{}, {}, {} - {}, {}, {} - {}\n"
                         .format(img_cmp_one.img_one, img_cmp_one.img_two, img_cmp_one.diff,
                                 img_cmp_two.img_one, img_cmp_two.img_two, img_cmp_two.diff,
                                 abs(img_cmp_one.diff - img_cmp_two.diff)))
            retry = remove(img_cmp_one, img_cmp_two)
            if retry is True:
                return retry
