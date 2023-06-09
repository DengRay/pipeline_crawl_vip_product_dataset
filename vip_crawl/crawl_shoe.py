import requests
import json
import math
import multiprocessing
import os
import time

def get_useful_id(urls,save_path,min,max):
    pro_id = []
    for num in range(0,(12)*120,120):  #这里是从第二页开始取数据了，第一个参数可以设置为0 最大页码即为12
        url = urls + f'&pageOffset={num}&salePlatform=1&priceRange={min}-{max}&_=1686131653466'
        #url = urls + f'&pageOffset={num}&salePlatform=1&_=1686131653466'
        try:
            html = requests.get(url,headers=headers_,proxies=proxies)
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

def run(arg):
    with open("/home/dengyiru/vip_crwal/cate_shoe.json", "r",encoding='utf-8') as f_r:
        #/home/dengyiru/y-vip_crwal/cate_shoe.json
        data = json.load(f_r)
        all_id  = []
        a_id = []
        flag = 1
        item = data[arg]
        cate = item[1]
        save_path = f"/home/dengyiru/vip_crwal/id_shoe/{arg}_{cate}.json"
        url = f"https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=101101101&client=pc&mobile_platform=1&province_id=101101&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1685072251637_f27b8e963323255d21a6da529e836b1e&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId={cate}&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=0"
        
        #lis = get_useful_id(url,save_path,0,0)
        #unique_id = list(set(lis))
        

        value_list = [100,200,250,300,400,500,5000]
        for i in range (len(value_list)-1):
            min = value_list[i]
            max = value_list[i+1]
            lis = get_useful_id(url,save_path,min,max)
            all_id.extend(lis)
        unique_id = list(set(all_id))
        
        #print(len(unique_id))
        with open(save_path,'w',encoding='utf-8') as f_w:
            json.dump(unique_id,f_w,ensure_ascii=False)
        print("the unique item in {} is {}".format(cate,len(unique_id)))
        '''
        print("spliting price,please wait!")
        #value_list = get_value_split(url)
        value_list = [100,200,250,300,400,500,5000]
        print("spliting price done!")
        print('get item id,please wait!')
        #while(flag != len(a_id)):
        while True:
            flag = len(a_id)
            #all_id = []
            #get_useful_id(url,save_path,0,0)
            for i in range (len(value_list)-1):
            #i = 0
                min = value_list[i]
                max = value_list[i+1]
                lis = get_useful_id(url,save_path,min,max)
                all_id.extend(lis)
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
            '''
        #return all_id
            

     
