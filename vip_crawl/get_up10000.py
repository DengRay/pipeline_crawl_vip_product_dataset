import requests
import json
import math
import multiprocessing
import os
import time

def get_useful_id(urls,save_path,min,max):
    pro_id = []
    for num in range(0,(1)*120,120):  #这里是从第二页开始取数据了，第一个参数可以设置为0 最大页码即为12
        url = urls + f'&pageOffset={num}&salePlatform=1' + "&_=1682586618628"
        #+ f'&priceRange={min}-{max}' + "&_=1682586618628"
        try:
            html = requests.get(url,headers=headers_)
            start = html.text.index('{')
            end = html.text.index('})')+1
            json_data = json.loads(html.text[start:end])
            product_ids = json_data['data']['products']
            for product_id in product_ids:
                pro_id.append(product_id['pid'])
        except:
            print("bug")
    temp_ = list(set(pro_id))
    pro_id = temp_
    #print(len(pro_id))
    return pro_id

def get_totle(url):
    try:
        html = requests.get(url,headers=headers_)
        start = html.text.index('{')
        end = html.text.index('})')+1
        json_data = json.loads(html.text[start:end])
        product_num = json_data["data"]["total"]
    except:
        print("get_totle error!")
        return 0
    return product_num

def get_value_split(url):
    value_list = [1,100,150,200,250,300,400,500,600,800,1000,5000]
    #value_list = [1,5000]
    i = 0
    product_num = get_totle(url)
    if product_num > 1440:  #最大呈现页码的商品总数12*120
        while i <= (len(value_list)-2):
            url_new = url + f"&priceRange={value_list[i]}-{value_list[i+1]}"
            max = value_list[i+1]
            n = get_totle(url_new)
            if n > 1440: #列表需要更新，且最大呈现页码的商品总数12*120
                while True:
                    n = get_totle(url_new)
                    if max == (value_list[i]+1):
                        value_list.insert(i+1,math.ceil(middle))
                        break
                    if n > 1440: #最大呈现页码的商品总数12*120
                        middle = math.ceil((value_list[i]+max)/2)
                        url_new = url + f"&priceRange={value_list[i]}-{middle}"  
                        max = middle
                    else:
                        value_list.insert(i+1,math.ceil(middle))
                        #print(value_list)
                        break
            i = i+1
    #print("get value split done!total {} split!".format(len(value_list)))
    return value_list

def find_max_up():
    with open("/home/dengyiru/vip_crwal/pure_cate.json", "r",encoding='utf-8') as f_r,open("/home/dengyiru/vip_crwal/up30000.json", "w",encoding='utf-8') as f_w:
        data = json.load(f_r)
        s = []
        for item in data:
            cate = item[1]
            url = f"https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=101101101&client=pc&mobile_platform=1&province_id=101101&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1680593954989_25174b1c65e9de41c5467b61ab30affd&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId={cate}&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=0"
            num = get_totle(url)
            if num > 9999:
                s.append(item)
        json.dump(s,f_w,ensure_ascii=False)

def run(arg):
    with open("/home/dengyiru/vip_crwal/up10000.json", "r",encoding='utf-8') as f_r:
        data = json.load(f_r)
        all_id  = []
        a_id = []
        flag = 1
        item = data[arg]
        cate = item[1]
        save_path = f"/home/dengyiru/vip_crwal/id_new/{arg}_{cate}.json"
        url = f"https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=101101101&client=pc&mobile_platform=1&province_id=101101&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1680593954989_25174b1c65e9de41c5467b61ab30affd&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId={cate}&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=0"
        #url = f"https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=101101101&client=pc&mobile_platform=1&province_id=101101&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1680593954989_25174b1c65e9de41c5467b61ab30affd&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId={cate}&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=0&pageOffset=0&salePlatform=1&_=1682586618628"
        print("spliting price,please wait!")
        value_list = get_value_split(url)
        print("spliting price done!")
        print('get item id,please wait!')
        while(flag != len(a_id)):
            flag = len(a_id)
            #all_id = []
            #get_useful_id(url,save_path,0,0)
            #for i in range (len(value_list)-1):
            i = 0
            min = value_list[i]
            max = value_list[i+1]
            lis = get_useful_id(url,save_path,min,max)
            all_id.extend(lis)
            print(all_id)
            #print("the totle list is {}".format(len(all_id)))
            a_id = list(set(all_id))
            all_id = a_id
            with open(save_path,'r',encoding='utf-8') as f_r2:
                data_ = json.load(f_r2)
                for item in a_id:
                    if item not in data_:
                        data_.append(item) 
            with open(save_path,'w',encoding='utf-8') as f_w:
                json.dump(data_,f_w,ensure_ascii=False)
            print("the unique item in {} is {}".format(cate,len(a_id)))
            #time.sleep(120)

        return all_id
            
        
     
if __name__ == '__main__':
    headers_ = {
        'Cookie': 'vip_cps_cuid=CU1680577573878429d3b6748134397e; vip_cps_cid=1680577573880_1be6e615f0b136d5c68c9528973cbc8d; PAPVisitorId=7025c19292974aff36f0f40d24fdc4eb; vip_new_old_user=1; vip_city_name=%E5%B9%BF%E5%B7%9E%E5%B8%82; mars_cid=1680577576776_664414ba2ad18014bf115f032e8fa34c; mars_sid=d30d0d37f6bf0350d89f998b5767def2; mars_pid=0; PHPSESSID=dtqk8agrh3to6rgeqt4g2jf8h3; vip_address=%257B%2522pname%2522%253A%2522%255Cu5317%255Cu4eac%255Cu5e02%2522%252C%2522pid%2522%253A%2522101101%2522%252C%2522cname%2522%253A%2522%255Cu5e7f%255Cu5dde%255Cu5e02%2522%252C%2522cid%2522%253A%2522101101101%2522%257D; vip_province=101101; vip_province_name=%E5%8C%97%E4%BA%AC%E5%B8%82; vip_city_code=101101101; vip_wh=VIP_BJ; vip_ipver=31; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A1%7Cul%3A3105; VipDFT=0; cps_share=cps_share; mst_area_code=104104; cps=adp%3Antq8exyc%3A%40_%401681790112898%3Amig_code%3A4f6b50bf15bfa39639d85f5f1e15b10f%3Aac014miuvl0000b5sq8cvtz9ogmr2lld; user_class=a; vpc_uinfo=fr713%3A0%2Cfr1352%3A0%2Cfr674%3AD1%2Cfr1051%3A0%2Cfr766%3A0%2Cfr259%3AS0-4%2Cfr896%3A0%2Cfr0901%3A0%2Cfr884%3A0%2Cfr863%3A0%2Cfr392%3A310505%2Cfr398%3A0%2Cfr408%3A0%2Cfr251%3AA%2Cfr1195%3A0%2Cfr344%3A0%2Cfr444%3AA%2Cfr848%3A0%2Cfr1196%3A0%2Cfr249%3AA1%2Cfr328%3A3105%2Cfr902%3A0%2Cfr901%3A0%2Cfr980%3A0; visit_id=C9D7A0A5DE9F9F38CFD45A725C0063C5; vip_access_times=%7B%22list%22%3A8%2C%22detail%22%3A2%7D; pg_session_no=182; vip_tracker_source_from=',
        'Referer': 'https://list.vip.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    pool = multiprocessing.Pool(processes=1)
    args = []
    for i in range(1):
        #i = i+37
        args.append(i)
    pool.map(run, args) 

