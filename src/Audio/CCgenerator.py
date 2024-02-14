import whisper
import string
import os
from src.Helpers.Helpers import clean_filename
from pytube import YouTube

delete_audio = False

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

def delete_audio_files():
    for file in os.listdir("audio_files"):
        os.remove(f"audio_files/{file}")


def generate_CC(url):
    model = whisper.load_model("base")
    result = model.transcribe(download_audio(url))
    print(result)
    try:
        delete_audio_file(download_audio(url))
    except:
        delete_audio_files()
        print("Audio file not found")

    return result

generate_CC("https://www.youtube.com/watch?v=i0mNnYP6w2w")
