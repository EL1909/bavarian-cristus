from . import views
from django.urls import path


urlpatterns = [
    path('', PostList.as_view(), name='home')
]