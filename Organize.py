import os
import shutil

# Specify the directory you want to organize
directory = r"C:\Users\Name\Downloads\Folder_Name" # Replace with the actual directory path

# Define the extensions and their corresponding folders
extensions = {
    '.mp4': 'MP4_Files',
    '.jpg': 'JPG_Files',
    '.jpeg': 'JPG_Files',
    '.png': 'PNG_Files',
    '.gif': 'GIF_Files',
    '.webm': 'WEBM_Files',
}

# Create folders for each extension if they don't exist
for ext, folder in extensions.items():
    folder_path = os.path.join(directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

# Iterate over all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    # Skip if it's a directory
    if os.path.isdir(file_path):
        continue
    
    # Get the file extension in lowercase
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    
    # If the file has one of the specified extensions, move it
    if ext in extensions:
        destination = os.path.join(directory, extensions[ext], filename)
        shutil.move(file_path, destination)
        print(f"Moved {filename} to {extensions[ext]}/")
        
print("Organization complete!")
