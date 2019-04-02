from datetime import datetime

from flask import Blueprint, request, jsonify

from app.db import db

api = Blueprint('login', __name__)


# GET,POST,PUT,DELETE
@api.route('/login', methods=['POST'])
def teacher_login():
    teacher = request.get_json()
    cursor = db.connect_db().cursor()

    sql = "select user_id,pwd from teacher where user_id= '" + teacher['user_id'] + "'"
    cursor.execute(sql)
    data = cursor.fetchone()
    if not data:
        return jsonify({"err_code": 200, "msg": "输入的账号不存在,请重试"})
    if data[1] == teacher['pwd']:
        return jsonify({"err_code": 100, "msg": "登陆成功"})
    else:
        return jsonify({"err_code": 501, "msg": "密码错误,请重试"})


@api.route('/register', methods=['POST'])
def register_teacher():
    teacher = request.get_json()
    teacher['rec_time'] = str(datetime.now())
    database = db.connect_db()
    cursor = database.cursor()
    try:
        sql = "select user_id,pwd from teacher where user_id= '" + teacher['user_id'] + "'"
        cursor.execute(sql)
        data = cursor.fetchone()
        if data:
            return jsonify({"err_code": 500, "msg": "该账号已经注册,请直接登陆"})
        else:
            sql_insert = "insert into teacher(user_id,pwd,teacher_num,name,university,college,tel,rec_time) " \
                         "values (" + "'" + teacher['user_id'] + "','" + teacher['pwd'] + "','"\
                         + teacher['teacher_num'] + "','" + teacher['name'] + "','" + teacher['university'] \
                         + "','" + teacher['college'] + "','" + teacher['tel'] + "','" + teacher['rec_time'] + "')"
            # sql_insert_2 = "insert into teacher(user_id,pwd,teacher_num,name,university,college,tel,rec_time)values" \
            #                "(%s,%s,%s,%s,%s,%s,%s,str_to_date(%s,'%Y-%m-%d %H:%i:%s'))",
            # (teacher['user_id'],teacher['pwd'],....)
            cursor.execute(sql_insert)
            database.commit()
            return jsonify({'err_code': 200, 'msg': "注册成功"})
    except:
        database.rollback()
        return jsonify({'err_code': 201, 'msg': "注册失败"})
