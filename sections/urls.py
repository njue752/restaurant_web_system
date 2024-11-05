"""
URL configuration for Hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import delivery_index, add_meal, pay_page, booked_services, UserListView, edit_meal, view_booked_services
from .views import confirm_order , book_meal
from .views import darajaapi
from .views import delete_appointment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('administrators/', views.administrators, name='administrators'),
    path('users/', views.user_list, name='view_users'),
    path('delivery/', views.delivery_index, name='delivery'),
    path('logout/', views.logout, name='logout'),
    path('delivery/', views.delivery_index, name='delivery'),
    path('menu/', views.menu_page, name='menu_page'),
    path('delivery/add/', add_meal, name='add_meal'),  # Add this line
    path('booked_services/', booked_services, name='booked_services'),
    path('view_booked_services/', views.view_booked_services, name='view_booked_services'),
    path('appointments/delete/<int:id>/', delete_appointment, name='delete_appointment'),  # Include the ID in the URL
    # path('admin/users/', UserListView.as_view(), name='user_list'),
    path('view_meals/', views.view_meals, name='view_meals'),  # No arguments needed here
    path('view_users/', views.view_users, name='user_list'),  # Make sure this name is consistent
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('edit_meal/<int:meal_id>/', edit_meal, name='edit_meal'),
    path('book_meal/<int:meal_id>/', views.book_meal, name='book_meal'),  # New URL for booking
    path('confirm_order/<int:meal_id>/', confirm_order, name='confirm_order'),
    path('darajaapi/<int:meal_id>/', darajaapi, name='darajaapi'),
    path('pay/<int:meal_id>/', pay_page, name='pay'),
    # path('appointments/', views.booked_services, name='booked'),  # Make sure this matches
    # path('appointments/delete/<int:id>/', views.delete_appointment, name='delete_appointment'),
]

