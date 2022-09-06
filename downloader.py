import os
from pytube import Playlist , YouTube


def downloadVideo(url):
    if url == '':
        print("Enter Valid Url")
        exit
    video = YouTube(url)
    path = video.title.replace('/','').replace(' ',"-")
    os.mkdir(path)
    print(video.title)
    print("Download Started...")
    video.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(path)
    print("Downloading Complete")
    print("===================================>")

def downloadSingleVideo():
    url = input("Enter Video Url : ")
    downloadVideo(url)

def downloadMultipleVideo():
    videos = []
    newItem = ''
    while newItem != 'quit' or newItem != '':
        newItem = input("Enter Video Url Or 'quit' : ")
        if newItem == 'quit' or newItem == '':
            break
        videos.append(newItem)
            
    for url in videos:
        downloadVideo(url)
        
def downloadPlaylist(url):
    if url == '':
        print("Enter Valid Url")
        exit
    list = Playlist(url)
    path = list.title.replace('/','').replace(' ',"-")
    os.mkdir(path)
    print(list.title)
    print("Playlist Started...")
    for video in list.videos:
        print(video.title)
        print("Download Started...")
        video.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download(path)
        print("Downloading Complete")
        print("===================================>")

    print("Playlist Download Complete")
    print("===================================>")


def downloadSinglePlaylist():
    url = input("Enter Playlist Url : ")
    downloadPlaylist(url)

def downloadMultiplePlaylist():
    playlists = []
    newItem = ''
    while newItem != 'quit' or newItem != '':
        newItem = input("Enter Playlist Url Or 'quit' : ")
        if newItem == 'quit' or newItem == '':
            break
        playlists.append(newItem)
        print(playlists)
    for url in playlists:
        downloadPlaylist(url)
        
        

print("Select Download Type: \n 1 = Video \n 2 = Playlist \n 3 = Multiple Video \n 4 = Multiple Playlist \n")
type = input("Enter Here : ")
if type == "1":
    # Single Vide
    downloadSingleVideo()
elif type == "2":
    # Single Playlist
    downloadSinglePlaylist()

elif type == "3":
    # Multiple Video
    downloadMultipleVideo()

elif type == "4":
    # Multiple Playlist
    downloadMultiplePlaylist()
else:
    print("Enter Valid Type")





# urls = [
#     # "https://youtube.com/playlist?list=PLW-zSkCnZ-gD8OcjTPu-u_Rxl9-kI9Xqr",
#     # "https://youtube.com/playlist?list=PLW-zSkCnZ-gABGZU8--ISUauyewG40Yex",
#     # "https://youtube.com/playlist?list=PLW-zSkCnZ-gDer-VZlBbe1f9-G0zNYdtg",
                #     "https://youtube.com/playlist?list=PLW-zSkCnZ-gA5Jn6gZtUa6-aG0OoRZyb6",
                #     "https://www.youtube.com/playlist?list=PL4cUxeGkcC9jLYyp2Aoh6hcWuxFDX6PBJ"
#     # "https://youtube.com/playlist?list=PLW-zSkCnZ-gBA67ZtNUjIMfc_kwLo3MET"
# ]
# path = "D:/Me/python/youtube-video-downloader-in-python/"

# for url in urls:
#     list = Playlist(url)
    
#     downloadPath = os.path.join(path, list.title) 
#     os.mkdir(downloadPath)
#     print(list.title)
#     print("Playlist Started...")
#     for video in list.videos:
#         print(video.title)
#         print("Download Started...")
#         video.streams.filter(progressive=True, file_extension='mp4').order_by(
#             'resolution').desc().first().download(downloadPath)
#         print("Downloading Complete")
#         print("===================================>")
    
#     print("Playlist Download Complete")
#     print("===================================>")