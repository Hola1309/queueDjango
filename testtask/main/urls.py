from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    path('person/', views.users),
    path('list', views.list),
]
