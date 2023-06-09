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



def download_pic(data_path,save_dir):
    data_path_json = data_path
    #save_path_tsv = save_path
    had_read = [] 
    ''''
    with open (save_path_tsv, 'r', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            had_read.append(line[0])
    #print(had_read)
    '''
    with open(data_path_json,'r',encoding='utf-8') as f_r:
        #data = json.load(f_r)
        #writer = csv.writer(f_w, delimiter='\t',quoting=csv.QUOTE_MINIMAL)
        #print(data)
        for line in f_r:
            #print(line)
            data = json.loads(line)
            temp = data["productId"]
            #print(temp)
            save_path = os.path.join(save_dir,temp)
            #print(save_path)
            if os.path.exists(save_path):
                continue
                #print(f"The path {save_path} exists.")
            else:
                os.makedirs(save_path, exist_ok=True)
                #print("1")
            #for item in data["image"]:
            #save_path = save_path_tsv + "temp{}.jpg".format(arg.tag_number)
                try:
                    if "shortVideoUrl" in data:
                        video_url = data["shortVideoUrl"]
                        #print()
                        try:
                            response = requests.get(video_url, stream=True)
                            # 确保请求成功
                            if response.status_code == 200:
                            # 注意修改为你希望存储文件的路径和文件名
                                t  = 'video.mp4'
                                save_pt = os.path.join(save_path,t)
                                with open(save_pt, 'wb') as file:
                                    for chunk in response.iter_content(chunk_size=1024):
                                        if chunk:
                                            file.write(chunk)
                            else:
                                print("请求失败，状态码：", response.status_code)
                        except:
                            print("video download fail!")
                    #print(data["previewImages_image"])
                    #print(len(data["previewImages_image"]))
                    #assert isinstance(data["image"], list) and data["image"], f"The value of image is not an empty list."
                    for i in range(len(data["previewImages_image"])):
                        item = data["previewImages_image"][i]
                        #print(item["imageUrl"])
                        response = requests.get(item["imageUrl"])
                        tt = f"p{i}.jpg"
                        save_p = os.path.join(save_path,tt)
                        with open(save_p, 'wb') as file:
                            file.write(response.content)
                    for i in range(len(data["detailImages_image"])):
                        item = data["detailImages_image"][i]
                        response = requests.get(item["imageUrl"])
                        tt = f"d{i}.jpg"
                        save_p = os.path.join(save_path,tt)
                        with open(save_p, 'wb') as file:
                            file.write(response.content)
                except:
                    print("download error")
                    continue
                

def get_file_args():
    with open("/home/dengyiru/vip_crwal/cate_shoe.json",'r',encoding='utf-8') as f_id:
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
    root_path = "/home/dengyiru/vip_crwal/shoe_dataset/"
    next_path = root_path + f"{arg}"
    os.makedirs(next_path, exist_ok=True)
    source_path = f"/home/dengyiru/vip_crwal/new_content_test/{arg}.json"
    save_dir = next_path
    #save_path = f"/home/dengyiru/vip_crwal/new_picture/{arg}.tsv"
    #source_path = "/home/dengyiru/vip_crwal/new_id/temp2.json"
    #save_path = "/home/dengyiru/vip_crwal/new_id/temp2.tsv"
    download_pic(source_path,save_dir)


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=25)
    arg = get_file_args()
    #print(arg)
    args = arg[:25]
    #print(args)
    #args = ["70_52156143","21_53986306","71_52179333","12_55515022","65_52044557","40_61547254","16_54886016","61_52044471","68_52179354","47_52040688","60_52044474","3_53986308","30_53986312","53_52044454"]
    #args = arg[25:]
    #args = [arg[10]]
    #print(args)
    pool.map(run, args) 
    #run()