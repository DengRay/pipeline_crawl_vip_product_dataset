import csv
import base64
from io import BytesIO
from PIL import Image

i = 0
#with open('/home/dengyiru/icut/pic_dataset/test.tsv', 'r', encoding='utf-8') as tsvfile:
with open('/home/dengyiru/icut/all_clean_done/vip_train_imgs.tsv', 'r', encoding='utf-8') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        try:
            field1 = row[0]
            field2 = row[1]
            img = Image.open(BytesIO(base64.urlsafe_b64decode(field2)))
            img.save(f"/home/dengyiru/icut/pic_dataset/recover_pic/temp.jpg", "JPEG", quality=95)
            i += 1
        except:
            print(i)
            print(field1)
    print("done")
tsvfile.close()