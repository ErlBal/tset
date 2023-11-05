from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('registrations/', views.RegView.as_view()),
    path('login/', views.AuthLogView.as_view(), name='home'),
    path('logout', views.AuthLogoutView.as_view(), name='logout'),
    path('users/', views.UserListView.as_view(), name='post'),
]