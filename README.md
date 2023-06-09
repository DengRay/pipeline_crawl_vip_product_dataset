# pipeline_crawl_vip_product_dataset
Infimind project to construct a foundation for a database of a magnitude of millions  for clothing merchandise

## The pipeline to crawls data on the magnitude of millions

1. get the categories id of the products,such as ["连衣裙", "53986307"],running the crawl_cate.py
2. select a large enough quantity of goods (more than 10000 pieces)product category,running the get_up10000.py
3. crawl the products id with parallel method,running the crawl_new.py
4. crawl the detail content of each product,running get_content.py
5. crawl the image of each products, running the parallel_dl_three.py
6. preprocess the data and package the data, running generate_train_jsonl_three.py and generate_tsv_three.py

## some other preprocess script：
- clean_json.py: to ensure the product in jsonl file is unique.
- cmp_count_new.py: to Verify the integrity and consistency of the downloaded data.
- count_new.py：calculate the number of download data in specific directory
- recover_pic.py ：convert the base64 encoding to the original picture

## The package using in the project
json,requests,bs4,multiprocessing,csv,base64,PIL(pillow)

## The data format：
- image dataset format(tsv):1000002	/9j/4AAQSkZJ...YQj7314oA//2Q== （商品图片id，'\t'，商品图片内容) (base64编码）
- text/query dataset format(jsonl):{"query_id": 8426, "query_text": "胖妹妹松紧腰长裤", "item_ids": [42967]}

##updata(2023.6.9):
- crawl the picture and video on vip product homepage with proxies
- run crawl_shoe.py,get_content_shoe.py,parallel_dl_three_shoe.py
- add the vip categories id (json file)
