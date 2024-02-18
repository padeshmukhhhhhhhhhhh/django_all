
from django.urls import path
from . import views


urlpatterns = [
   # path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('', views.signup, name='signup'),
	path('rooms', views.rooms, name='rooms'),
	path('chat/<int:id>', views.chat, name='chat'),
	
]
