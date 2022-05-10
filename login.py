from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://16thMembers:advanceToyproject@boilerplate.s8tem.mongodb.net/mini?retryWrites=true&w=majority')
db = client.mini

SECRET_KEY = 'likeMusic'

import jwt
import datetime
import hashlib


@app.route('/write_review', methods=['POST'])
def write_review():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})
        # 리뷰 작성 - DB 작업
        print('리뷰 작성할 아이디', user_info['id'])
        return render_template('detailTest.html', id=user_info["id"])
    except jwt.exceptions.DecodeError:
        return jsonify({'result':'fail', 'msg':'로그인 페이지로 이동합니다.'})

# 상세 페이지 예제 코드
@app.route('/detail')
def detail():
    token_receive = request.cookies.get('mytoken')
    return render_template('detailTest.html', token=token_receive)

# 토큰 값 가져오기 예제 코드
@app.route('/hey', methods=['POST'])
def hey():
    token_receive = request.cookies.get('mytoken')
    # text 받아오기
    # text = request.form['text']
    result = False
    if token_receive:
        result = True
    return jsonify({'result': result})

@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    return render_template('mainTest.html', token=token_receive)

# token_receive = request.cookies.get('mytoken')
# try:
#     payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#     user_info = db.user.find_one({"id": payload['id']})
#     return render_template('mainpage.html', id=user_info["id"])
# except jwt.exceptions.DecodeError:
#     return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))
@app.route('/loginForm')
def loginForm():
    msg = request.args.get("msg")
    return render_template('loginForm.html', msg=msg)


@app.route('/user/idChecker', methods=['POST'])
def id_checker():
    id_receive = request.form['id_give']
    id_check = db.user.find_one({'id': id_receive})
    result = False
    msg = '중복된 아이디입니다.'

    # id 중복확인 후 중복이 아니면 true값 리턴
    if id_check is None:
        result = True
        msg = '사용가능한 아이디입니다.'

    return jsonify({'result': result, 'msg': msg})


# 저장하기 전에, pw를 sha256 방법(=단방향 암호화. 풀어볼 수 없음)으로 암호화해서 저장.
@app.route('/user/register', methods=['POST'])
def user_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    doc = {'id': id_receive, 'password': pw_hash}
    db.user.insert_one(doc)

    return jsonify({'msg': '회원가입을 완료하였습니다!'})


# 로그인
@app.route('/user/login', methods=['POST'])
def user_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # 회원가입 때와 같은 방법으로 pw를 암호화
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    # 가입된 유저 정보 확인
    result = db.user.find_one({'id': id_receive, 'password': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급
    if result is not None:
        payload = {
            'id': id_receive,
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디 또는 비밀번호가 일치하지 않습니다.'})


if __name__ == '__main__':
    login.run('0.0.0.0', port=5000, debug=True)


