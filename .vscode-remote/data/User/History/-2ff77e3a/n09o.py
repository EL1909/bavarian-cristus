from . import views
from django.urls import path


urlpatterns = [
    path('', views.ImagePostList.as_view(), name='home')
]