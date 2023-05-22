import os
import json
def count_lines_in_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        return len(data)

def count_lines_in_json_2(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return len(data)

def main(folder_path,new_path):
    total_lines = 0
    count = 0
    for root, dirs, files in sorted(os.walk(folder_path)):
        for file_name in files:
            if file_name.endswith('.json'):
            #if file_name.endswith('.tsv'):
                file_path = os.path.join(root, file_name)
                #new_ = os.path.join(new_path,file_name)
                #new_ = new_path
                #if os.path.exists(new_):
                #    count +=1
                #print(file_name)
                lines_in_file = count_lines_in_json_2(file_path)
                #print("{}:{}".format(file_name,lines_in_file))
                total_lines += lines_in_file
                count +=1
                #print(f"File: {file_name} - Lines: {lines_in_file}")
    print(f"Total lines in all JSON files: {total_lines}")
    print(count)
    return total_lines

if __name__ == '__main__':
    folder_path1 = '/home/dengyiru/vip_crwal/id_new'  # 更改为你的文件夹路径 171 42 27 19
    #folder_path1 = '/home/dengyiru/vip_crwal/new_content'  # 更改为你的文件夹路径 171 42 27 19
    #folder_path1 = '/home/dengyiru/vip_crwal/new_picture'  # 更改为你的文件夹路径 171 42 27 19
    #folder_path1 = '/home/dengyiru/vip_crwal/new_picture'
    #folder_path2 = '/home/dengyiru/vip_crwal/json'
    #folder_path3 = '/home/dengyiru/vip_crwal/jso'
    #folder_path4 = '/home/dengyiru/vip_crwal/js'
    new_path = '/home/dengyiru/vip_crwal/jso'
    a = main(folder_path1,new_path)
    #file_path = "/home/dengyiru/icut/all_clean_done/5_12_done.jsonl"
    #le = count_lines_in_json(file_path)
    #print(le)
