from django.urls import path
from customers import views

urlpatterns = [
    path('customers/', views.CustomerView.as_view()),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view())
]
