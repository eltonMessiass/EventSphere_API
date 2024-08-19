from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import userView, user_detail

urlpatterns = [
    path('signup/', userView, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name="get_token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('users/', userView, name='users'),
    path('users/<int:id>/', user_detail, name='user_detail')
]
