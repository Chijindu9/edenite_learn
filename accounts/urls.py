from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ProfileView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("register/", RegisterView.as_view()),
    path("profile/", ProfileView.as_view()),
]
