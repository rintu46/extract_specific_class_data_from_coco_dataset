import os
import shutil
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# Define the paths
source_folder = '/home/Documents/archive (1)/person_class/val_data_all'
target_folder = '/home/Documents/archive (1)/person_class/train_data_all'
print('target_folder: ', target_folder)
os.makedirs(target_folder, exist_ok=True)

# Paths for images and labels inside source and target folders
source_image_folder = os.path.join(source_folder, 'images')
source_label_folder = os.path.join(source_folder, 'labels')
target_image_folder = os.path.join(target_folder, 'images')
target_label_folder = os.path.join(target_folder, 'labels')
print('target_label_folder: ', target_label_folder)



# Check if the source folders exist
if not os.path.exists(source_image_folder):
    raise FileNotFoundError(f"Image folder not found: {source_image_folder}")
if not os.path.exists(source_label_folder):
    raise FileNotFoundError(f"Label folder not found: {source_label_folder}")

# Create the target directories if they don't exist
os.makedirs(target_image_folder, exist_ok=True)
os.makedirs(target_label_folder, exist_ok=True)

# Function to copy files from one folder to another with tqdm progress bar
def copy_files(source, destination):
    file_names = os.listdir(source)
    for file_name in tqdm(file_names, desc=f"Copying from {source} to {destination}", unit="file"):
        source_file = os.path.join(source, file_name)
        if os.path.isfile(source_file):
            shutil.copy(source_file, destination)

# Create a ThreadPoolExecutor to run the copy operations concurrently
with ThreadPoolExecutor(max_workers=2) as executor:
    # Submit both copy operations to the executor
    executor.submit(copy_files, source_image_folder, target_image_folder)
    executor.submit(copy_files, source_label_folder, target_label_folder)

print("Files copied successfully!")
