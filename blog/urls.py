from django.urls import path
# from .views import index, single_post_page
from .views import PostList, PostDetail
from . import views

urlpatterns = [
    path('category/<str:slug>/', views.category_page),
    path('', views.PostList.as_view()), # CBV 방식의 call
    # path('', index, name="index"), # FBV 방식의 call
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail')
    # path('<int:pk>/', single_post_page, name='post_detail'),
    # path('', views.index),
]
