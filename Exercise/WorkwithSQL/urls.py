from django.urls import path
from . import views

urlpatterns= [
#  path("", views.second_input, name='second_input'),
  path('', views.second_input, name='second_input')
]
