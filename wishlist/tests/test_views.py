from rest_framework import status

from wishlist.models import WishList


def test_create_wishlist(api_client, token, product, customer):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'product': product.id, 'customer': customer.id}
    resp = api_client.post('/api/wishlists/', data=payload, headers=headers)
    assert resp.status_code == status.HTTP_201_CREATED
    assert WishList.objects.filter(product=product.id, customer=customer.id).exists()


def test_create_wishlist_unauthorized(api_client, product, customer):
    payload = {'product': product.id, 'customer': customer.id}
    resp = api_client.post('/api/wishlists/', data=payload)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


def test_read_wishlist(api_client, wishlist, token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = api_client.get(f'/api/wishlists/{wishlist.id}/', headers=headers)
    assert resp.status_code == status.HTTP_200_OK


def test_read_nonexistent_wishlist(api_client, wishlist, token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = api_client.get(f'/api/wishlists/{wishlist.id + 1}/', headers=headers)
    assert resp.status_code == status.HTTP_404_NOT_FOUND


def test_update_wishlist(api_client, wishlist, customer, product2, token):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'customer': customer.id, 'product': product2.id}
    resp = api_client.put(f'/api/wishlists/{wishlist.id}/', data=payload, headers=headers)

    assert resp.status_code == status.HTTP_200_OK
    assert WishList.objects.filter(product=product2.id, customer=customer.id).exists()


def test_delete_wishlist(api_client, wishlist, token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = api_client.delete(f'/api/wishlists/{wishlist.id}/', headers=headers)

    assert resp.status_code == status.HTTP_204_NO_CONTENT
    assert not WishList.objects.filter(id=wishlist.id).exists()


def test_delete_nonexistent_wishlist(api_client, wishlist, token):
    headers = {'Authorization': f'Bearer {token}'}
    resp = api_client.delete(f'/api/wishlists/{wishlist.id + 1}/', headers=headers)

    assert resp.status_code == status.HTTP_404_NOT_FOUND
