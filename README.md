# File Organizer

This Python script organizes files in a specified directory based on their file extensions. It creates separate folders for different file types and moves the files into their respective folders.

## Features

- Organizes files based on their extensions
- Creates folders for different file types if they don't exist
- Supports multiple file types including MP4, JPG, JPEG, PNG, GIF, and WEBM
- Prints progress and completion messages

## Usage

1. Clone this repository or download the `Organize.py` file.
2. Open the `Organize.py` file and modify the `directory` variable to point to the folder you want to organize.
3. Run the script using Python:

python Organize.py


## Supported File Types

- MP4 files: Moved to 'MP4_Files' folder
- JPG/JPEG files: Moved to 'JPG_Files' folder
- PNG files: Moved to 'PNG_Files' folder
- GIF files: Moved to 'GIF_Files' folder
- WEBM files: Moved to 'WEBM_Files' folder

## Requirements

- Python 3.x
- No additional libraries required (uses built-in `os` and `shutil` modules)

## Note

Make sure you have the necessary permissions to read from and write to the specified directory.
