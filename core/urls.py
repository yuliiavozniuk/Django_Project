from django.urls import path
from core.views import CustomUserCreateView


urlpatterns = [
    path('register/', CustomUserCreateView.as_view(), name='user-register'),
]