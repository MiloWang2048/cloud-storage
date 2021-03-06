import base64


def test_basic_auth(client, user):
    c = client
    r = c.get('/api/storage/')
    assert r.status_code == 401
    headers = {
        'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(b'test:test').decode("ascii")
    }
    r = c.get('/api/storage/', **headers)
    assert r.status_code == 200
