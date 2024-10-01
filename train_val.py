import os
import shutil
import random

# Define your source folders
image_folder = '/home/Documents/archive (1)/person_class/train_data_all/images'
label_folder = '/home/Documents/archive (1)/person_class/train_data_all/labels'

# Define your destination folders
train_image_folder = '/home/Documents/archive (1)/main_dataset/train/images'
train_label_folder = '/home/Documents/archive (1)/main_dataset/train/labels'
val_image_folder = '/home/Documents/archive (1)/main_dataset/val/images'
val_label_folder = '/home/Documents/archive (1)/main_dataset/val/labels'

# Ensure the destination directories exist
os.makedirs(train_image_folder, exist_ok=True)
os.makedirs(train_label_folder, exist_ok=True)
os.makedirs(val_image_folder, exist_ok=True)
os.makedirs(val_label_folder, exist_ok=True)

# Get a list of all image files in the image folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Shuffle the images and split them into 80% train and 20% val
random.shuffle(image_files)
split_index = int(0.8 * len(image_files))
train_images = image_files[:split_index]
val_images = image_files[split_index:]

# Function to move image and corresponding label
def move_image_and_label(image_file, destination_image_folder, destination_label_folder):
    # Construct full path for image and corresponding label
    image_path = os.path.join(image_folder, image_file)
    label_file = image_file.replace(image_file.split('.')[-1], 'txt')  # Assuming the label files are in .txt
    label_path = os.path.join(label_folder, label_file)
    
    # Move the image to the destination image folder
    shutil.move(image_path, os.path.join(destination_image_folder, image_file))
    
    # Move the corresponding label if it exists
    if os.path.exists(label_path):
        shutil.move(label_path, os.path.join(destination_label_folder, label_file))
    else:
        print(f"Warning: Label file for {image_file} not found!")

# Move training images and labels
for image_file in train_images:
    move_image_and_label(image_file, train_image_folder, train_label_folder)

# Move validation images and labels
for image_file in val_images:
    move_image_and_label(image_file, val_image_folder, val_label_folder)

print("Data split completed: 80% in train folder and 20% in val folder.")
