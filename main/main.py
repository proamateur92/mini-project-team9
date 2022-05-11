from main import * #main에 선언된 모든 값을 가져온다.
from flask import Blueprint

app = Flask(__name__)

SECRET_KEY = 'likeMusic'
blueprint = Blueprint("home", __name__, url_prefix="/")

# 지니 차트 200 DB insert 작업
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://www.genie.co.kr/chart/top200', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup = BeautifulSoup(data.text, 'html.parser')
# chart =soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# for music in chart:
#     rank = music.select_one('td.number').text[:2].strip()
#     a = music.select_one('td.info > a.title.ellipsis').text.strip()
#     a = music.select_one('td.info > a.title.ellipsis').text.strip()
#     if a[0:3] == '19금':
#         a = a[4:].strip()
#     singer = music.select_one('td.info > a.artist.ellipsis').text
#     album = music.select_one('td.info > a.albumtitle.ellipsis').text
#     cover = music.select_one('td:nth-child(3) > a > img')['src']
#     doc = {
#             'rank': rank,
#             'title': a,
#            'singer': singer,
#            'album': album,
#            'cover':cover}
# db.chart.insert_one(doc)

# 차트 전체 불러오기
@blueprint.route('/musiclist', methods=['GET'])
def musiclist():
    chart = list(db.chart.find({}, {'_id': False}))
    return jsonify({'chart': chart})
