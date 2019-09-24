from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name="about"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('contactus', views.contactus, name="contactus"),
]