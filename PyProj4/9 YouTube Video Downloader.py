from pytube import YouTube

link = input("enter the link of the video here : ")
youtube_1 = YouTube(link)

# print (youtube_1.thumbnail_url)
# videos = youtube_1.streams.all() # All Format
# videos = youtube_1.streams.filter(only_audio=True) # Only audio
videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("enter : "))
videos[strm].download()
print('Successfully')

