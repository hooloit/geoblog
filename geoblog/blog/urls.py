from django.urls import path, include, re_path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', index, name="index"),
    path('chat/', chat, name="chat"),
    # re_path(r'', include('django_private_chat2.urls', namespace='django_private_chat2')),
    path("chat/<str:room_name>/", room, name="room"),
]