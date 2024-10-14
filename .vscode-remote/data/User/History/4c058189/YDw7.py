from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('upload', views.upload, name='upload'),
    path('post_edit/<item_slug>', views.Post_edit, name='post_edit'),
    path('delete/<item_slug>', views.Delete, name='delete'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')
]
