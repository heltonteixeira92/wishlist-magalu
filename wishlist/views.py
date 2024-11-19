from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from wishlist.models import WishList
from wishlist.serializers import WishListSerializer


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(name='customer', description='Customer Id', type=int),
        ]
    )
)
class WishListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WishListSerializer

    def get_queryset(self):
        queryset = WishList.objects.all()
        customer = self.request.query_params.get('customer')
        if customer is not None:
            queryset = queryset.filter(customer_id=customer)
        return queryset


class WishListDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
