from django.shortcuts import render
from .models import ChatRoom,ChatMessage
def index(request):
    rooms = ChatRoom.objects.all()
    return render(request,'chatapp/index.html',{'rooms':rooms})

def chatroom(request,slug):
    room = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=room)[0:30]
    return render(request,'chatapp/room.html',{'room':room,"messages":messages})
