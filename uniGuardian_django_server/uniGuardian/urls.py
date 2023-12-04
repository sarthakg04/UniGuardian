# dashboard/urls.py

from django.urls import path
from .views import *


urlpatterns = [
  path('api/dashboard/', create_user_profile),
  path('api/dashboard/<str:email>/', fetch_user_profile),
  path('dashboard/', dashboard_view, name='dashboard'),
  path('', index, name='index'),
  path('upload-transcript/', upload_transcript, name='upload_transcript'),
  path('check-analysis/<str:email>/', check_analysis, name='check_analysis'),
]