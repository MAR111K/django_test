from django.urls import path
from .views.auth_views import RegisterView, LoginView
from .views.user import UserMeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/me/', UserMeView.as_view(), name='user-me'),
]