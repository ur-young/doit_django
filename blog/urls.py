from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name="index"),
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]
