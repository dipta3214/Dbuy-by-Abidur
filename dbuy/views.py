from itertools import product
from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import ProductSerializer, CommentSerializer
from .models import Product, Comment
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
# views.py


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Filter
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['color']
    # Search
    search_fields = ['title', 'brand']
    # Ordering
    ordering_fields = ['color']


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
