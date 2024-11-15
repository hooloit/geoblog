from ast import parse
from bisect import insort
from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import parsers
from .models import post
from .serializers import postSerializer



class postViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = postSerializer

#  Просто пиздец
# # GET и POST запросы
# class postAPIList(generics.ListCreateAPIView):
#     queryset = post.objects.all()
#     serializer_class = postSerializer
#
# #Обновление БД
# class postAPIUpdate(generics.UpdateAPIView):
#     queryset = post.objects.all()
#     serializer_class = postSerializer
#
# class postAPICrud(generics.RetrieveUpdateDestroyAPIView):
#     queryset = post.objects.all()
#     serializer_class = postSerializer

# Расписаный пиздец
# class postAPIView(APIView):
#     # GET запрос
#     def get(self, request):
#         p = post.objects.all()
#         return Response({"post": postSerializer(p, many=True).data})
#
#     # POST запрос
#     def post(self, request):
#         serializer = postSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True) # Проверка данных
#         serializer.save() # Метод create
#         return Response({"post": serializer.data})
#
#     def put(self, requset, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = post.objects.get(pk=pk) # проверяем наличие записи
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = postSerializer(data=requset.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = post.objects.get(pk=pk)  # проверяем наличие записи
#         except:
#             return Response({"error": "Object does not exists"})
#
#         post.objects.filter(id=pk).delete()
#         return Response({"delete": str(pk)})

def index(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, "chat.html")

def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})

def create(request):
    return render(request, "create_post.html")