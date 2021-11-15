from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('josephtan/', views.josephtan, name='blog-josephtan'),

]