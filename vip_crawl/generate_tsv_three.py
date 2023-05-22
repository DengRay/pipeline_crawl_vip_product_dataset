import os
import csv
import base64
from io import BytesIO
from PIL import Image

def merge_pic(di_1,save_path_):
    with open(di_1, 'r', encoding='utf-8') as f_r,open(save_path_, 'a', newline='') as f_w:
        reader = csv.reader(f_r, delimiter='\t')
        #lines = f_r.readlines()
        writer = csv.writer(f_w, delimiter='\t',quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            temp_ = row[0] + "\t" + row[1]
            rows = [temp_.split('\t')]
            writer.writerows(rows)
        print(f"{di_1} done")

def check_pic(path):
    id_l = []
    with open(path,'r',encoding='utf-8') as f:
        reader = csv.reader(f,delimiter="\t")
        for row in reader:
            if row[0] in id_l:
                print(f"the path {path} has repetitive picture the the picture id is {row[0]}")
            id_l.append(row[0])
            pic_temp = row[1]
            try:
                img = Image.open(BytesIO(base64.urlsafe_b64decode(pic_temp)))
                img.save(f"/home/dengyiru/vip_crwal/new_id/temp.jpg", "JPEG", quality=95)
            except:
                print(f"the {path}picture {row[0]} is damaged")


folder_path = "/home/dengyiru/vip_crwal/new_picture"
#di_1 = "/home/dengyiru/Chinese-CLIP-master/data_path/datasets/farfetch/train_imgs.tsv"
save_path_ = '/home/dengyiru/icut/all_clean_done/5_12_test.tsv'

for root,dirs,files in os.walk(folder_path):
    for filename in files:
        if filename.endswith("tsv"):
            file_path = os.path.join(root,filename)
            #check_pic(file_path)
            merge_pic(file_path,save_path_)

            