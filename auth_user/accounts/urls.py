from django.urls import path
from .views import signup_view, login_view, dashboard_view

urlpatterns = [
    path('dashboard', dashboard_view, name='dashboard'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
]