from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from .views import Posts,PostDetail,CreateComment,PostCreate,profil_list,success_button,delete_button

urlpatterns = [
    
    path('home/', Posts.as_view(),  name = 'home'),
    path('detail/<int:pk>/', PostDetail.as_view(),  name = 'detail'),
    path('create_post/', PostCreate.as_view(),  name = 'create_post'),
    path('comment/', CreateComment.as_view(),  name = 'comment'),
    path('profile/', profil_list,  name = 'profile'),
    path('success_button/<int:pk>/', success_button,  name = 'success_button'),
    path('delete_button/<int:pk>/', delete_button,  name = 'delete_button'),
]
