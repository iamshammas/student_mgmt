from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.user_login,name='user_login'),
    path('home/',views.home,name='home'),
    path('register/',views.user_register,name='user_register'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
    path('password_reset/',views.password_reset,name='password_reset'),
    path('admin_panel/',views.admin_panel,name='admin_panel'),

]
