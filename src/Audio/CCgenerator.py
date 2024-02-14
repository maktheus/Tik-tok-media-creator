import whisper
import string
import os
from pytube import YouTube

delete_audio = False

def clean_filename(title):
    title = title.lower()
    title = title.translate(str.maketrans("", "", string.punctuation))
    title = title.replace(" ", "_")
    return title

def download_audio(url):
    yt = YouTube(url)
    cleaned_title = clean_filename(yt.title)

    # Download the audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file_path = f"./audio_files/{cleaned_title}.mp3"
    audio_stream.download(output_path="audio_files", filename=cleaned_title + ".mp3")

    return audio_file_path

def delete_audio_file(audio_file_path):
    if delete_audio:
        print(f"Audio file is not saved at {audio_file_path}")
        return
    os.remove(audio_file_path)


def generate_CC(url):
    model = whisper.load_model("base")
    result = model.transcribe(download_audio(url))
    print(result["text"])
    
    return result["text"]

    


generate_CC("https://www.youtube.com/watch?v=i0mNnYP6w2w")
