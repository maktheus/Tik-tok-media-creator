import os
import string
from pytube import YouTube
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Helpers.Helpers import clean_filename


def download_video(url):
    yt = YouTube(url)
    cleaned_title = clean_filename(yt.title)
    # Download the video stream
    video_stream = yt.streams.filter().first()
    video_file_path = f"./video_files/{cleaned_title}.mp3"
    video_stream.download(output_path="video_files", filename=cleaned_title + ".mp3")
    return video_file_path