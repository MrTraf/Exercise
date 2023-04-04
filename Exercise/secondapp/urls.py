from django.urls import path
from . import views

urlpatterns= [
   path("", views.home, name='home'),
   path('input/', views.input, name='input'),
   #new one
   path('second_input/', views.Insertrecord, name='second_input'),
#   path('second_output/', views.second_output, name='second_output'),

   #second_new
   path('display/',views.display,name='display'),
]
