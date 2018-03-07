import sys

with open(sys.argv[1], 'r') as label, open('lexicon.txt', 'r') as lexicon, open('image_path_list.txt', 'w') as image_path_list, open('label_list.txt','w') as label_list:
    labelset = label.readlines()
    lexicon_list = lexicon.readlines()
    for sample in labelset:
        image_path, index = sample.strip('\n').split()
        label = lexicon_list[int(index)].strip('\n')
        image_path_list.write(image_path + '\n')
        label_list.write(label +'\n')
