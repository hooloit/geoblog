from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import post

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = "__all__"

