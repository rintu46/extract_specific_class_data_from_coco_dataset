import os
import shutil

# Define your source and destination directories
image_folder = '/home/Documents/archive (1)/coco2014/images/train2014'
label_folder = '/home/Documents/archive (1)/coco2014/labels/train2014'

# Define your destination directories
destination_image_folder = '/home/Documents/archive (1)/person_class/train_data_all/images'
destination_label_folder = '/home/Documents/archive (1)/person_class/train_data_all/labels'

# Ensure the destination directories exist
os.makedirs(destination_image_folder, exist_ok=True)
os.makedirs(destination_label_folder, exist_ok=True)

def clean_label_file(label_path):
    """This function reads the label file, removes lines with a class other than 0,
    removes duplicates, and writes the cleaned data back."""
    with open(label_path, 'r') as label_file:
        lines = label_file.readlines()

    # Keep only lines where the first number is '0' and remove duplicates
    cleaned_lines = list({line for line in lines if line.strip() and line[0] == '0'})

    return cleaned_lines

# Traverse the image folder
for image_file in os.listdir(image_folder):
    if image_file.endswith(('.jpg', '.jpeg', '.png')):  # Handle different image extensions
        image_path = os.path.join(image_folder, image_file)
        label_file = image_file.replace(image_file.split('.')[-1], 'txt')  # Assumes label is in .txt format
        label_path = os.path.join(label_folder, label_file)

        # Check if corresponding label file exists
        if os.path.exists(label_path):
            cleaned_lines = clean_label_file(label_path)

            if cleaned_lines:
                # Save cleaned label if there's at least one valid line
                cleaned_label_path = os.path.join(destination_label_folder, label_file)
                with open(cleaned_label_path, 'w') as cleaned_label:
                    cleaned_label.writelines(cleaned_lines)

                # Copy the image to the destination folder
                shutil.copy(image_path, os.path.join(destination_image_folder, image_file))
                print(f"Copied {image_file} and cleaned {label_file}")
            else:
                print(f"No valid '0' class lines in {label_file}, skipping file.")
        else:
            print(f"Label file not found for {image_file}")
