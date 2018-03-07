import sys
import cv2
import numpy as np
from xml.etree.ElementTree import parse
from PIL import Image

tree = parse("train.xml")
root = tree.getroot()
num_images = len(root)

with open('image_path_list.txt', 'w') as image_path_list, open('label_list.txt','w') as label_list:
    for child in root:
        image_path = child[0].text
        number_of_text = len(child.find('taggedRectangles'))

        for i in range(number_of_text):
            height = int(child.find('taggedRectangles')[i].get('height'))
            width = int(child.find('taggedRectangles')[i].get('width'))
            x = int(child.find('taggedRectangles')[i].get('x'))
            y = int(child.find('taggedRectangles')[i].get('y'))

            img = Image.open(image_path)
            cropped_image = img.crop((x, y, x+width, y+height))
            cropped_image_path = 'cropped_'+image_path.split('.')[0]+'_%d.jpg' % i
            cropped_image.save(cropped_image_path)

            label = child.find('taggedRectangles')[i][0].text

            image_path_list.write(cropped_image_path + '\n')
            label_list.write(label +'\n')
