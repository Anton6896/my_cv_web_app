from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeUsers, register, ProfileUserUpdate

app_name = 'users'

urlpatterns = [
    path('', HomeUsers.as_view(), name='home'),
    path('<str:uname>', HomeUsers.as_view(), name='user_home'),
    path('register/', register, name='register'),
    path('profile/<int:pk>', ProfileUserUpdate.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login_users.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout_users.html'), name='logout'),

]
