
*step-1 : 
    - open "op.py" file and replace the image_folder &        label_folder path. in this case i have used the coco_dataset

    - update the destination_image_folder & destination_label_folder path which actually where you want to place the datasets

*step-2:
    - open "file_merge.py" file and replace the source_folder with val_image

    - basically this file copy all the images and labels from the source_folder and then paste them into the destination. And we do this just combine all the images and labels into a single folder.

*step-3:
    - in "test.ipynb" notebook file at first replace the image_folder & label_folder path and then check_label function

    - here we just check, is there any label.txt file exists which is start class:1 or anyother except class:0, 
    make sure that the main purpose of this task is seperated the human class which is class:0

*step-4:
    - in "train_val.py" file just replace the image_folder & label_folder which is our training dataset folder path

    - then update the train_image_folder, train_label_folder, val_image_folder and val_label_folder path where you wan to place train & val data which is split into 80% for training data and left 20% for validation data




Necessary Links: 
    - COCO_detection_dataset from kaggle
      https://www.kaggle.com/datasets/jeffaudi/coco-2014-dataset-for-yolov3

      