if __name__ == '__main__':
    '''
    headers_ = {
        'Cookie': 'vip_cps_cuid=CU1680577573878429d3b6748134397e; vip_cps_cid=1680577573880_1be6e615f0b136d5c68c9528973cbc8d; PAPVisitorId=7025c19292974aff36f0f40d24fdc4eb; vip_new_old_user=1; vip_city_name=%E5%B9%BF%E5%B7%9E%E5%B8%82; mars_cid=1680577576776_664414ba2ad18014bf115f032e8fa34c; mars_sid=d30d0d37f6bf0350d89f998b5767def2; mars_pid=0; PHPSESSID=dtqk8agrh3to6rgeqt4g2jf8h3; vip_address=%257B%2522pname%2522%253A%2522%255Cu5317%255Cu4eac%255Cu5e02%2522%252C%2522pid%2522%253A%2522101101%2522%252C%2522cname%2522%253A%2522%255Cu5e7f%255Cu5dde%255Cu5e02%2522%252C%2522cid%2522%253A%2522101101101%2522%257D; vip_province=101101; vip_province_name=%E5%8C%97%E4%BA%AC%E5%B8%82; vip_city_code=101101101; vip_wh=VIP_BJ; vip_ipver=31; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A1%7Cul%3A3105; VipDFT=0; cps_share=cps_share; mst_area_code=104104; cps=adp%3Antq8exyc%3A%40_%401681790112898%3Amig_code%3A4f6b50bf15bfa39639d85f5f1e15b10f%3Aac014miuvl0000b5sq8cvtz9ogmr2lld; user_class=a; vpc_uinfo=fr713%3A0%2Cfr1352%3A0%2Cfr674%3AD1%2Cfr1051%3A0%2Cfr766%3A0%2Cfr259%3AS0-4%2Cfr896%3A0%2Cfr0901%3A0%2Cfr884%3A0%2Cfr863%3A0%2Cfr392%3A310505%2Cfr398%3A0%2Cfr408%3A0%2Cfr251%3AA%2Cfr1195%3A0%2Cfr344%3A0%2Cfr444%3AA%2Cfr848%3A0%2Cfr1196%3A0%2Cfr249%3AA1%2Cfr328%3A3105%2Cfr902%3A0%2Cfr901%3A0%2Cfr980%3A0; visit_id=C9D7A0A5DE9F9F38CFD45A725C0063C5; vip_access_times=%7B%22list%22%3A8%2C%22detail%22%3A2%7D; pg_session_no=182; vip_tracker_source_from=',
        'Referer': 'https://list.vip.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    '''
    headers_ = {       
        'Cookie': 'mars_cid=1680593954989_25174b1c65e9de41c5467b61ab30affd; mars_pid=0; mars_sid=785595c824d70f29cc2228b29cae2a65; visit_id=61700065DE085448004B59FA25168461; pg_session_no=46; vip_tracker_source_from=; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A1%7Cul%3A3105; user_class=a; vip_access_times=%7B%22list%22%3A3%7D; vip_address=%257B%2522pname%2522%253A%2522%255Cu5317%255Cu4eac%255Cu5e02%2522%252C%2522pid%2522%253A%2522101101%2522%252C%2522cname%2522%253A%2522%255Cu5e7f%255Cu5dde%255Cu5e02%2522%252C%2522cid%2522%253A%2522101101101%2522%257D; vip_city_code=101101101; vip_city_name=%E5%B9%BF%E5%B7%9E%E5%B8%82; vip_province=101101; vip_province_name=%E5%8C%97%E4%BA%AC%E5%B8%82; vip_wh=VIP_BJ; cps=adp%3Antq8exyc%3A%40_%401683799131180%3Amig_code%3A4f6b50bf15bfa39639d85f5f1e15b10f%3Aac014miuvl0000b5sq8c5rgou9b9hark; cps_share=cps_share; vip_ipver=31; mst_area_code=101101101; vip_cps_cuid=CU168371685352970ee0d870bfb88695; PAPVisitorId=c4be9faa4c599e3c7e6678dbd8ba75d7; vip_cps_cid=1680593938712_9870204b9f6e83ecc41dad0286dd2aff; vip_new_old_user=1',
        'Referer': 'https://list.vip.com/autolist.html?rule_id=53986307&title=%E8%BF%9E%E8%A1%A3%E8%A3%99&refer_url=https%3A%2F%2Fcategory.vip.com%2Fhome',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15'
    }
    proxies = {
      "http": "http://t17895897212428:1cvlhwmw@w386.kdltps.com:15818",
      "https": "http://t17895897212428:1cvlhwmw@w386.kdltps.com:15818"
    }
    '''
    url = f"https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=101101101&client=pc&mobile_platform=1&province_id=101101&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1680577576776_664414ba2ad18014bf115f032e8fa34c&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId=52044471&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=0"
    #url = url + f'&pageOffset=0&salePlatform=1&&_=1686131653466'
    url = f"https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2?callback=getProductIdsListRank&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=101101101&client=pc&mobile_platform=1&province_id=101101&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1685072251637_f27b8e963323255d21a6da529e836b1e&wap_consumer=a&uid=&abtestId=1872&mtmsRuleId=52044471&scene=rule_stream&sizeNames=&props=&vipService=&bigSaleTagIds=&filterStock=0&brandStoreSns=&sort=0&pageOffset=0&salePlatform=1&_=1686136141777"
    html = requests.get(url,headers=headers_,proxies=proxies)
    print(html)
    '''
    for i in range(21,50):
        run(i)
    
    '''
    pool = multiprocessing.Pool(processes=1)
    args = []
    for i in range(1):
        #i = i+25
        args.append(i)
    pool.map(run, args)
    '''
    

