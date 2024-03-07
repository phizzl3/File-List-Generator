#!/usr/bin/env python3
"""
Gets a folder via drag-and-drop and outputs a text file with a list
of all of the files and folders the source folder contains. 
"""


import time
from pathlib import Path

import listgen
from utils import dropfile
from utils.openfile import openfile

# Set output folder in user's Home directory and T/F to open output file
OUTPUT_FOLDER = "Downloads"
OPEN_FILE = True

# Generate output Path
target_folder = Path().home().resolve() / OUTPUT_FOLDER

# Get source filepath
print("\n Drop the folder you'd like to list the contents of...")
source_folder = dropfile.get()

# List files and output text file with contents
output_file = listgen.main(source_folder=source_folder,
                           target_folder=target_folder)

# Optionally open output file or display a message
if OPEN_FILE:
    openfile(output_file)
else:
    print(f"\n File saved to {output_file}")
    time.sleep(3)
