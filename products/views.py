from products.models import Product
from products.serializers import  ProductSerializerV3
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser


class ProductListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializerV3


class ProductCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializerV3





