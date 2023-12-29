from django.urls import path
from ..views.blog_view import post_blog , update_blog , get_all_blogs

urlpatterns = [
    path('post' , post_blog , name='post_blog'),
    path('update' , update_blog , name='update_blog'),
    path('get-all' , get_all_blogs , name='get_all_blogs'),
]