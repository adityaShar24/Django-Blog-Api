from django.urls import path
from ..views.blog_view import post_blog , update_blog , get_all_blogs , get_by_id

urlpatterns = [
    path('post' , post_blog , name='post_blog'),
    path('update/<str:pk>' , update_blog , name='update_blog'),
    path('get-all' , get_all_blogs , name='get_all_blogs'),
    path('get/<str:pk>' , get_by_id , name='get_by_id'),
]