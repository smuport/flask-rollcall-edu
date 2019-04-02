import pytest

from app.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_get_teacher_list(client):
    rv = client.get('/teacher/get')
    assert rv.status_code == 200
    assert rv.is_json
    teachers = rv.json
    assert len(teachers) >= 0


def login(client, username, password):
    return client.post('/login', json=dict(
        user_id=username,
        pwd=password
    ))


def test_login(client):
    """
    测试登陆
    :param client: 模拟客户端
    :return:
    """
    rv = login(client, '233', '2333')
    assert 200 == rv.status_code
    assert rv.is_json
    ret = rv.json
    assert 200 == ret['err_code']
    assert '输入的账号不存在,请重试' == ret['msg']

    rv = login(client, '00001', '2333')
    assert 200 == rv.status_code
    assert rv.is_json
    ret = rv.json
    assert 501 == ret['err_code']
    assert '密码错误,请重试' == ret['msg']

    rv = login(client, '00001', '123')
    assert 200 == rv.status_code
    assert rv.is_json
    ret = rv.json
    assert 100 == ret['err_code']
    assert '登陆成功' == ret['msg']




