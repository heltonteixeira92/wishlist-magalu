from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.serializers import ProductSerializer


class ProductView(generics.ListCreateAPIView):
    """view for listing a queryset or creating a model instance"""
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """view for retrieving, updating or deleting a model instance"""
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
