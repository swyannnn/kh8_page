from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('josephtan/', views.josephtan, name='blog-josephtan'),
    path('mindyliew/', views.mindyliew, name='blog-mindyliew'),
    path('test/', views.test, name='blog-test')
]