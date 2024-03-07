import os
from pathlib import Path


def output_file_list(source_folder: Path, target_folder: Path) -> Path:

    output_file = __set_output(sf=source_folder, tf=target_folder)
    with open(output_file, "w") as text_file:
        for root, _dirs, files in sorted(os.walk(source_folder)):
            __write_folder_info(text_file, root)
            __write_file_list(text_file, files)
            __write_separator(text_file)

    return Path(output_file)


def __set_output(sf: Path, tf: Path) -> Path:
    return Path(f"{tf / sf.name}_file_list.txt")


def __write_folder_info(text_file, root) -> None:
    text_file.write(f"Folder:\n")
    text_file.write(f"{root}\n\n")


def __write_file_list(text_file, files) -> None:
    text_file.write("Files:\n")
    for file in files:
        text_file.write(f"{file}\n")


def __write_separator(text_file) -> None:
    text_file.write("\n\n")
    text_file.write("-" * 30)
    text_file.write("\n\n")
