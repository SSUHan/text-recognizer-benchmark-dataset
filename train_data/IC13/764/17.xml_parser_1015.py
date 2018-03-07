import sys
import re

cnt = 0
with open(sys.argv[1], 'r') as dataset, open('image_path_list.txt', 'w') as image_path_list, open('label_list.txt','w') as label_list:
    samples = dataset.readlines()
    for sample in samples:
        image_path, label = sample.strip('\n').split(', ')
        label = label.strip('"')
        if not re.search('[^a-zA-Z0-9]', label):
            cnt += 1
            image_path_list.write('./images/'+image_path + '\n')
            label_list.write(label +'\n')

    print('number of samples :',cnt)
