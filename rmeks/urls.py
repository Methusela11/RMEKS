from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_page, name='login'),
    path('methusela-enoch/', views.cv, name='cv'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)