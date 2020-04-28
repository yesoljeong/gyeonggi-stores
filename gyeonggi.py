import requests

from pymongo import MongoClient

#client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.gyeonggi_money

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://openapi.gg.go.kr/RegionMnyFacltStus?Key=7c85b811c8aa4d70a8d44ce50938d346&Type=json&SIGUN_NM=용인시&pSize=1&pIndex=1'
res = requests.get(url, headers=headers)
res_obj = res.json()

data_list = res_obj['RegionMnyFacltStus'][0]
print(res_obj)
head_obj = data_list['head'][0]
count_num = head_obj['list_total_count']
loop_count = int(count_num/100 + 1)

# for i in range(loop_count):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     url = 'https://openapi.gg.go.kr/RegionMnyFacltStus?Key=7c85b811c8aa4d70a8d44ce50938d346&Type=json&SIGUN_NM=용인시&pSize=1000&pIndex=' \
#           + str(i + 1)
#     res = requests.get(url,
#                        headers=headers)
#     res_obj = res.json()
#
#     stores = []
#     datas = res_obj['RegionMnyFacltStus']
#     for data in datas:
#         if 'row' in data:
#             stores = data['row']
#             db.store.insert_many(stores)
