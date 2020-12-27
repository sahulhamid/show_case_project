from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/bio/', bio, name='bio'),
    path('post/', post, name='post'),
    path('mypost/', my_post, name='mypost'),
    path('mypost/<str:pk>/delete', del_my_post, name='delete'),
    path('allpost/', all_post, name='allpost')
]
