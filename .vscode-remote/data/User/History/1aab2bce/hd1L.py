from django.urls import path
from . import views

urlpatterns = [
    path('', views.postList.as_view(), name='home'),
    path('profile/(?P<username>[^/]+)/?', views.profile, name='profile'),
    path('upload', views.upload, name='upload'),
    path('post_edit/<item_slug>', views.Post_edit, name='post_edit'),
    path('delete/<item_slug>', views.delete, name='delete'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.postDetail.as_view(), name='post_detail'),
    path('post/<slug:slug>/like/', views.postLike.as_view(), name='post_like'),
    path('<slug:item_slug>/confirm_delete/', views.confirm_delete, name='confirm_delete'),
]
