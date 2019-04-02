
import requests


def test_hello():
    url = "http://localhost:5000/hello"
    r = requests.get(url)
    ret = r.text

    assert ret == 'hello world, dxq'

