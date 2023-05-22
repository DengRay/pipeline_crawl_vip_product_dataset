import json

record =[]
dict = {}
all_dict = []
q_id = 500000

with open("/home/dengyiru/icut/all_clean_done/prevalid_queries.jsonl",'r',encoding='utf-8') as f_r,open("//home/dengyiru/icut/all_clean_done/valid_queries.jsonl","w",encoding="utf-8") as f_w:
    
    for line in f_r:
        data = json.loads(line)
        text = data["query_text"]
        item = data["item_ids"]
        if text in record: 
            idx = record.index(text)
            temp = all_dict[idx]
            #print(type(temp))
            temp["item_ids"].append(item[0])
            all_dict[idx] = temp
            #print("!!!")
        else:
            dict["query_id"] = q_id
            dict["query_text"] = text
            dict["item_ids"] = item
            #print(dict)
            q_id += 1
            all_dict.append(dict.copy())
            record.append(text)
            #print(all_dict)
    #print(record)
    #print(all_dict)
    for i in all_dict:
        json.dump(i, f_w,ensure_ascii=False)
        f_w.write('\n')
        