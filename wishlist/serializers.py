from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from products.models import Product

from .models import WishList


class WishListSerializer(serializers.ModelSerializer):
    product_detail = serializers.ModelSerializer

    class Meta:
        model = WishList
        fields = ['id', 'customer', 'product']
        validators = [
            UniqueTogetherValidator(
                queryset=WishList.objects.all(),
                fields=['customer', 'product']
            )
        ]

    def to_representation(self, instance):
        instance = super(WishListSerializer, self).to_representation(instance)
        products = Product.objects.filter(
            id=instance['product']).values('title', 'image', 'price')
        instance['product_detail'] = [product for product in products]
        return instance
