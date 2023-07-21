import os
import shutil
from datetime import datetime

directory = 'F:/all photos'
output_directory = os.path.join(directory, 'sorted_images')
audio_directory = os.path.join(directory, 'audio')
films_directory = os.path.join(directory, 'films')
other_directory = os.path.join(directory, 'others')

os.makedirs(output_directory, exist_ok=True)
os.makedirs(audio_directory, exist_ok=True)
os.makedirs(films_directory, exist_ok=True)
os.makedirs(other_directory, exist_ok=True)

for root, _, files in os.walk(directory):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            timestamp = os.path.getmtime(file_path)
            creation_date = datetime.fromtimestamp(timestamp)
            folder_name = creation_date.strftime("%Y_%B")
            folder_path = os.path.join(output_directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            new_file_path = os.path.join(folder_path, file_name)
            # Handle existing files with the same name
            if os.path.exists(new_file_path):
                base_name, extension = os.path.splitext(file_name)
                counter = 1
                while True:
                    new_file_name = f"{base_name}_{counter}{extension}"
                    new_file_path = os.path.join(folder_path, new_file_name)
                    if not os.path.exists(new_file_path):
                        break
                    counter += 1
            shutil.move(file_path, new_file_path)
        elif file_name.lower().endswith(('.mp3', '.m4a', '.amr')):
            new_file_path = os.path.join(audio_directory, file_name)
            # Handle existing files with the same name
            if os.path.exists(new_file_path):
                base_name, extension = os.path.splitext(file_name)
                counter = 1
                while True:
                    new_file_name = f"{base_name}_{counter}{extension}"
                    new_file_path = os.path.join(audio_directory, new_file_name)
                    if not os.path.exists(new_file_path):
                        break
                    counter += 1
            shutil.move(file_path, new_file_path)
        elif file_name.lower().endswith(('.mov', '.mp4', 'mpg')):
            new_file_path = os.path.join(films_directory, file_name)
            # Handle existing files with the same name
            if os.path.exists(new_file_path):
                base_name, extension = os.path.splitext(file_name)
                counter = 1
                while True:
                    new_file_name = f"{base_name}_{counter}{extension}"
                    new_file_path = os.path.join(films_directory, new_file_name)
                    if not os.path.exists(new_file_path):
                        break
                    counter += 1
            shutil.move(file_path, new_file_path)
        else:
            new_file_path = os.path.join(other_directory, file_name)
            # Handle existing files with the same name
            if os.path.exists(new_file_path):
                base_name, extension = os.path.splitext(file_name)
                counter = 1
                while True:
                    new_file_name = f"{base_name}_{counter}{extension}"
                    new_file_path = os.path.join(other_directory, new_file_name)
                    if not os.path.exists(new_file_path):
                        break
                    counter += 1
            shutil.move(file_path, new_file_path)
