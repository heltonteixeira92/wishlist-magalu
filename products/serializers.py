from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'title', 'brand', 'price', 'image']
