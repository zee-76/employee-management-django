from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/dashboard/')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('list/', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'), # New delete URL
    path('register/', views.register, name='register'),
    path('accounts/logout/', views.test_logout, name='test_logout'),
]