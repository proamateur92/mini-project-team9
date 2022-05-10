from main import *
from flask import Blueprint


blueprint = Blueprint("detail", __name__, url_prefix="")

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# 토큰 디코드
SECRET_KEY = 'likeMusic'

import jwt

for music in musics:
    a = music.select_one('td.info > a.title.ellipsis').text
    singer = music.select_one('td.info > a.artist.ellipsis').text
    album = music.select_one('td.info > a.albumtitle.ellipsis').text
    cover = music.select_one('td:nth-child(3) > a > img')['src']

    doc = {
        'title': a,
        'singer': singer,
        'album': album,
        'cover': cover
    }
    db.musics.insert_one(doc)

# 코딩 시작


@blueprint.route('/reviewform')
def home():
    return render_template('detail.html')

@blueprint.route('/detail', methods=['GET'])
def music_get():
    music_total = list(db.musics.find({}, {'_id': False}))

    return jsonify({'musics':music_total})

@blueprint.route('/review', methods=['POST'])
def test_post():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})
        comment_receive = request.form['comment_give']
        star_receive = request.form['star_give']
        doc = {
            'id': user_info['id'],
            'comment': comment_receive,
            'star': star_receive
        }
        db.review.insert_one(doc)
        return render_template('detailTest.html', id=user_info["id"])
    except jwt.exceptions.DecodeError:
        return jsonify({'result':'fail', 'msg':'로그인 페이지로 이동합니다.'})



@blueprint.route('/review', methods=['GET'])
def test_get():
    review_total = list(db.review.find({}, {'_id': False}))
    print(review_total)
    return jsonify({'reviews':review_total})

