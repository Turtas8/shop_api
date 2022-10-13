from rest_framework import serializers
from category.models import Category
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Product
        fields = ('owner', 'title', 'price', 'image')


class ProductDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'
