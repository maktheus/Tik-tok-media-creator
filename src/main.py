from pytube import YouTube
import string



def clean_filename(title):
    title = title.lower()
    title = title.translate(str.maketrans("", "", string.punctuation))
    title = title.replace(" ", "_")
    return title

# get the video
yt = YouTube("https://www.youtube.com/watch?v=3D9Ft3J3Yx8")
title = clean_filename(yt.title)

#dowload the audio stream
audio = yt.streams.filter(only_audio=True).first()
audio.download(filename=title)


# download the video
