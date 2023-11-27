# dashboard/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('file_upload_sop/', file_upload_sop, name='file_upload_sop'),
    path('file_upload_resume/', file_upload_resume, name='file_upload_resume'),
    path('file_upload_rl/', file_upload_rl, name='file_upload_rl'),
    path('home/', home, name='home'),
]
