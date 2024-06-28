from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include('django.contrib.auth.urls')),
    path("register/", views.register, name='register'),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('accounts/profile/', views.profile, name='profile'),
    path('unapproved_takeaways/', views.profile, name='unapproved_takeaways'),
]
