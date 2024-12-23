"""
This code is to visualize the bounding boxes coordinates from kitti dataset on the images.

please change the paths if required
"""

# Import necessary libraries
import numpy as np
import cv2

# Load the first five images in your dataset
for i in range(5):
    # Set directory path to the i-th image
    dir = "Training\\images\\"
    dir = dir+str(i).zfill(6)+".png"

    # Load the image using OpenCV
    img = cv2.imread(dir)

    # Get image dimensions
    h, w, _ = img.shape
    
    # Load the corresponding annotation file in YOLO format
    annotation_path = f"Training/labels/"
    annotation_path = annotation_path+str(i).zfill(6)+".txt"
    with open(annotation_path, 'r') as f:
        lines = f.readlines()
    
    # Draw bounding boxes on the image
    for line in lines:
        # Extract class_id and coordinates from the annotation file
        class_id, x_min, y_min, x_max, y_max = [float(x) for x in line.split()]
        
        # Scale the coordinates to match image dimensions
        x_min = x_min * w
        y_min = y_min * h
        x_max = x_max * w
        y_max = y_max * h
        
        # Draw bounding box on the image
        cv2.rectangle(img, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
    
    # Display the image with bounding boxes
    cv2.imshow("Image with Bounding Boxes", img)
    cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

