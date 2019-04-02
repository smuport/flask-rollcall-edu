# 主要存放和hello有关的接口
# blueprint 蓝图
from flask import Blueprint

hello = Blueprint('hello', __name__)


@hello.route('/hello')
def helloworld():
    return 'hello world, dxq'

