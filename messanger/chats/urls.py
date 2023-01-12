from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import (
    chats,
    private_chat
)

urlpatterns = [
    path('', chats),
    path('<str:user>', private_chat)
]

urlpatterns += staticfiles_urlpatterns()