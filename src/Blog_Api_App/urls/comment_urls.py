from django.urls import path
from ..views.comment_view import comment


urlpatterns = [
    path('comment' , comment , name='comment'),
]
