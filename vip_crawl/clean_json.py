
import os
def clean_lines_in_json(file_path,new_folder_path):
    with open(file_path,'r',encoding='utf-8') as f_r,open(new_folder_path,'w',encoding='utf-8') as f_w:
        lines = f_r.readlines()
        #print(type(lines))
        #print(len(lines))
        lines_ = list(set(lines))
        #print(len(lines_))
        #print("done")
        with open(new_folder_path,'w',encoding='utf-8') as f_w:
            for lin in lines_:
                f_w.write(lin)
        #for line in lines:
        #    id = line["productId"]

def main(folder_path,new_folder_path):
    for root,dirs,files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".json"):
                file_path = os.path.join(root,file_name)
                new_path = os.path.join(new_folder_path,file_name)
            clean_lines_in_json(file_path,new_path)




if __name__ == '__main__':
    folder_path = "/home/dengyiru/vip_crwal/jsonl"
    new_folder_path = '/home/dengyiru/vip_crwal/clean_json'
    main(folder_path,new_folder_path)