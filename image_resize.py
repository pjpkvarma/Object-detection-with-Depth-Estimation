import cv2
import os

train_dir = ""
val_dir= "
# Define the new size of the images

new_width = 640
new_height = 194
# Loop over the images and labels
for img_file in os.listdir(os.path.join(train_dir, 'images')):
    # Load the image
    img_path = os.path.join(train_dir, 'images', img_file)
    img = cv2.imread(img_path)

    # Resize the image
    resized_img = cv2.resize(img, (new_width, new_height))

    # Save the resized image
    cv2.imwrite(img_path, resized_img)

    # Load the corresponding label file
    label_path = os.path.join(train_dir, 'labels', img_file.replace('.png', '.txt').replace('.jpg', '.txt'))
    with open(label_path, 'r') as f:
        labels = f.read().splitlines()

    # Loop over the labels and update the bounding box coordinates
    for i, label in enumerate(labels):
        label_parts = label.split()
        x1, y1, x2, y2 = map(float, label_parts[1:])
        # x_scale = new_width / img.shape[1]
        # y_scale = new_height / img.shape[0]
        new_x = ((x1 + x2) / 2)/img.shape[1]
        new_y = ((y1 + y2) / 2)/img.shape[0]
        new_w = (x2 - x1) / img.shape[1]
        new_h = (y2 - y1) / img.shape[0]
        labels[i] = f'{label_parts[0]} {new_x} {new_y} {new_w} {new_h}'

    # Save the updated label file
    with open(label_path, 'w') as f:
        f.write('\n'.join(labels))


# Loop over the images and labels
for img_file in os.listdir(os.path.join(val_dir, 'images')):
    # Load the image
    img_path = os.path.join(val_dir, 'images', img_file)
    img = cv2.imread(img_path)

    # Resize the image
    resized_img = cv2.resize(img, (new_width, new_height))

    # Save the resized image
    cv2.imwrite(img_path, resized_img)

    # Load the corresponding label file
    label_path = os.path.join(val_dir, 'labels', img_file.replace('.png', '.txt').replace('.jpg', '.txt'))
    with open(label_path, 'r') as f:
        labels = f.read().splitlines()

    # Loop over the labels and update the bounding box coordinates
    for i, label in enumerate(labels):
        label_parts = label.split()
        x1, y1, x2, y2 = map(float, label_parts[1:])
        # x_scale = new_width / img.shape[1]
        # y_scale = new_height / img.shape[0]
        new_x = ((x1 + x2) / 2)/img.shape[1]
        new_y = ((y1 + y2) / 2)/img.shape[0]
        new_w = (x2 - x1) / img.shape[1]
        new_h = (y2 - y1) / img.shape[0]
        labels[i] = f'{label_parts[0]} {new_x} {new_y} {new_w} {new_h}'

    # Save the updated label file
    with open(label_path, 'w') as f:
        f.write('\n'.join(labels))
