from main import *
from flask import Blueprint
blueprint = Blueprint("detail", __name__, url_prefix="")
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 토큰 디코드
SECRET_KEY = 'likeMusic'
import jwt

# 코딩 시작

@blueprint.route('/detail')
def detail():
    # 선택된 곡 정보 가져오기
    rank = request.args.get('rank')
    title = request.args.get('title')
    if title is not None:
        title = title.split('(')
    singer = request.args.get('singer')
    album = request.args.get('album')
    cover = request.args.get('cover')
    done = 1

    # 사용자 토큰 확인
    token_receive = request.cookies.get('mytoken')

    if token_receive is None:
        return render_template('detail.html', rank=rank, title=title[0], singer=singer, album=album, cover=cover, done=done)

    id = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])['id']

    # done값을 가져오기 위한 코드
    result = db.mymusic.find_one({'rank':rank, 'id':id})
    if result is not None:
        done = 0

    return render_template('detail.html', token=token_receive, id=id, rank=rank, title=title[0], singer=singer, album=album, cover=cover, done=done)

@blueprint.route('/review', methods=['POST'])
def test_post():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})
        year_receive = request.form['year_give']
        month_receive = request.form['month_give']
        date_receive = request.form['date_give']
        rank_receive = request.form['rank_give']
        comment_receive = request.form['comment_give']
        star_receive = request.form['star_give']
        doc = {
            'year': year_receive,
            'month': month_receive,
            'date': date_receive,
            'rank': rank_receive,
            'id': user_info['id'],
            'comment': comment_receive,
            'star': star_receive
        }
        db.review.insert_one(doc)
        return render_template('detail.html', id=user_info["id"])
    except jwt.exceptions.DecodeError:
        return jsonify({'result':'fail', 'msg':'로그인 페이지로 이동합니다.'})

@blueprint.route('/review', methods=['GET'])
def test_get():
    review_total = list(db.review.find({}, {'_id': False}))
    return jsonify({'reviews':review_total})

# 플레이리스트 담기 버튼 클릭
@blueprint.route('/detail', methods=['POST'])
def get():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        id = db.user.find_one({"id": payload['id']})['id']
        rank_receive = request.form['rank_give']
        cover_receive = request.form['cover_give']
        title_receive = request.form['title_give']
        album_receive = request.form['album_give']
        singer_receive = request.form['singer_give']
        done_receive = request.form['done_give']

        # 아이디 별로 index + 1
        mymusic_index = list(db.mymusic.find({'id':id}))
        count = len(mymusic_index) + 1

        doc = {
            'id': id,
            'index': count,
            'rank': rank_receive,
            'cover': cover_receive,
            'title': title_receive,
            'album': album_receive,
            'singer': singer_receive,
            'done': done_receive
        }
        print('doc', doc)
        db.mymusic.insert_one(doc)

        return jsonify({'result':'success'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result':'fail', 'msg':'로그인 페이지로 이동합니다.'})

# db.mymusic.update_one({'done':[0]}, {'$set': {'done': 1}})

@blueprint.route('/detail/remove', methods=['POST'])
def remove():
    token_receive = request.cookies.get('mytoken')
    try:
        id = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])['id']
        rank = request.form['rank_give']
        db.mymusic.delete_one({'id': id, 'rank':rank})

        return jsonify({'result': 'success', 'msg': '취소에 성공하셨습니다', 'id': id})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 페이지로 이동합니다.'})


@blueprint.route('/review', methods=['GET'])
def music_get():

    mymusic_list = list(db.mymusic.find({}, {'_id': False}))
    return jsonify({'musics' : mymusic_list})