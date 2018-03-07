import sys
import cv2
import numpy as np
from xml.etree.ElementTree import parse
from PIL import Image
from shutil import copyfile
import re


image_count = 0
with open('all_image_path_list.txt', 'w') as all_image_path_list, open('all_label_list.txt','w') as all_label_list:

    #IC03
    from xml.etree.ElementTree import parse
    tree = parse("../IC03/word.xml")
    root = tree.getroot()
    num_images = len(root)

    for child in root:
        image_path = child.attrib['file']
        label = child.attrib['tag']

        if not re.search('[^a-zA-Z0-9]', label) and len(list(label)) >= 3:
            all_image_path = 'all_images/%d.jpg' % image_count
            copyfile('../IC03/'+image_path, all_image_path)
            all_image_path_list.write(all_image_path + '\n')
            all_label_list.write(label +'\n')
            image_count += 1
    print(image_count)

    #IC13
    with open('../IC13/image_path_list.txt','r') as IC13_Image, open('../IC13/label_list.txt','r') as IC13_label:
        image_list = IC13_Image.readlines()
        label_list = IC13_label.readlines()
        for image_path, label in zip(image_list, label_list):
            image_path = image_path.strip()
            label = label.strip()

            if not re.search('[^a-zA-Z0-9]', label) and len(list(label)) >= 3:

                all_image_path = 'all_images/%d.jpg' % image_count
                copyfile('../IC13/'+image_path, all_image_path)
                all_image_path_list.write(all_image_path + '\n')
                all_label_list.write(label +'\n')
                image_count += 1
    print(image_count)

    #IC15
    with open('../IC15/gt.txt','rb') as IC15:
        data = IC15.readlines()
        for line in data:
            image_path, label = line.decode("utf-8").strip().split(', ')
            label = label.strip('"')

            if not re.search('[^a-zA-Z0-9]', label) and len(list(label)) >= 3:
                all_image_path = 'all_images/%d.jpg' % image_count
                copyfile('../IC15/'+image_path, all_image_path)
                all_image_path_list.write(all_image_path + '\n')
                all_label_list.write(label +'\n')
                image_count += 1
    print(image_count)

    #IIIT5K
    with open('../IIIT5K/IIIT5K_train_label.txt','r') as IIIT5K:
        data = IIIT5K.readlines()
        for line in data:
            image_path, label = line.split('\t')
            label = label.strip()

            if not re.search('[^a-zA-Z0-9]', label) and len(list(label)) >= 3:
                all_image_path = 'all_images/%d.jpg' % image_count
                copyfile('../IIIT5K/'+image_path, all_image_path)
                all_image_path_list.write(all_image_path + '\n')
                all_label_list.write(label +'\n')
                image_count += 1
    print(image_count)

    #SVT
    with open('../SVT/image_path_list.txt','r') as SVT_Image, open('../SVT/label_list.txt','r') as SVT_label:
        image_list = SVT_Image.readlines()
        label_list = SVT_label.readlines()
        for image_path, label in zip(image_list, label_list):
            image_path = image_path.strip()
            label = label.strip()

            if not re.search('[^a-zA-Z0-9]', label) and len(list(label)) >= 3:
                all_image_path = 'all_images/%d.jpg' % image_count
                copyfile('../SVT/'+image_path, all_image_path)
                all_image_path_list.write(all_image_path + '\n')
                all_label_list.write(label +'\n')
                image_count += 1
    print(image_count)
