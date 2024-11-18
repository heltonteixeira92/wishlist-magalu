from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import WishList


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ['id', 'customer', 'product']
        validators = [
            UniqueTogetherValidator(
                queryset=WishList.objects.all(),
                fields=['customer', 'product']
            )
        ]
