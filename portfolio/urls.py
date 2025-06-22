from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # /root home URL
    path('home/', views.home, name='home'), # /home URL
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
]
