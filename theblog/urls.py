from django.urls import path
from . import views
from .views import *

urlpatterns = [
    #path('',views.home,name='home'),
    path('',HomeView.as_view(),name='home'),
    path('article/<str:pk>/',ArticleDetailView.as_view(),name='postDetail'),
    path('addPost/',AddPostView.as_view(),name='addPost'),
    path('addCategory/',AddCategoryView.as_view(),name='addCategory'),
    path('article/editPost/<int:pk>/',UpdatePostView.as_view(),name='editPost'),
    path('article/deletePost/<int:pk>/',DeletePostView.as_view(),name='deletePost'),
    path('category/<str:cats>/',CategoryView,name="category"),
    path('category-list/',CategoryListView,name="category_list_view"),
    path('like/<int:pk>',LikeView,name="like_post"),
]