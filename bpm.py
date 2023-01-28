"""
Module used to analyze bpm of a file.
Invokes the consolebpm.exe application developed by abyssmedia.
https://www.abyssmedia.com/bpmcounter/
"""

import pathlib
import subprocess


def analyze_bpm(file):
    cwd = pathlib.Path(__file__).parent.resolve()
    console_path = f'{cwd}/console/consolebpm.exe'
    result = subprocess.run([console_path, file], shell=True, capture_output=True)

    if result.returncode == 0:
        return str(result.stdout.strip(), 'utf-8', 'ignore')
    else: 
        return None