from django.urls import path

from products.views import ProductDetailView, ProductView

urlpatterns = [
    path('products/', ProductView.as_view(), name='product'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
