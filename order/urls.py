from django.urls import path
from order.views import CreateCheckoutApiView, PaymentFailedApiView, PaymentSuccceedApiView

urlpatterns = [
    path('order/chek', CreateCheckoutApiView.as_view()),
    path('order/failed', PaymentFailedApiView.as_view()),
    path('order/succeed', PaymentSuccceedApiView.as_view()),

]