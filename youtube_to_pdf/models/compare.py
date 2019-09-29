from dataclasses import dataclass


@dataclass
class ImageCompare:
    img_one: str
    img_two: str
    diff: float
    path: str
