from django.urls import path
from ..views.comment_view import create_comment


urlpatterns = [
    path('comment' , create_comment , name='comment'),
]

