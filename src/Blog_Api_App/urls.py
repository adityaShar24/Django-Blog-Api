from django.urls import path

from .views.blog_view import post_blog , get_all_blogs

urlpatterns = [
    path('blog/post/', post_blog , name='post_blog'),
    path('blog/get-all/', get_all_blogs , name='get_all_blogs')
]