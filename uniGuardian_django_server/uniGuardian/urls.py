# dashboard/urls.py
# from django.urls import path
# from .views import dashboard_view,index
#
# urlpatterns = [
#     path('dashboard/', dashboard_view, name='dashboard'),
#     path('', index, name='index'),
# ]

# from django.urls import include, re_path
# from uniGuardian import views
#
# urlpatterns = [
#     re_path(r'^api/dashboard$', views.create_user_profile),
#     re_path(r'^api/dashboard/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', views.fetch_user_profile),
# ]


from django.urls import path

from uniGuardian import views

urlpatterns = [
  path('api/dashboard/', views.create_user_profile),
  path('api/dashboard/<str:email>/', views.fetch_user_profile),
]