"""
Script used to develop a report of all processed files
"""

import csv
from datetime import datetime
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import pathlib
from track import Track

class Report:
    def __init__(self, files):
        self._files = files
        self._file_name = f'report-{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'

    @property
    def files(self):
        return self._files

    @property
    def file_name(self):
        return self._file_name

    def generate(self):
        header = ['Artist', 'Album', 'Title', 'BPM', 'Bit Rate', 'File', 'Error Code']

        with open(self.file_name, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)

            for file in self.files:
                try:
                    audio = MP3(file, ID3=EasyID3)
                    track = Track(audio)
                    writer.writerow([track.artist, track.album, track.title, track.bpm, track.bitrate, file, ''])
                except Exception as e:
                    print(f"Error parsing track data [{file}] - {str(e)}")
                    writer.writerow(['', '', '', '', '', file, str(e)])
                    continue