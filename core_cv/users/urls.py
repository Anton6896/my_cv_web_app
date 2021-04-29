from django.urls import path
from .views import HomeUsers

app_name = 'users'

urlpatterns = [
    path('', HomeUsers.as_view(), name='home'),

]
