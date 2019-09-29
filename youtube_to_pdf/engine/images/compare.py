import os
from os.path import isfile, join

from youtube_to_pdf import settings
from natsort import natsorted

from youtube_to_pdf.engine.images.analysis.advance import AdvanceImageAnalysis
from youtube_to_pdf.engine.images.analysis.simple import SimpleImageAnalysis
from youtube_to_pdf.models.video import Video


class Compare:
    removed_path: str
    simple_analysis: SimpleImageAnalysis
    advance_analysis: AdvanceImageAnalysis

    def setup(self, video: Video):
        self.removed_path = os.path.join(settings.FRAMES_TO_REMOVE_DIR, video.md5sum)
        self.simple_analysis = SimpleImageAnalysis(self.removed_path)
        self.advance_analysis = AdvanceImageAnalysis(self.removed_path)

    @staticmethod
    def get_images(frames_path: str):
        image_list = [f for f in os.listdir(frames_path) if isfile(join(frames_path, f))]
        return natsorted(image_list)

    def compare_images(self, video: Video) -> Video:
        retry = True
        frames_path = os.path.join(settings.FRAMES_DIR, video.md5sum)
        report_path = os.path.join(settings.REPORT_DIR, video.md5sum)

        if not os.path.exists(self.removed_path):
            os.makedirs(self.removed_path)

        if not os.path.exists(report_path):
            os.makedirs(report_path)

        simple_report_path = os.path.join(report_path, "simple_report.txt")
        simple_report = open(simple_report_path, "w")
        simple_report.write("simple_image_analysis\n")
        self.simple_analysis.simple_image_analysis(
            frames_path, self.get_images(frames_path), simple_report)

        advance_report_path = os.path.join(report_path, "advance_report.txt")
        advance_report = open(advance_report_path, "w")
        advance_report.write("advance_image_analysis\n")
        while retry:
            retry = self.advance_analysis.advance_image_analysis(
                frames_path, self.get_images(frames_path), advance_report)

        simple_report.close()
        advance_report.close()

        video.report_path = [simple_report_path, advance_report_path]
        return video
