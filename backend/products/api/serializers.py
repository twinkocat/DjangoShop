from rest_framework import serializers
from collections import OrderedDict


from products.models.product import Product


class ProductsListSerializer(serializers.ModelSerializer):
    type = serializers.CharField()
    brand = serializers.CharField()
    name = serializers.CharField(source='model.name')
    photos = serializers.SlugRelatedField(many=True, read_only=True, slug_field='image_url')
    available = serializers.CharField()
    price = serializers.CharField(source='model.get_formatted_price_display')
    discount = serializers.DictField(source='get_discount',)

    class Meta:
        model = Product
        fields = ['type', 'brand', 'name', 'photos', 'available', 'price', 'discount',]

    def to_representation(self, instance):
        result = super(ProductsListSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
