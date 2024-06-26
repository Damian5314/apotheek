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
    path('update_afhaalacties/', views.update_afhaalacties, name='update_afhaalacties'),
    path('update_afhaalacties/', views.update_afhaalacties, name='update_afhaalacties'),
    path('afhaalacties/', views.update_afhaalacties, name='afhaalacties'),
    path('approve_afhaalactie/<int:pk>', views.approve_afhaalactie, name='approve_afhaalactie'),
    path('deny_afhaalactie/<int:pk>', views.deny_afhaalactie, name='deny_afhaalactie'),
    path('confirm_afhaalacties/', views.confirm_afhaalacties, name='confirm_afhaalacties'),
    path('manage_collections/', views.manage_collections, name='manage_collections'),
    path('manage_collections/<int:medicine_id>/', views.manage_collections, name='manage_collections_with_medicine'),
    path('medicine/', views.medicine, name='medicine'),
    path('new_medicine/', views.new_medicine, name='new_medicine'),
    path('edit_medicine/<int:pk>/', views.edit_medicine, name='edit_medicine'),
    path('delete_medicine/<int:pk>/', views.delete_medicine, name='delete_medicine'),
    path('select_user/', views.select_user, name='select_user'),
    path('user_history/<int:user_id>/', views.user_history, name='user_history'),
]
