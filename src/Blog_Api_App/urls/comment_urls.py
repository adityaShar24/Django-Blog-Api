from django.urls import path
from ..views.comment_view import create_comment , update_comment


urlpatterns = [
    path('create' , create_comment , name='comment'),
    path('update' , update_comment , name='update'),
]

