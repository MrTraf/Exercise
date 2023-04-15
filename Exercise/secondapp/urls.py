from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path('input/', views.input, name='input'),
    path('second_input/', views.Insert_record, name='second_input'),
    path('display/', views.display, name='display'),
]