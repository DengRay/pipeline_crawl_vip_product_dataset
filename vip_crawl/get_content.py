import requests
import json
import math
import multiprocessing
import os

def get_useful_ifo(pro_id,save_path):
    url = "https://mapi.vip.com/vips-mobile/rest/shopping/pc/detail/main/v6"
    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": "OAuth api_sign=571958a04acf6d489ffc92463a40ac8f3945acf2",
        "Origin": "https://detail.vip.com",
        "Referer": "https://detail.vip.com/",
        "x-requested-with": "XMLHttpRequest"
    }
    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": "OAuth api_sign=184f43a07279370085b3b3eddca1db5a6f70d1a4",
        "Origin": "https://detail.vip.com",
        "Referer": "https://detail.vip.com/",
        "x-requested-with": "XMLHttpRequest"
    }

    payload = {
        "app_name": "shop_pc",
        "app_version": "4.0",
        "warehouse": "VIP_BJ",
        "fdc_area_id": "101101101",
        "client": "pc",
        "mobile_platform": "1",
        "province_id": "101101",
        "api_key": "70f71280d5d547b2a7bb370a529aeea1",
        "user_id": "",
        "mars_cid": "1680577576776_664414ba2ad18014bf115f032e8fa34c",
        "wap_consumer": "a",
        "scene": "detail",
        "productId": f"{pro_id}",
        "opts": "priceView:13;quotaInfo:1;restrictTips:1;panelView:3;foreShowActive:1;invisible:1;floatingView:1;announcement:1;svipView:2;showSingleColor:1;svipPriceMode:1;promotionTips:6;foldTips:3;formula:2;extraDetailImages:1;shortVideo:1;countryFlagStyle:1;saleServiceList:1;storeInfo:1;brandCountry:1;freightTips:3;priceBannerView:1;bannerTagsView:1;buyMoreFormula:1;kf:1;relatedProdSpu:1",
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
    except:
        print("bug")
    if response.status_code == 200:
        # 在这里处理响应数据
        data_raw = {}
        url_raw = []
        url = {}
        s = ""
        response_json = response.json()
        res_json = response_json["data"]
        data_raw["productId"] = res_json["productId"]
        #print(res_json)
        temp0 = res_json["productId"]
        temp1 = res_json["base"]["title"] #修改，没有加入名称，temp1代表name
        data_raw["name"] = temp1
        temp2 = res_json['props']
        #temp3 = res_json['products'][f"{pro_id}"]["priceView"]["finalPrice"]["price"]
        #data_raw["price"] = temp3
        #print(temp0)
        #print(temp1)
        for items in temp2:
            #print(items['name'],items['value'])
            if items['name'][0] == "生" or items['name'][0] == "上":
                break
            else:
                if items['name'][0] != "详" and items['name'][0]!="面" and items['name'][0]!="选":
                    s = s + items['value'] + " "
        data_raw["description"] = s
        try:
            if f"{pro_id}" in res_json['images']['groups']:
                temp3 = res_json['images']['groups'][f"{pro_id}"]['previewImages']
                if len(temp3) >= 3:
                    for i in range(3):
                        #print(temp3[i]["imageUrl"])
                        url["imageUrl"] = temp3[i]["imageUrl"]
                        url_raw.append(url.copy())
                else:
                    url["imageUrl"] = temp3[0]["imageUrl"]
                    url_raw.append(url.copy())
            else:
                temp3 = res_json['images']['groups']['spu']['previewImages']
                if len(temp3) >= 3:
                    for i in range(3):
                        #print(temp3[i]["imageUrl"])
                        url["imageUrl"] = temp3[i]["imageUrl"]
                        url_raw.append(url.copy())
                else:
                    url["imageUrl"] = temp3[0]["imageUrl"]
                    url_raw.append(url.copy())
        except:
            print("image bug")
        data_raw["image"] = url_raw
        #写入json
        with open(save_path, "a",encoding='utf-8') as f:
            json.dump(data_raw, f,ensure_ascii=False)
            f.write("\n")

    else:
        print(f"请求失败，状态码：{response.status_code}")
    #except:
    #    print("bug")

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
    source_path = f"/home/dengyiru/vip_crwal/id_new/{arg}.json"
    save_path = f"/home/dengyiru/vip_crwal/new_content/{arg}.json"
    #source_path = f"/home/dengyiru/vip_crwal/id_new/10_61971038.json"
    #save_path = f"/home/dengyiru/vip_crwal/new_content/10_61971038.json"
    with open(save_path, 'r', encoding='utf-8') as file:
        had_done = []
        for line in file:
            data = json.loads(line)
            #print(items)
            #print(type(items))
            had_done.append(data["productId"])

    with open(source_path,'r',encoding='utf-8') as f:
        pro_id = json.load(f)
        #save_path = "/home/dengyiru/vip_crwal/new_id/temp2.json"
        for item in pro_id:
            if item not in had_done:
                get_useful_ifo(item,save_path)

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=37)
    arg = get_file_args()
    #args = arg[:37]
    args = arg[37:]
    #args = [arg[10]]
    #print(args)
    pool.map(run, args) 
    #run()