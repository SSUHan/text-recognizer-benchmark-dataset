import pickle
import os.path as osp
import os

target_dir = 'test_data/SVT-Perspective'
gt_txt_name = 'gt'
out_pkl_name = 'svt_perspective_all'

with open(osp.join(target_dir, "{}.txt".format(gt_txt_name)), 'r') as fp:
	data = fp.readlines()
print("data len : {}".format(len(data)))
dic = {}

for each_line in data:
	each_line = each_line.replace('\n', '')
	each_line = each_line.strip()
	path, text = each_line.split(' ')
	dic[path] = text

print("len(dic) : {}".format(len(dic.keys())))
with open(osp.join(target_dir, "{}.pkl".format(out_pkl_name)), 'wb') as fp:
	pickle.dump(dic, file=fp, protocol=2)
