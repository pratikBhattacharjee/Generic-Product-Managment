from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict

from products.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
  
@api_view(['GET'])
def api_home(requests, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = ProductSerializer(model_data).data

    return Response(data)
