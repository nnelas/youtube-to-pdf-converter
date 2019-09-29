from dataclasses import dataclass, field


@dataclass
class Video:
    url: str
    description: str = field(default=None)
    md5sum: str = field(default=None)
    video_path: str = field(default=None)
    report_path: list = field(default=None)
    pdf_path: str = field(default=None)
