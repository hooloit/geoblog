from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import *

app_name = 'reg'

urlpatterns = [
    path('reg/', register, name="reg"),
    path('api/token/', Test.as_view(), name='test'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
