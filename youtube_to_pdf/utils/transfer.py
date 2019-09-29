import os


def silently_remove(path):
    try:
        os.remove(path)
    except os.error:
        pass


def silently_move(old_path, new_path, file):
    try:
        os.rename(os.path.join(old_path, file),
                  os.path.join(new_path, file))
    except os.error:
        pass
