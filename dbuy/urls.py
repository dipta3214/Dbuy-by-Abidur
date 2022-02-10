from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('comments/', views.CommentList.as_view(), name="comment_list"),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name="comment_detail"),
    path('contacts/', views.ContactList.as_view(), name="contact_list"),
    path('contacts/<int:pk>', views.ContactDetail.as_view(), name="contact_detail")
]
