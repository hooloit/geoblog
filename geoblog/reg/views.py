from django.shortcuts import render

from django.utils.module_loading import import_string
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.views import TokenViewBase, TokenObtainPairView


# Create your views here.
def register(request):
    return render(request, 'register.html')

class Test(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    _serializer_class = api_settings.TOKEN_OBTAIN_SERIALIZER


token_obtain_pair = TokenObtainPairView.as_view()
