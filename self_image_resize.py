import os
import cv2

# Define the input and output directories
input_dir = ""
output_dir = ""

# Loop over all the files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        # Load the image
        img = cv2.imread(os.path.join(input_dir, filename))

        # Resize the image to a new width and height
        new_width = 640
        new_height = 194
        resized_img = cv2.resize(img, (new_width, new_height))

        # Save the resized image to disk
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.png')
        cv2.imwrite(output_path, resized_img)


