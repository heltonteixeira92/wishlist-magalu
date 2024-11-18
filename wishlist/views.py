
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from wishlist.models import WishList
from wishlist.serializers import WishListSerializer


class WishListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class WishListDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
