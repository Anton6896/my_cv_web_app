from django.urls import path
from .views import HomeUsers

pp_name = 'users'

urlpatterns = [
    path('', HomeUsers.as_view(), name='home_users'),

]
