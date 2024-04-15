from pytube import YouTube
from sys import argv


link = argv[1]
youtube = YouTube(link)

print("Title: ", youtube.title)
print("Views: ", youtube.views)

downloader = youtube.streams.get_highest_resolution()
downloader.download('/home/wethinkcode/download')