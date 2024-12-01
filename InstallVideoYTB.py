from plyer import audio
from pytube import Youtube

# Get a url video in youtube
url = input("Enter a url you wanna install: ")

# Use some alogrithm to take all data about the video insert
yt = Youtube(url)

#Filter audio streams and download the first one
audio_stream = yt.streams.filter(only_audio=True).first()

# Download
audio_stream.dowload()