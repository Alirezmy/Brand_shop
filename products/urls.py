from django.urls import path
from products.views import ProductCreateView, ProductListView


urlpatterns = [
    path('v1/create', ProductCreateView.as_view()),
    path('v1/list', ProductListView.as_view()),

]