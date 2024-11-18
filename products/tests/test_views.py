from rest_framework import status

from products.models import Product


def test_create_product(api_client, token):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'title': 'Televisão 48', 'brand': 'Samsung', 'price': 899.90}
    resp = api_client.post('/api/products/', data=payload, headers=headers)
    assert resp.status_code == status.HTTP_201_CREATED
    assert Product.objects.filter(title=payload['title']).exists()


def test_create_product_unauthorized(api_client):
    payload = {'title': 'Televisão 48', 'brand': 'Samsung', 'price': 899.90}
    resp = api_client.post('/api/products/', data=payload)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


def test_read_product(api_client, product, token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = api_client.get(f'/api/products/{product.id}/', headers=headers)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == {
        'id': product.id,
        'title': product.title,
        'brand': product.brand,
        'price': product.price,
        'image': None
    }


def test_read_nonexistent_product(api_client, product, token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = api_client.get(f'/api/products/{product.id + 1}/', headers=headers)
    assert resp.status_code == status.HTTP_404_NOT_FOUND


def test_update_product(api_client, product, token):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'title': 'Televisão 48', 'brand': 'Samsung', 'price': 899.90}
    resp = api_client.put(f'/api/products/{product.id}/', data=payload, headers=headers)

    assert resp.status_code == status.HTTP_200_OK
    assert Product.objects.filter(title=payload['title']).exists()


def test_delete_product(api_client, product, token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = api_client.delete(f'/api/products/{product.id}/', headers=headers)

    assert resp.status_code == status.HTTP_204_NO_CONTENT
    assert not Product.objects.filter(title=product.title).exists()


def test_delete_nonexistent_product(api_client, product, token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = api_client.delete(f'/api/products/{product.id + 1}/', headers=headers)

    assert resp.status_code == status.HTTP_404_NOT_FOUND
