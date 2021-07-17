import pytube
import sys

SAVE_PATH = "/media/coderdude/Adwait/Study/Other Institutions/MIT/6.824 _Distributed_Systems/course_downloader/"

link = "https://youtu.be/668nUCeBHyY"


def percent(tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc


def progress_function(stream, chunk,bytes_remaining):

    size = video.filesize
    p = 0
    while p <= 100:
        progress = p
        print(str(p)+'%')
        p = percent(bytes_remaining, size)


try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = pytube.YouTube(link, on_progress_callback=progress_function)
except:
    print("Connection Error", sys.exc_info()[0]) #to handle exception



video = yt.streams.get_highest_resolution()

video.download(SAVE_PATH)

