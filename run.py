import glob
import os
import shutil
from bpm import analyze
from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from track import Track


def run():
    print('Begin...')
    mp3_files = glob.iglob('*.mp3', recursive=False)

    for file in mp3_files:
        try:
            # get path variables
            file_path = os.path.abspath(file)
            dir_name = os.path.dirname(file_path)
        except Exception as e:
            print(f"Error collecting path information - {str(e)}")

        try:
            print(f"Processing {file}...")
            audio = MP3(file, ID3=EasyID3)
            
            # analyze bpm and persist it to the file's ID3 tags
            bpm = analyze(file_path)
            print(f'BPM: {bpm}')
            audio['bpm'] = bpm
            audio.save()

            track = Track(audio)
        except Exception as e:
            print(f"Error parsing track data - {str(e)}")

        try:
            # set source and destination directories
            src = Path(dir_name) / Path(file)
            dst = Path(dir_name) / track.directory / track.file_name
        except Exception as e:
            print(f"Error setting up directory information - {str(e)}")

        try:
            os.makedirs(os.path.dirname(track.directory), exist_ok=True)
        except Exception as e:
            print(f"Error making track directory - {str(e)}")

        try:
            shutil.copyfile(src, dst)
        except Exception as e:
            print(f"Error copying track to directory - {str(e)}")