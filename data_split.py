"""
please change the paths of the folder to run this code

this code is to split the dataset into train and test splits
"""

import os
import random
from shutil import copyfile

def split_data(source, label, training, validation, training_l, validation_l, split_ratio):
    # create an empty list to store valid files
    files = []
    # loop through all files in the source directory
    for filename in os.listdir(source):
        # get the full file path
        file_path = source + filename
        # check if the file is not empty
        if os.path.getsize(file_path) > 0:
            # if the file is not empty, add it to the list of valid files
            files.append(filename)
        else:
            # if the file is empty, print a message to the console
            print(f'Invalid file: {filename}')
    # calculate the number of files to be used for training and validation based on the split ratio
    training_length = int(len(files) * split_ratio)
    validation_length = len(files) - training_length
    # randomly shuffle the list of files
    shuffled_set = random.sample(files, len(files))
    # create two separate sets of files: one for training and one for validation
    training_set = shuffled_set[0:training_length]
    validation_set = shuffled_set[training_length:]

    # loop through each file in the training set
    for filename in training_set:
        # get the full file path for both the image and its corresponding label
        this_file = source + filename
        this_file_label = label + filename[:-4] + '.txt'
        # define the destination path for the image and its corresponding label in the training set
        destination = training + filename
        destination_label = training_l + filename[:-4] + '.txt'
        # copy the image and its corresponding label to their respective destination folders
        copyfile(this_file, destination)
        copyfile(this_file_label, destination_label)
    # loop through each file in the validation set
    for filename in validation_set:
        # get the full file path for both the image and its corresponding label
        this_file = source + filename
        this_file_label = label + filename[:-4] + '.txt'
        # define the destination path for the image and its corresponding label in the validation set
        destination = validation + filename
        destination_label = validation_l + filename[:-4] + '.txt'
        # copy the image and its corresponding label to their respective destination folders
        copyfile(this_file, destination)
        copyfile(this_file_label, destination_label)

# define the source and destination paths, and the split ratio
img_source = ""
label_source = ""
training_images = ''
validation_images = ''
training_labels = ''
validation_labels = ''
split_ratio = 0.8

# call the function to split the data into training and validation sets
split_data(img_source, label_source, training_images, validation_images, training_labels, validation_labels, split_ratio)

