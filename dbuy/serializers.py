from rest_framework import serializers
from .models import Product, Comment, Contact


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # comments = serializers.HyperlinkedRelatedField(
    #     view_name='comment_detail',
    #     many=True,
    #     read_only=True,
    # )

    product_url = serializers.ModelSerializer.serializer_url_field(
        view_name='product_detail'
    )

    class Meta:
        model = Product
        fields = ('id', 'product_url', 'title', 'category', 'image', 'description',
                  'location', 'condition', 'brand', 'color', 'price', 'user_id',)


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        view_name='product_detail',
        read_only=True
    )

    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )

    class Meta:
        model = Comment
        fields = ('id', 'username', 'content',
                  'user_id', 'product', 'product_id',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'username', 'user_id', 'email',
                  'phone', 'instagram_username',)
