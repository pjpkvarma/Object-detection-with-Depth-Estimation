# importing required packages
import numpy as np
import os
print(os.getcwd())

#labels folder path
label_files = ""

def convert_kitti_to_yolo(label_file, img_width, img_height):
    classes = ['Car', 'Pedestrian', 'Cyclist', 'Truck', "Van", "Tram", "Person_sitting", "Misc"]
    with open(label_file) as f:
        lines = f.readlines()
    annotations = []
    for line in lines:
        data = line.strip().split(' ')
        
        # don't cares are neglected
        if data[0] == 'DontCare':
            continue
        
        # storing index of classes
        class_id = classes.index(data[0])
        
        # getting xcenter, ycenter, height and width from lables files
        x_center = float(data[4]) * img_width
        y_center = float(data[5]) * img_height
        w = float(data[6]) * img_width
        h = float(data[7]) * img_height
        x_min = x_center - w/2
        y_min = y_center - h/2
        x_max = x_center + w/2
        y_max = y_center + h/2
        # x_min = float(data[4])
        # y_min = float(data[5])
        # x_max = float(data[6])
        # y_max = float(data[7])
        annotation = (class_id, x_min, y_min, x_max, y_max)
        print(annotation)
        annotations.append(annotation)
        
    #output directory path
    out_dir = ""
    out_dir = out_dir+str(i).zfill(6)+".txt"
    
    # writing to output files
    with open(out_dir, 'w') as f:
        for annotation in annotations:
            class_id, x_min, y_min, x_max, y_max = annotation
            yolo_annotation = '{} {:.6f} {:.6f} {:.6f} {:.6f}'.format(
                class_id, x_min, y_min, x_max, y_max)
            f.write(yolo_annotation + '\n')
    
    #returnning all the labeles
    return np.array(annotations)

annotations=[]

for i in range(7481):
    dir = label_files+str(i).zfill(6)+".txt"
    annotation=convert_kitti_to_yolo(str(dir), 1224, 370)
    annotations.append(annotation)
    
