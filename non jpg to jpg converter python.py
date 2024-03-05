import os
from PIL import Image

def convert_to_jpg(file_path):
    try:
        img = Image.open(file_path)
        if img.format != 'JPEG':
            jpg_path = os.path.splitext(file_path)[0] + '.jpg'
            img.convert('RGB').save(jpg_path)
            os.remove(file_path)
            print(f"Converted {file_path} to {jpg_path}")
    except Exception as e:
        print(f"Error converting {file_path}: {e}")

def convert_folder_to_jpg(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            convert_to_jpg(file_path)

# Specify the folder path
folder_path = 'new hawk'

# Convert all files in the folder and its subfolders to JPG
convert_folder_to_jpg(folder_path)
