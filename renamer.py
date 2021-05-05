from os import listdir
import os

# get script directory and change os path to it
script_dir = os.path.abspath(__file__)[:-10]
os.chdir(script_dir)
videoExtensions = ['.mkv', '.mp4']
subtitleExtensions = ['.srt', '.ass']

# create the lists
videos = []
subs = []
allFiles = os.listdir()
allFiles.sort()
for file in allFiles:
    if file[-4:] in videoExtensions:
        videos.append(file)
    elif file[-4:] in subtitleExtensions:
        subs.append(file)
print('found', len(videos), 'videos, and', len(subs), 'subs')

# rename files
for epNum, sub in enumerate(subs):
    oldName = sub
    newName = videos[epNum][:-4] + sub[-4:]
    try:
        os.rename(oldName, newName)
    except IndexError:
        print("mismatched number of videos/subs")
        break
print("--> OPERATION COMPLETE")