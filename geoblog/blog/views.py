from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, "chat.html")
def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})