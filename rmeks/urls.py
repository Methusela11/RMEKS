from . import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_page, name='login'),
    path('methusela-enoch/', views.cv, name='cv'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
]