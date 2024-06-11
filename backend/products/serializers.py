from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product

class ProductSerializer(ModelSerializer):
    """
    Serializer class for the Product model.
    """
    discount = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'discount'
        ]

    def get_discount(self, obj):
        try:
            return obj.get_discount()
        except Exception as e:
            return None