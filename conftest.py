import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from customers.models import Customer


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    pwd = 'test123@mudar'
    user = get_user_model().objects.create_user(email='test@test.com', password=pwd)
    user.clean_password = pwd  # monkey patch
    return user


@pytest.fixture
def customer(db):
    return Customer.objects.create(name='foo bar', email='foo.bar@test.com')


@pytest.fixture
def token(user, api_client):
    payload = {'email': user.email, 'password': user.clean_password}
    resp = api_client.post('/api/token/', data=payload, format="json")
    return resp.json()['access']


@pytest.fixture
def refresh_token(user, api_client):
    payload = {'email': user.email, 'password': user.clean_password}
    resp = api_client.post('/api/token/', data=payload, format="json")
    return resp.json()['refresh']


@pytest.fixture
def logged_in_client(user, api_client):
    api_client.force_authenticate(user, token=token)
    return api_client
