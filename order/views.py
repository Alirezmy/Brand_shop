from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from order.models import Order, OrderItem
from cart.models import Cart
from order.servises import decrease_product_count, create_checkout, payment_failed, payment_succeed

class CreateCheckoutApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        payment = create_checkout(request.user)
        return Response(payment)

class PaymentSuccceedApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, payment_id):
        payment = payment_succeed(payment_id)
        decrease_product_count(payment)
        return Response(payment)

class PaymentFailedApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, payment_id):
        payment = payment_failed(payment_id)
        return Response(payment)




