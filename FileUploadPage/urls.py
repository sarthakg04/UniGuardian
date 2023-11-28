from django.urls import path
from hello import views

urlpatterns = [
    path("", views.file_upload, name="file_upload"),
]