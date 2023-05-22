import requests
from bs4 import BeautifulSoup
import json

headers = { 
    'Cookie': 'mars_cid=1680593954989_25174b1c65e9de41c5467b61ab30affd; mars_pid=0; mars_sid=c349dc6daa5ee6ce0c1b4fe1b3892c9b; visit_id=01621C261A68750014B91FAE9DFCADCF; pg_session_no=69; vip_tracker_source_from=; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A1%7Cul%3A3105; user_class=a; vip_address=%257B%2522pname%2522%253A%2522%255Cu5317%255Cu4eac%255Cu5e02%2522%252C%2522pid%2522%253A%2522101101%2522%252C%2522cname%2522%253A%2522%255Cu5e7f%255Cu5dde%255Cu5e02%2522%252C%2522cid%2522%253A%2522101101101%2522%257D; vip_city_code=101101101; vip_city_name=%E5%B9%BF%E5%B7%9E%E5%B8%82; vip_province=101101; vip_province_name=%E5%8C%97%E4%BA%AC%E5%B8%82; vip_wh=VIP_BJ; cps=adp%3Antq8exyc%3A%40_%401680752540917%3Amig_code%3A4f6b50bf15bfa39639d85f5f1e15b10f%3Aac014miuvl0000b5sq8cu58w8rvr0shc; cps_share=cps_share; vip_access_times=%7B%22list%22%3A8%2C%22detail%22%3A4%7D; VipDFT=1; PHPSESSID=ndq2ja5fbjmbjdd0rmrm9e3jp7; vip_ipver=31; PAPVisitorId=c4be9faa4c599e3c7e6678dbd8ba75d7; vip_cps_cid=1680593938712_9870204b9f6e83ecc41dad0286dd2aff; vip_cps_cuid=CU168059393870969da44d84dd40c7c8; vip_new_old_user=1',
    'Referer': 'https://www.vip.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15'
}

#url = f'https://mapi.vip.com/vips-mobile/rest/shopping/pc/category/index/get_tab_data/v1?callback=getSubCategory30074&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=101101101&client=pc&mobile_platform=1&province_id=101101&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1680593954989_25174b1c65e9de41c5467b61ab30affd&wap_consumer=a&hierarchyId=117&categoryId=30074&clientFrom=PC&net=wifi&width=1194&height=834&pcmpWidth=750&mobile_channel=nature&functions=jumper&_=1680760304059'
#url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/category/index/get_tab_data/v1?callback=getSubCategory324442&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=101101101&client=pc&mobile_platform=1&province_id=101101&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1680593954989_25174b1c65e9de41c5467b61ab30affd&wap_consumer=a&hierarchyId=117&categoryId=324442&clientFrom=PC&net=wifi&width=1194&height=834&pcmpWidth=750&mobile_channel=nature&functions=jumper&_=1680760304060'
url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/category/index/get_tab_data/v1?callback=getSubCategory30066&app_name=shop_pc&app_version=4.0&warehouse=VIP_BJ&fdc_area_id=101101101&client=pc&mobile_platform=1&province_id=101101&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid=1680577576776_664414ba2ad18014bf115f032e8fa34c&wap_consumer=a&hierarchyId=117&categoryId=30066&clientFrom=PC&net=wifi&width=1440&height=900&pcmpWidth=750&mobile_channel=nature&functions=jumper&_=1681032735773'
html = requests.get(url,headers=headers)
    #print(html.text)
    #注意下面的代码是在for循环中
start = html.text.index('{')
end = html.text.index('})')+1
json_data = json.loads(html.text[start:end])
#print(json_data)

product_ids = json_data['data']['data']['sectionList']

categories = []
for product_id in product_ids:
    temp0 = product_id['category']
    name = product_id['category']['name']
    pro_ = product_id['category']['children']
    #print(name)
    for item in pro_:
        temp1 = item['name']
        temp2 = item['categoryId']
        categories.append([temp1,temp2])
    #print('商品id',product_id['category'])

with open("/home/dengyiru/vip_crwal/cate.json", "a") as f:
    json.dump(categories, f,ensure_ascii=False)
    f.write("\n")