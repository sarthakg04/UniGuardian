# dashboard/urls.py

from django.urls import path
from .views import *


urlpatterns = [
  path('api/dashboard/', create_user_profile),
  path('api/dashboard/<str:email>/', fetch_user_profile),
  path('dashboard/', dashboard_view, name='dashboard'),
  path('', index, name='index'),
]