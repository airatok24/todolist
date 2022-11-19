from django.urls import path
from core import views

urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('profile', views.ProfileView.as_view(), name='update-retrieve-destroy-user'),
    path('update_passwords', views.UpdatePasswords.as_view(), name='update-password'),

]

