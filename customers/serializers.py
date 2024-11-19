from rest_framework import serializers

from wishlist.models import WishList

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    wishlist = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['name', 'email', 'wishlist']

    def get_wishlist(self, object):  # noqa
        qty_product = WishList.objects.filter(customer=object.id).count()
        wishlist = f'user has {qty_product} products on their wishlist'
        return wishlist
