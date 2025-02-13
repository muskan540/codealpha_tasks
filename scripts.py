import os
import shutil

def organize_files(directory):
    """
    Organizes files in the given directory into subfolders based on file types.
    
    :param directory: The path of the directory to organize.+
    """
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".html", ".css"],
    }

    for folder, extensions in file_types.items():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True) 

        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path) and os.path.splitext(file)[1].lower() in extensions:
                shutil.move(file_path, folder_path)

    print(f"Files in '{directory}' have been organized.")

directory_to_organize = "D:\CodeAlpha"
organize_files(directory_to_organize)