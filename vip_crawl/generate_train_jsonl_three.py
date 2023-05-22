import json
import csv
import os
#sourcedata = "/home/dengyiru/merge_outputs/1.json"
#image_path = "/home/dengyiru/icut/pic_dataset/test1.tsv"
#save_path = "/home/dengyiru/icut/all_clean_done/test.jsonl"



#for kk in range(74):
#jj = kk+1
def white_jsonl(save_path,sourcedata,image_path,totle,q):
    #sourcedata = source + "temp2.json"
    #image_path = image_p + "temp2.tsv"
    with open(sourcedata,'r',encoding='utf-8') as f_r1,open(image_path, 'r', newline='') as f_r2,open(save_path,mode = 'a',encoding="utf-8") as f_w:
        #r_1 = json.load(f_r1)
        #r_2 = csv.reader(f_r2,delimiter='\t')      
        
        image_id = []
        pair_dict = {}
        
        for row in f_r2:
            row = row.split('\t')
            image_id.append(row[0])
        #print(image_id)
        #print(len(image_id))
        for line in f_r1:
            data = json.loads(line)
            pro_id = data["productId"]
            if pro_id in image_id:
                q += 1
                #pr_text = data["description"]
                pair_dict["query_id"] = totle + q
                pair_dict["query_text"] = data["name"]+data["description"]
                pair_dict["item_ids"] = [int(pro_id)]
                #print(pair_dict)
                json.dump(pair_dict, f_w,ensure_ascii=False)
                f_w.write('\n')
            '''
            if "description" in line:
                q += 1
                pr_text = line["description"]
                pair_dict["query_id"] = totle+q
                pair_dict["query_text"] = pr_text
                pair_dict["item_ids"] = [int(pro_id)]
                #print(pair_dict)
                json.dump(pair_dict, f_w,ensure_ascii=False)
                f_w.write('\n')
            '''
        totle = totle + q
    return totle

source = "/home/dengyiru/vip_crwal/new_id/"
image_p = "/home/dengyiru/vip_crwal/new_id/"
save_path = "/home/dengyiru/icut/all_clean_done/5_12_done.jsonl"


totle = 0 #修改
q = 0

folder_path = "/home/dengyiru/vip_crwal/new_content"
folder_path_2 = "/home/dengyiru/vip_crwal/new_picture"

for root,dirs,files in os.walk(folder_path):
    for filename in files:
        if filename.endswith("json"):
            file_path_1 = os.path.join(root,filename)
            file_prefix, file_suffix = os.path.splitext(filename)
            file_path_2 = folder_path_2 + "/" + file_prefix + ".tsv"
            totle = white_jsonl(save_path,file_path_1,file_path_2,totle,q)
            print(f"{file_path_2} done!")
            