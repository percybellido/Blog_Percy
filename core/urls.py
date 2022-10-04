from django.urls import path
from . import views
from .views import HomePageView, AboutPageView

urlpatterns = [
    
    path('', HomePageView.as_view(), name="home"),
    path('about-me/', AboutPageView.as_view(), name="about"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contacto"),
    
]