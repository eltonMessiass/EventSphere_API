from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import userView

urlpatterns = [
    path('signup/', userView, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name="get_token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    
]
