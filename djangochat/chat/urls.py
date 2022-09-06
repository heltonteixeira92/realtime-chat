from django.urls import path
from . import views


# app_name = ''

urlpatterns = [
    path('', views.home, name='home'),
    path('checkview', views.checkview, name='checkview'),
    path('<str:room>/', views.room, name='room'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

]
