from rest_framework import status


def test_get_jwt_token(api_client, user):
    payload = {'email': user.email, 'password': user.clean_password}
    resp = api_client.post('/api/token/', data=payload, format='json')
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['access']
    assert resp.json()['refresh']


def test_refresh_jwt_token(api_client, refresh_token):
    payload = {'refresh': refresh_token}
    resp = api_client.post('/api/token/refresh/', data=payload, format='json')
    assert resp.status_code == status.HTTP_200_OK


def test_register(api_client, db):
    payload = {'name': 'test', 'email': 'test@test.com', 'password': '123@mudar'}
    resp = api_client.post('/register/', data=payload)
    assert resp.status_code == status.HTTP_201_CREATED

