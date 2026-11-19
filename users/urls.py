from django.urls import path

from users.views import UserRegister, UserLogin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('register/', UserRegister.as_view()),

    path('login/', UserLogin.as_view()),
    path('access-token/', TokenObtainPairView.as_view()),


]