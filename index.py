import os
import sys
import urllib.request
import time

if len(sys.argv) < 5:
    print("Usage: ")
    exit("python3 index.py /path/to/download/folder/ https://example.com/<<file>>.mp4 totalEpisodes startEpisode")



fileMask = "<<file>>"
series = int(sys.argv[3])
actual = int(sys.argv[4])
current = int(actual)

folder = sys.argv[1]
url = sys.argv[2]

name, ext = os.path.splitext(url)

def reporthook(count, block_size, total_size):

    global start_time
    global current
    
    if count == 0:
        start_time = time.time()
        return
    
    duration = time.time() - start_time
    
    progress_size = int(count * block_size)
    
    speed = int(progress_size / (1024 * duration))
    
    percent = int(count * block_size * 100 / total_size)
    
    sys.stdout.write("\rDowload episode № %d: %d%%, %d MB, %d KB/s, %d seconds passed" % (current, percent, progress_size / (1024 * 1024), speed, duration))
    
    sys.stdout.flush()

print("Info :")
print(f"Start Episode: {actual}")
print(f"Episodes Total: {series}")
print(f"Download Folder: {folder}")
print(f"URL: {url}\n")

for i in range(actual, series+1):

    if len(str(i)) < 2: i = f"0{i}"

    current = int(i)
    
    urllib.request.urlretrieve(url.replace(fileMask, str(i)), f"{folder}{current}{ext}", reporthook)