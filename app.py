import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('mongodb+srv://slldfg8:qaz741852@cluster0.2uvii.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(3) > td.info > a.title.ellipsis

musics =soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    a = music.select_one('td.info > a.title.ellipsis').text
    singer = music.select_one('td.info > a.artist.ellipsis').text
    titles = music.select_one('td.info > a.albumtitle.ellipsis').text

    doc = {'title': a,
           'singer': singer,
           'albumtitles': titles}
    db.musics.insert_one(doc)




#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.albumtitle.ellipsis