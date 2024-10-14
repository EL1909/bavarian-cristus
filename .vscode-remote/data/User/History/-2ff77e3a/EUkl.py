from . import views
from django.urls import path


urlpatterns = [
    path('', view.PostList.as_view(), name='home')
]