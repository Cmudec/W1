from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('first', views.first, name='first'),
    path('second/<int:id>/', views.second, name='second'),
]
