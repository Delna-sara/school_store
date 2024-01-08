from django.urls import path

from . import views
from .views import DepartmentListView

urlpatterns = [
    path('base/', views.home, name='base'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('new_page/', views.new_page, name='new_page'),
    path('form_page/', views.form_page, name='form_page'),
    path('logout/', views.logout, name='logout'),
    path('departments/', DepartmentListView.as_view(), name='departments'),



]
