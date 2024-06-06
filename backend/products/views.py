from rest_framework import generics


from .models import Product
from .serializers import ProductSerializer



#this is a class-based view that inherits from generics.ListAPIView
#unclear what the generic does still
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #say i want to assign something to that data
    #this doesn't work
    def perform_create(self, serializer):
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "There is no description to this product."

        serializer.save(content=content)

        #send a Django Signal


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
