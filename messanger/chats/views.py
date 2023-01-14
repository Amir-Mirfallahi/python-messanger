from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import (
    Messages
)

# Create your views here.
@login_required
def chats(request):
    # chats to user
    message_sender = []
    for chat in Messages.objects.filter(to_user=request.user):
        message_sender.append(chat.from_user)
        message_sender.append(chat.message)
    sender = []
    for i in range(0, len(message_sender), 2):
        sender.append(message_sender[i])
    senders = [i for n, i in enumerate(sender) if i not in sender[:n]] 
    # chats from user
    chats = []
    for i in Messages.objects.filter(from_user=request.user):
        chats.append(i.to_user)
    for a in chats:
        senders.append(a)
    
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
    result = []
    for i in users:
        user = i
        if user == request.user:
            continue
        result.append(user)
    context = {
        'users': result
    }
    return render(request, 'add-contact.html', context)
