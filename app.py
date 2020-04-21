import requests
from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# client = MongoClient('localhost', 27017)
# db = client.dbsparta


# HTML을 보여주겠다
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
# DB에 저장되어 있는 모든 것을 조회하겠다
@app.route('/api/list', methods=['GET'])
def store_list():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    res = requests.get(
        'https://openapi.gg.go.kr/RegionMnyFacltStus?Key=7c85b811c8aa4d70a8d44ce50938d346&Type=json&pSize=10',
        headers=headers)
    res_obj = res.json()

    stores = []
    datas = res_obj['RegionMnyFacltStus']
    for data in datas:
        if 'row' in data:
            stores = data['row']
    return jsonify({'result': 'success', 'store_list': stores})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
