import os

import numpy
from cv2 import cv2


def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100,
                       fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def get_images_diff(frames_path: str, image_list: list, idx: int):
    img1 = cv2.imread(os.path.join(frames_path, image_list[idx]), 0)
    img2 = cv2.imread(os.path.join(frames_path, image_list[idx+1]), 0)

    # --- take the absolute difference of the images ---
    res = cv2.absdiff(img1, img2)

    # --- convert the result to integer type ---
    res = res.astype(numpy.uint32)

    # --- find percentage difference based on number of pixels that are not zero ---
    return (numpy.count_nonzero(res) * 100) / res.size
