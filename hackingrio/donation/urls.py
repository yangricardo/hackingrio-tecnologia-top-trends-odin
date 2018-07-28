from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donate/', views.donation, name='donate'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
