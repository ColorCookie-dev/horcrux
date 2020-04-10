from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexView, name='index'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('login/', views.loginPage, name='login_url'),

    path('register/', views.registerView, name="register_url"),
    path('logout/', views.logoutUser, name='logout_url'),
]
