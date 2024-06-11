from rest_framework import generics, mixins
import rest_framework


from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view



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

#class-based view to handle update
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.content is None:
            instance.content = instance.title
            pass

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET', 'POST'])
def product_alt_view(request,pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk:
            #detail view to get one product
            obj = get_object_or_404(Product, pk=pk)
            if obj:
                data = ProductSerializer(obj, many=False).data
                return Response(data)
        else:
            #list view
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)
    if method == "POST":
        #POST Request -> create view
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = "There is no description to this product."
            serializer.save(content=content)
            return Response(serializer.data)
        return Response(serializer.errors)
    

#Mixin View

class ProductMixinView(generics.GenericAPIView,
                       mixins.ListModelMixin
                       ,mixins.RetrieveModelMixin
                       ,mixins.CreateModelMixin
                       ,mixins.UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)