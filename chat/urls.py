from django.contrib.auth.views import logout
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.urls import path , include


urlpatterns = [
    path('', views.index, name='index'),
    path('chats', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
    path('api/users/<int:pk>', views.user_list, name='user-detail'),
    path('api/users', views.user_list, name='user-list'),
    path('logout', logout, {'next_page': 'index'}, name='logout'),
    path('register', views.register_view, name='register'),
]