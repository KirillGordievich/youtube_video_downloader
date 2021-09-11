import pytube
import pytube.request
import time


def progress_check(stream = None, chunk = 9437184, remaining=0):
    # Gets the percentage of the file that has been downloaded
    percent = int((100*(file_size-remaining))/file_size)
    print('%s%%' % percent)


global file_size
# Change the value here to something smaller to decrease chunk sizes,
#  thus increasing the number of times that the progress callback occurs
pytube.request.default_range_size = int(9437184/9) # 1MB chunk size


if __name__ == "__main__":
    path = 'D:/Kirill/Download'
    video_urls_file = open('urls.txt', 'r')
    video_urls = video_urls_file.readlines()
    for url in video_urls:
        start_time = time.time()
        youtube = pytube.YouTube(url, on_progress_callback=progress_check)
        video = youtube.streams.filter(adaptive=True).first()
        file_size = video.filesize
        title = video.title
        resolution = video.resolution
        print('Resolution: %s, Size: %s byte, Title: %s' % (resolution, file_size, title))
        print('Your video will be saved to: %s' % path)
        print('Downloaded: ')
        video.download(path)  # path, where to video download.
        print('The video "%s" has downloaded' % title)
        print("--- %s seconds ---" % (time.time() - start_time))
        print(' ')