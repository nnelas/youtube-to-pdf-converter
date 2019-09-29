# API parameters
import os

API_HOST = "localhost"
API_PORT = 5050

# Flask parameters
DEBUG = True

# Youtube API
DATA_DIR = os.path.join(os.path.expanduser("~"), "Documents", "python-projects")

# Video
UPLOADING_DIR = os.path.join(DATA_DIR, "uploading")
VIDEO_DIR = os.path.join(DATA_DIR, "videos")

# Frame
FRAMES_DIR = os.path.join(DATA_DIR, "frames")
FRAMES_TO_REMOVE_DIR = os.path.join(DATA_DIR, "removed")

# PDF
PDF_DIR = os.path.join(DATA_DIR, "pdfs")

# Report
REPORT_DIR = os.path.join(DATA_DIR, "report")
