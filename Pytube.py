from pytube import YouTube

link = input('Enter video URL:')
yt = YouTube(link)
print('downloading...')
yt.streams.first().download()
print('Finish')
