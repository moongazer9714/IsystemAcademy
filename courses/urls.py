import imp
from django.urls import path
from courses import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('courses/<slug:slug>/', views.courses_detail, name='courses_detail'),
]