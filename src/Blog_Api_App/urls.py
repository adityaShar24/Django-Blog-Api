from django.urls import path

from . import views

urlpatterns = [
    path('blog/post/', views.post_blog, name='post_blog'),
]