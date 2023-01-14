from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import time
from .models import (
    Messages
)

# Create your views here.
@login_required
def chats(request):
    message_sender = []
    for chat in Messages.objects.filter(to_user=request.user):
        message_sender.append(chat.from_user)
        message_sender.append(chat.message)
    sender = []
    for i in range(0, len(message_sender), 2):
        sender.append(message_sender[i])
    senders = [i for n, i in enumerate(sender) if i not in sender[:n]] 
    print(senders)
    message = []
    for i in range(1, len(message_sender), 2):
        message.append(message_sender[i])
    context =  {
        'chatstatus': 'active',
        "senders": senders,
    }
    return render(request, 'chats.html', context)
def private_chat(request, user):
    context = {
        "chatstatus": 'active',
        "user": user
    }
    messages = []
    for i in Messages.objects.all():
        if str(i.from_user) == str(user) and str(i.to_user) == str(request.user):
            messages.append(f"{i.from_user}: {i.message}")
        if str(i.to_user) == str(user) and str(i.from_user) == str(request.user):
            messages.append(f"you: {i.message}")
    
    if request.POST:
        Messages.objects.create(from_user=request.user, to_user=User.objects.get(username=str(user)), message=request.POST['message'])
        return redirect(f"/chats/{user}/pv/")
    context['sender_messages'] = messages

    return render(request, 'private_chat.html', context)
def add_contact(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'add-contact.html', context)
