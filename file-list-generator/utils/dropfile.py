__version__ = "1.1.1"

from pathlib import Path


def get_dropped_file() -> Path:
    file_location = input("\n Drop File: ")
    file_location = __clean_characters(file_location)
    return Path(file_location).resolve()


def __clean_characters(file_location: str) -> str:
    file_location = file_location.strip(" &'\"")
    file_location = file_location.replace("\ ", " ")
    file_location = file_location.replace("''", "'")
    return file_location
