from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('create/', views.ImagePostCreate.as_view(), name='create'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
