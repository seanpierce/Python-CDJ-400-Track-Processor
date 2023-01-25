import glob
from pathlib import Path
import os
import shutil
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from track import Track


mp3_files = glob.iglob('**/*.mp3', recursive=True)

for file in mp3_files:
    try:
        file_path = os.path.abspath(file)
        dir_name = os.path.dirname(file_path).replace('\/\/', '/')
        audio = MP3(file, ID3=EasyID3)
        track = Track(audio)
        src = Path(dir_name) / Path(file)
        dst = Path(dir_name) / track.directory / track.file_name
    except Exception as e:
        print(f"Error collecting track data - {str(e)}")
    try:
        os.makedirs(os.path.dirname(track.directory), exist_ok=True)
    except Exception as e:
        print(f"Error making track directory - {str(e)}")
    try:
        shutil.copyfile(src, dst)
    except Exception as e:
        print(f"Error copying track to directory - {str(e)}")