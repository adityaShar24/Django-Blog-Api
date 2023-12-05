from django.urls import path

from .views.blog_view import post_blog , get_all_blogs
from .views.auth_view import register_user , login_user

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('blog/post/', post_blog , name='post_blog'),
    path('blog/get-all/', get_all_blogs , name='get_all_blogs'),
    path('auth/register/', register_user , name='register_user'),
    path('auth/login/', login_user , name='login_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]