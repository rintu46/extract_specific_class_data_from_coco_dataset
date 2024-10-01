import os

# Define your image and label directories
image_folder = '/home/Documents/archive (1)/person_class/data_2014/images'
label_folder = '/home/Documents/archive (1)/person_class/data_2014/labels'

# Get a list of all image files in the image folder
for image_file in os.listdir(image_folder):
    if image_file.endswith(('.jpg', '.jpeg', '.png')):  # Consider image extensions
        # Construct full path for corresponding label
        label_file = image_file.replace(image_file.split('.')[-1], 'txt')  # Assuming the label files are in .txt
        label_path = os.path.join(label_folder, label_file)
        
        # Check if the label file exists
        if os.path.exists(label_path):
            with open(label_path, 'r') as label:
                lines = label.readlines()
                
            # Check if any line in the label file has a first index other than 0
            found_non_zero = False
            for line in lines:
                if line.strip() and line[0] != '0':
                    found_non_zero = True
                    break
            
            # If any line does not start with 0, print the file name
            if found_non_zero:
                print(f"Label file {label_file} contains a line starting with a value other than 0.")
        else:
            print(f"Label file not found for {image_file}")
