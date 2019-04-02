# 操作FLASK核心对象
from flask import Flask


# 注册蓝图
def register_blueprint(my_app):
    from app.api.hello import hello
    from app.api.user import user
    from app.api.teacher import teacher
    from app.api.login import api
    my_app.register_blueprint(hello)
    my_app.register_blueprint(user)
    my_app.register_blueprint(teacher)
    my_app.register_blueprint(api)


# 创建核心对象
def create_app():
    my_app = Flask(__name__)
    register_blueprint(my_app)
    return my_app
