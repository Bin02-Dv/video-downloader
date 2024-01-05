import yt_dlp

# get the video url
url = input("Enter the video Url: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video Download Successfully...")