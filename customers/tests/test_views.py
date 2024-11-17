from rest_framework import status

from customers.models import Customer


def test_create_customer(api_client, token):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'name': 'Matilde Cunha', 'email': 'matildecunha@test.com'}
    resp = api_client.post('/api/customers/', data=payload, headers=headers)

    assert resp.status_code == status.HTTP_201_CREATED
    assert Customer.objects.filter(email=payload['email']).exists()


def test_create_customer_unauthorized(api_client, token):
    payload = {'name': 'Matilde Cunha', 'email': 'matildecunha@test.com'}
    resp = api_client.post('/api/customers/', data=payload)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


def test_read_customer(api_client, customer, token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = api_client.get(f'/api/customers/{customer.id}/', headers=headers)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == {'name': customer.name, 'email': customer.email}


def test_read_nonexistent_customer(api_client, customer, token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = api_client.get(f'/api/customers/{customer.id + 1}/', headers=headers)
    assert resp.status_code == status.HTTP_404_NOT_FOUND


def test_update_customer(api_client, customer, token):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'name': 'Matilde Cunha', 'email': 'matildecunha@test.com'}
    resp = api_client.put(f'/api/customers/{customer.id}/', data=payload, headers=headers)

    assert resp.status_code == status.HTTP_200_OK
    assert Customer.objects.filter(email=payload['email']).exists()


def test_delete_customer(api_client, customer, token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = api_client.delete(f'/api/customers/{customer.id}/', headers=headers)

    assert resp.status_code == status.HTTP_204_NO_CONTENT
    assert not Customer.objects.filter(email=customer.email).exists()


def test_delete_nonexistent_customer(api_client, customer, token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = api_client.delete(f'/api/customers/{customer.id + 1}/', headers=headers)

    assert resp.status_code == status.HTTP_404_NOT_FOUND
