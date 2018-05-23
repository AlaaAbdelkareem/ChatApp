from django.contrib.auth.views import logout
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls import url , include

urlpatterns = [
    url(r'', views.index, name='index'),
    url(r'^chat', views.chat_view, name='chats'),
    url(r'^chat/<int:sender>/<int:receiver>', views.message_view, name='chat'),
    url(r'^api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    url(r'^api/messages', views.message_list, name='message-list'),
    url(r'^api/users/<int:pk>', views.user_list, name='user-detail'),
    url(r'^api/users', views.user_list, name='user-list'),
    url(r'^logout', logout, {'next_page': 'index'}, name='logout'),
    url(r'^register', views.register_view, name='register'),
]
