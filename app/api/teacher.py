import pymysql
from flask import Blueprint, jsonify

from app.db.db import connect_db

teacher = Blueprint('teacher', __name__)


# pymysql
@teacher.route('/teacher/get')
def get_teacher():
    cursor = connect_db().cursor()
    sql ="select * from teacher"
    cursor.execute(sql)
    data = cursor.fetchall()
    teachers = []
    for row in data:
        teachers.append({
            'user_id': row[0],
            'pwd': row[1],
            'teacher_num': row[2],
            'name': row[3],
            'university': row[4],
            'college': row[5],
            'tel': row[6],
            'rec_time': row[7]
        })
    return jsonify(teachers)

