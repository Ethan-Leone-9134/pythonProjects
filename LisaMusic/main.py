from pydub import AudioSegment
import os

import ffmpeg
import shutil

def convert_m4a_to_mp3(m4a_file, mp3_file):
    ffmpeg.input(m4a_file).output(mp3_file, format='mp3').run(
        cmd=r"C:\Users\zaper\Downloads\ffmpeg-builder\ffmpeg-2024-12-19-git-494c961379-full_build\bin\ffmpeg.exe",
        quiet=True,  # Suppresses the logs
        overwrite_output=True  # Overwrites the file if it exists
    )



current_directory = os.getcwd()                         # Folder directory
directory = f"{os.getcwd()}\\ITUNES MUSIC COLLECTION"   # Search directory
newDirect = f"{os.getcwd()}\\SpeakerMusic"

# List all folders in the specified directory
folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
count = 0
for artistName in folders:
    folderPath = f"{directory}\\{artistName}"
    files = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
    
    for songName in files:
        count += 1
        oldPath = f"{folderPath}\\{songName}"
        if songName[-4:] == ".m4a":
            newSongName = f"{artistName} - {songName}".replace(".m4a",".mp3")
            newPath = f"{newDirect}\\{newSongName}"

            if not(os.path.exists(newPath)):
                print(f"{newSongName}, {count}/789")
                print(" ")
                convert_m4a_to_mp3(oldPath, newPath)
            # print()
        elif (songName[-4:] == ".mp3"):
            newPath = f"{newDirect}\\{artistName} - {songName}"
            if not(os.path.exists(newPath)):
                print(f"{newSongName}, {count}/789")
                print(" ")
                shutil.copy(oldPath, newPath)

        else:
            pass
            # print(oldPath)
