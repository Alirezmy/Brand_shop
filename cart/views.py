from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from cart.services import add_to_cart
from rest_framework import status


class AddToCartView(APIView):
    def post(self, request, *args, **kwargs):
        product_id = request.data['product_id']
        user = request.user
        quantity = request.data['quantity']
        cart_item = add_to_cart(user=user, product_id=product_id, quantity=quantity)
        return Response({'cart_item': cart_item.id}, status=status.HTTP_201_CREATED)

