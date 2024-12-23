"""
please change the paths of the folder to run this code

This code is to augment the images 
blurring
night effect
noise effect
rain effect
"""

import os
import cv2
import random
import numpy as np

# input_folder = "validation\\images\\"
input_folder = "resized_test\\"
# output_folder = "modified_validation"
output_folder = "augmented_images\\"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(input_folder)
image_files = [file for file in files if file.endswith(('png', 'jpg', 'jpeg'))]

for file in image_files:
    image_path = os.path.join(input_folder, file)
    img = cv2.imread(image_path)

    # Randomly select whether to modify the image or not
    modify_image = random.choice([True, False])

    # If modifying the image
    if modify_image:
        # Randomly select a modification to apply
        modification = random.choice(['blur', 'night', 'noise', 'rain'])

        # If doing blurring
        if modification == 'blur':
            # Randomly select a blurring kernel size
            kernel_size = random.choice([3, 5, 7, 9])
            blurred_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

            # Save the modified image
            output_path = os.path.join(output_folder, file)
            cv2.imwrite(output_path, blurred_img)

        # If doing night effect
        elif modification == 'night':
            # Convert the image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply gamma correction to darken the image
            gamma = 3
            gray = np.power(gray/255.0, gamma) * 255.0
            gray = gray.astype(np.uint8)

            # Apply contrast and brightness adjustments to simulate a night effect
            alpha = 1.2 # Contrast control (1.0-3.0)
            beta = 50 # Brightness control (0-100)
            night_img = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)

            # Save the modified image
            output_path = os.path.join(output_folder, file)
            cv2.imwrite(output_path, night_img)

        # If doing salt and pepper noise
        elif modification == 'noise':
            # Randomly select a noise percentage
            noise_percentage = random.choice([0.01, 0.02, 0.03, 0.04, 0.05])
            noise_img = img.copy()

            # Add salt and pepper noise to the image
            height, width, _ = img.shape
            noise_pixels = int(height * width * noise_percentage)
            for i in range(noise_pixels):
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                noise_img[y, x] = (255, 255, 255) if random.randint(0, 1) else (0, 0, 0)

            # Save the modified image
            output_path = os.path.join(output_folder, file)
            cv2.imwrite(output_path, noise_img)
        # If doing rain effect
        elif modification == 'rain':
            # Generate a rain effect by adding random white lines to the image
            height, width, _ = img.shape
            rain_img = img.copy()
            for i in range(500):
                x1 = random.randint(0, width)
                y1 = random.randint(0, height)
                x2 = x1 + random.randint(1, 5)
                y2 = y1 + random.randint(5, 25)
                cv2.line(rain_img, (x1, y1), (x2, y2), (255, 255, 255, 128), 1)

                # Check that the line coordinates are within the image bounds
                x1 = max(0, min(x1, width-1))
                y1 = max(0, min(y1, height-1))
                x2 = max(0, min(x2, width-1))
                y2 = max(0, min(y2, height-1))

                # Apply Gaussian blur to the line region
                line_roi = rain_img[min(y1,y2):max(y1,y2), min(x1,x2):max(x1,x2)]
                if line_roi.size != 0:
                    line_roi = cv2.GaussianBlur(line_roi, (3, 3), 0)
                    rain_img[min(y1,y2):max(y1,y2), min(x1,x2):max(x1,x2)] = line_roi

            # Save the modified image
            output_path = os.path.join(output_folder, file)
            cv2.imwrite(output_path, rain_img)



    # If not modifying the image, just copy it to the output folder
    else:
        output_path = os.path.join(output_folder, file)
        cv2.imwrite(output_path, img)
