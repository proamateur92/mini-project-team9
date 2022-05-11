from main import * # main에 선언된 모든 값을 가져와요 , __init__ file에 선언된 라이브러리를 가져와 사용할 수 있습니다
from flask import Blueprint

app = Flask(__name__)

SECRET_KEY = 'likeMusic'
blueprint = Blueprint("mypage", __name__, url_prefix="/")

# 마이페이지로 이동해요
@blueprint.route('/mypage')
def mypage():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})

        # 로그인한 아이디 가져오기
        # id = user_info['id']

        # DB로부터 플레이리스트 가져오기
        # db.playlist.find_one({"id": id})

        # {'id': id,
        #  'playlist': {
        # 1: ['title': title, 'album': album],
        # 2: ['title':title, 'album': album],
        # 3: ['title':title, 'album': album],
        # }}

        # doc = {
        # }

        return render_template('mypage.html', token=token_receive)
    except jwt.exceptions.DecodeError:
        return render_template('loginForm.html')

# db에 들어온 정보들을 플레이리스트로 저장해서 넘겨줘요
@blueprint.route('/playlist', methods=['GET'])
def web_playlist_get():
    play_list = list(db.chart.find({}, {'_id': False}))
    return jsonify({'playlist': play_list})
