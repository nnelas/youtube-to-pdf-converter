import os
from os.path import isfile, join

from fpdf import FPDF
from natsort import natsorted

from youtube_to_pdf import settings
from youtube_to_pdf.models.video import Video


class Converter:
    @staticmethod
    def get_images(frames_path: str):
        image_list = [f for f in os.listdir(frames_path) if isfile(join(frames_path, f))]
        return natsorted(image_list)

    def from_image_to_pdf(self, video: Video) -> Video:
        pdf = FPDF()
        frames_path = os.path.join(settings.FRAMES_DIR, video.md5sum)
        pdf_path = os.path.join(settings.PDF_DIR, video.md5sum)

        for image in self.get_images(frames_path):
            pdf.add_page("L")
            pdf.image(os.path.join(frames_path, image))

        file_path = pdf_path + ".pdf"
        pdf.output(file_path, "F")
        video.pdf_path = file_path

        return video
