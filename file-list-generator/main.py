__version__ = "1.0.0"

from pathlib import Path

from modules import display
from modules.fileoutput import output_file_list
from utils.dropfile import get_dropped_file
from utils.openfile import open_file

OUTPUT_FOLDER = Path().home() / "Downloads"
OPEN_OUTPUT = True


def get_source_folder() -> Path:
    print(
        " Drop the folder you'd like to list the contents of...\n",
        "The list will be saved as a text file in your Downloads folder.",
    )
    return get_dropped_file()


if __name__ == "__main__":
    display.ascii_art(__version__)
    source_folder = get_source_folder()
    output_filepath = output_file_list(
        source_folder=source_folder, target_folder=OUTPUT_FOLDER
    )
    if OPEN_OUTPUT:
        open_file(output_filepath)
