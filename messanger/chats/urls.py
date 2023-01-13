from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import (
    chats,
    private_chat,
    add_contact
)

urlpatterns = [
    path('', chats),
    path('<str:user>/pv/', private_chat),
    path('add-contact', add_contact),

]
