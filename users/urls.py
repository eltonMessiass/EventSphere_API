from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import userView, user_detail,profileDetailView, profileView, logged_user_profile

urlpatterns = [
    path('signup/', userView, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name="get_token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('users/', userView, name='users'),
    path('users/<int:id>/', user_detail, name='user_detail'),
    path('users/profiles/', profileView, name="all_profiles"),
    path('users/profiles/<int:id>/', profileDetailView, name='user_profile'),
    path('users/my_profile/', logged_user_profile, name="my_profile")
]
