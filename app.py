import re

import requests
from bson.json_util import dumps
from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.gyeonggi_money


# HTML을 보여주겠다
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
# DB에 저장되어 있는 모든 것을 조회하겠다
@app.route('/api/search', methods=['GET'])
def store_search_list():
    keyword = request.args.get("keyword")
    sigun = request.args.get("sigun")
    sector = request.args.get("sector")

    keyword_rgx = re.compile(f'.*{keyword}.*', re.IGNORECASE)
    sector_rgx = re.compile(f'.*{sector}.*', re.IGNORECASE)
    query = {
        'CMPNM_NM': keyword_rgx,
        # 'INDUTYPE_NM': sector_rgx
    }

    if sigun != "지역명":
        query['SIGUN_NM'] = sigun

    if sector != "업종":
        query['INDUTYPE_NM'] = sector_rgx

    print('검색조건: ', query)
    stores = []
    for store in db.store.find(query, {'_id': False}).limit(10):
        print(store)
        stores.append(store)
    return jsonify({'result': 'success', 'store_list': stores})


@app.route('/api/list', methods=['GET'])
def store_list():
    stores = []
    for store in db.store.find({}, {'_id': False}).limit(10):
        stores.append(store)
    return jsonify({'result': 'success', 'store_list': stores})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
