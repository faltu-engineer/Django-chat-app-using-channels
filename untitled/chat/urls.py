from django.urls import path, re_path
from django.urls import path

from  . import views

app_name = 'chat'

urlpatterns=[
    path('',views.ShowChatHome,name='showchat'),
    path('room/<str:room_name>/<str:person_name>', views.ShowChatPage, name='showchat'),
]
