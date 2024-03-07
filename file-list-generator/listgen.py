import os
from pathlib import Path


def main(source_folder: Path, target_folder: Path) -> Path:
    """Gets a source folder and a target folder, lists all files and 
    folders contained in the source folder and writes a text file with
    the information out to the target folder.

    Args:
        source_folder (Path): Folder containing the files/folders to list.
        target_folder (Path): Folder where the text file containing the list
        should be saved.

    Returns:
        Path: Path to the output text file with the listed files/folders.
    """
    # Set output text file name
    output_file = f"{target_folder}/{source_folder.name}.txt"

    # Walk the directory and write the file
    with open(output_file, 'w') as text_file:
        # Check each nested directory
        for root, _dirs, files in sorted(os.walk(source_folder)):
            # Write folder info
            text_file.write(f"Folder:\n")
            text_file.write(f'{root}\n\n')
            # Write file list
            text_file.write("Files:\n")
            for file in files:
                text_file.write(f'{file}\n')
            # Write separator
            text_file.write("\n\n")
            text_file.write("-" * 30)
            text_file.write("\n\n")

    return Path(output_file)
