from django.contrib import admin
from django.urls import path, include
from .views import home
from accounts.views import (
    login_view,
    logout_view,
    register_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path("chats/", include('chats.urls')),
    path("login/", login_view),
    path("logout/", logout_view),
    path("sign-up/", register_view)
]
