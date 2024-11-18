from rest_framework import serializers

from wishlist.models import WishList

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    wishlist = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['name', 'email', 'wishlist']

    def get_wishlist(self, object):  # noqa
        products = WishList.objects.filter(customer=object.id).values_list('product')
        wishlist = [product[0] for product in list(products)]
        return wishlist
