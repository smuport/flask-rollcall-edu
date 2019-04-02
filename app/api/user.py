from flask import Blueprint

user = Blueprint('user', __name__)


@user.route('/user')
def get_user():
    return "user"
