from pytube import YouTube
from sys import argv

# Argv built in library for input command lines to access the link.
link = argv[1]
yt = YouTube(link)

# Print out the title of the youtube video you want to view
print("Title", yt.title)

# Print out the number of views the video has on youtube
print("View", yt.views)

# Gives the downloader the highest resolution of the video which is being downloaded
yd = yt.streams.get_highest_resolution()

# This statement is the downloading code
yd.download('')