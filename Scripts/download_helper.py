import platform
import os
import shutil

def detect_download_path():
    if platform.system() == 'Windows':
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    elif platform.system() == "Darwin":  
        return os.path.join(os.environ['HOME'], 'Downloads')
    else:  
        return os.path.join(os.environ['HOME'], 'Downloads')
    
def get_file_type(file_extension):
    file_type_mapping = {
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx', '.csv'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv'],
        'Music': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.bz2', '.7z'],
        'Executables': ['.exe', '.msi', '.sh', '.bat', '.jar'],
        'Images' : ['.iso'],
    }
    for folder, extensions in file_type_mapping.items():
        if file_extension in extensions:
            return folder
    return 'Others'

def process_files(file_path, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.move(file_path, destination_folder)

def sort_downloads():
    download_path = detect_download_path()
    for filename in os.listdir(download_path):
        file_path = os.path.join(download_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            folder_name = get_file_type(file_extension)
            destination_folder = os.path.join(download_path, folder_name)
            process_files(file_path, destination_folder)
            print(f"Moved {filename} to {folder_name}/")


if __name__ == "__main__":
    sort_downloads()