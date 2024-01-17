from pytube import YouTube
link = input("Enter the link: ")
yt = YouTube(link)
vid = yt.streams.get_highest_resolution()
vid.download()
print("Done!")