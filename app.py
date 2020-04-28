import re
from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('mongodb://localhost', 27017)
db = client.gyeonggi_money


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/search', methods=['GET'])
def store_search_list():
    keyword = request.args.get("keyword")
    sigun = request.args.get("sigun")
    sector = request.args.get("sector")

    # 검색어를 포함하고 있는 단어를 db에서 검색
    keyword_rgx = re.compile(f'.*{keyword}.*', re.IGNORECASE)
    sector_rgx = re.compile(f'.*{sector}.*', re.IGNORECASE)
    query = {
        'CMPNM_NM': keyword_rgx,
    }

    if sigun != "지역명":
        query['SIGUN_NM'] = sigun

    if sector != "업종":
        query['INDUTYPE_NM'] = sector_rgx

    stores = []
    store_count = db.store.find(query, {'_id': False}).count()
    for store in db.store.find(query, {'_id': False}).limit(20):
        print(store)
        stores.append(store)
    return jsonify({'result': 'success', 'store_count': store_count, 'store_list': stores})


if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
