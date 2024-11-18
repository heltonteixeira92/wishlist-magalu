from django.urls import path

from wishlist.views import WishListDetailView, WishListView

urlpatterns = [
    path('wishlists/', WishListView.as_view(), name='wishlist'),
    path('wishlists/<int:pk>/', WishListDetailView.as_view(), name='wishlist_detail')
]
