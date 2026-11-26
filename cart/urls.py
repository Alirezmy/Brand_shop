from django.urls import path
from cart.views import AddToCartView, GetCartItemsView


urlpatterns = [
    path('cart/add', AddToCartView.as_view()),
    path('cart/get', GetCartItemsView.as_view()),

]