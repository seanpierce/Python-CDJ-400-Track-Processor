import glob
import os
import shutil
from bpm import analyze
from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from report import Report
from track import Track


def run_report():
    print('Starting Report...')

    mp3_files = glob.glob('**/*.mp3', recursive=True)
    print(f'Found {len(mp3_files)} mp3 files')

    non_mp3_files = glob.glob('**/*[!.mp3]', recursive=True)
    print(f'Found {len(mp3_files)} non-mp3 files')

    report = Report(mp3_files)
    report.generate()
    report.append_non_mp3_files_to_report(non_mp3_files)

    print('Job Complete!')


def analyze():
    print('Analyzing...')

    mp3_files = glob.glob('**/*.mp3', recursive=True)
    print(f'Found {len(mp3_files)} files')

    for file in mp3_files:
        print(f"Processing {file}...")

        try:
            # get path variables
            file_path = os.path.abspath(file)
            dir_name = os.path.dirname(file_path)
        except Exception as e:
            print(f"Error collecting path information - {str(e)}")
            continue

        try:
            audio = MP3(file, ID3=EasyID3)
            # analyze bpm and persist it to the file's ID3 tags
            bpm = analyze(file_path)
            print(f'BPM: {bpm}')
            audio['bpm'] = bpm
            audio.save()

            track = Track(audio)
        except Exception as e:
            print(f"Error parsing track data - {str(e)}")
            continue

        try:
            # set source and destination directories
            src = file_path
            dst = Path(dir_name) / track.directory / track.file_name
            os.makedirs(Path(dir_name) / track.directory, exist_ok=True)
        except Exception as e:
            print(f"Error making track directory - {str(e)}")
            continue

        try:
            shutil.copyfile(src, dst)
            os.remove(file)
        except Exception as e:
            print(f"Error copying track to directory - {str(e)}")
            continue

    print('Job Complete!')