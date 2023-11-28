# dashboard/urls.py
from django.urls import path
from .views import dashboard_view,index

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', index, name='index'),
]
