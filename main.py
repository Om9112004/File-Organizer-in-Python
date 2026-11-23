import os
import shutil

# Folder path you want to organize
FOLDER_PATH = os.getcwd()

# File Types and their corresponding extensions
FILE_TYPES= {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx','.csv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.js', '.html', '.css', '.php'],
}

# Create Folders for each file type if they don't exist
for folder in FILE_TYPES.keys():
    folder_path = os.path.join(FOLDER_PATH, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files in the folder
for file in os.listdir(FOLDER_PATH):
    file_path= os.path.join(FOLDER_PATH, file)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    file_ext = os.path.splitext(file)[1].lower()

    for folder, extensions in FILE_TYPES.items():
        if file_ext in extensions:
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))

print("Files have been organized successfully!")
    