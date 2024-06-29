from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include('django.contrib.auth.urls')),
    path("register/", views.register, name='register'),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('accounts/profile/', views.profile, name='profile'),
    path('unapproved_takeaways/', views.unapproved_takeaways,
         name='unapproved_takeaways'),
    path('afhaalacties/', views.update_afhaalacties, name='afhaalacties'),
    path('confirm_afhaalacties/', views.confirm_afhaalacties,
         name='confirm_afhaalacties'),
    path('manage_collections/', views.manage_collections,
         name='manage_collections'),
    path('medicine/', views.medicine, name='medicine'),
    path('new_medicine/', views.new_medicine, name='new_medicine'),
]
