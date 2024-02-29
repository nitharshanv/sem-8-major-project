'''
import os
import numpy as np

num_skipped = 0

a=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Bat"
b=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Car"
c=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Grenade"
d=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Knife"
e=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Machine Guns"
f=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Masked Face"
g=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Motorcycle"
h=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Pistol"
i=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\RPG"
j=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Truck"
main_fol=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\test"
folders=[a,b,c,d,e,f,g,h,i,j]
for folder_name in folders:
    folder_path = os.path.join(main_fol, folder_name)
    for fname in os.listdir(folder_path):
        fpath = os.path.join(folder_path, fname)
        try:
            fobj = open(fpath, "rb")
            is_jfif = b"JFIF" in fobj.peek(10)
        finally:
            fobj.close()
        if not is_jfif:
            num_skipped += 1
            # Delete corrupted image
            os.remove(fpath)
print(f"Deleted {num_skipped} images.")
'''
from pathlib import Path
import filetype


a=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Bat"
b=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Car"
c=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Grenade"
d=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Knife"
e=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Machine Guns"
f=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Masked Face"
g=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Motorcycle"
h=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Pistol"
i=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\RPG"
j=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train\Truck"
main_fol=r"D:\Hawk_Eye_dataset-20240209T072717Z-001\Hawk_Eye_dataset\Train"
folders=[a,b,c,d,e,f,g,h,i,j]
# RFC image file extensions supported by TensorFlow
img_exts = {"png", "jpg", "gif", "bmp"}
for i in folders:
  path = Path(i)

  for file in path.iterdir():
    if file.is_dir():
        continue

    ext = filetype.guess_extension(file)

    if ext is None:
        print(f"'{file}': extension cannot be guessed from content")
    elif ext not in img_exts:
        print(f"'{file}': not a supported image file")
    else:
        print("nothing")