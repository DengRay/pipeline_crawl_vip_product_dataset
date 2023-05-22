import requests
import json
import os
import base64
from io import BytesIO
from PIL import Image
import csv
import argparse
import math
import multiprocessing



def download_pic(data_path,save_path):
    data_path_json = data_path
    save_path_tsv = save_path
    had_read = [] 
    
    with open (save_path_tsv, 'r', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            had_read.append(line[0])
    #print(had_read)
    
    with open(data_path_json,'r',encoding='utf-8') as f_r,open(save_path_tsv, 'a', newline='') as f_w:
        #data = json.load(f_r)
        writer = csv.writer(f_w, delimiter='\t',quoting=csv.QUOTE_MINIMAL)
        #print(data)
        for line in f_r:
            try:
                data = json.loads(line)
                temp = data["productId"]
                if temp not in had_read:
                    #for item in data["image"]:
                    #save_path = save_path_tsv + "temp{}.jpg".format(arg.tag_number)
                    assert isinstance(data["image"], list) and data["image"], f"The value of image is not an empty list."
                    item = data["image"][0]
                    response = requests.get(item["imageUrl"])
                    image = Image.open(BytesIO(response.content))
                    resized_image = image.resize((224, 224), resample=Image.BICUBIC)
                    #print(image.format)
                    #print(resized_image.format)
                    img_buffer = BytesIO()
                    resized_image.save(img_buffer,format='JPEG')
                    byte_data = img_buffer.getvalue()
                    base64_str = base64.b64encode(byte_data)
                    s = "{}".format(base64_str)
                    temp_ = temp + "\t" + s[2:-1]
                    rows = [temp_.split('\t')]
                    writer.writerows(rows)
                    #resized_image.save(save_path)
            except AssertionError as e:
                print(f"AssertionError: {e}")
            except:
                print("download error")
                continue

def get_file_args():
    with open("/home/dengyiru/vip_crwal/up10000.json",'r',encoding='utf-8') as f_id:
        data = json.load(f_id)
        file_args = []
        for i,item in enumerate(data):
            ex_filename = "{}_{}".format(i,item[1])
            file_args.append(ex_filename)
        return file_args
        #print(file_args)
        #print(i,item[1])

#def run():
def run(arg):
    source_path = f"/home/dengyiru/vip_crwal/new_content/{arg}.json"
    save_path = f"/home/dengyiru/vip_crwal/new_picture/{arg}.tsv"
    #source_path = "/home/dengyiru/vip_crwal/new_id/temp2.json"
    #save_path = "/home/dengyiru/vip_crwal/new_id/temp2.tsv"
    download_pic(source_path,save_path)


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=14)
    arg = get_file_args()
    #args = arg[:37]
    args = ["70_52156143","21_53986306","71_52179333","12_55515022","65_52044557","40_61547254","16_54886016","61_52044471","68_52179354","47_52040688","60_52044474","3_53986308","30_53986312","53_52044454"]
    #args = arg[37:]
    #args = [arg[10]]
    #print(args)
    pool.map(run, args) 
    #run()