from flask import Flask, request, render_template, g
import sqlite3
import os
import json

app = Flask(__name__)
app.secret_key = os.urandom(32)  # 세션 생성

# 키 파일 불러옴
with open("./passwd.json", "r") as file:
    PASSWORD = json.load(file)

# 디비 구성
DATABASE = "database.db"
if not os.path.exists(DATABASE):
    db = sqlite3.connect(DATABASE)
    db.execute('create table androidwoojea(stage int, password char(100));')
    db.execute(f'insert into androidwoojea(stage, password) values (1, "{PASSWORD["stage1"]}")')
    db.execute(f'insert into androidwoojea(stage, password) values (2, "{PASSWORD["stage2"]}")')
    db.execute(f'insert into androidwoojea(stage, password) values (3, "{PASSWORD["stage3"]}")')
    db.commit()
    db.close()

# 디비를 불러옴
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

# 디비에 쿼리를 날림
def query_db(query, one=True):
    cur = get_db().execute(query)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# 요청이 완료되면 db를 닫음
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# 메인 페이지
@app.route('/')
def index():
    password = request.args.get('pw')  # pw 파라미터 값을 받음
    if not password:
        return render_template('index.html')

    res = query_db(f'select * from androidwoojea where stage=1 and password="{password}"')
    if res and res['password'] == PASSWORD["stage1"]:
        return render_template('correct1.html')
    elif PASSWORD["stage1"].startswith(password):
        return render_template('partial_match.html')
    return render_template('incorrect.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
