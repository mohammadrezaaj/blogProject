from django.urls import path
from home_app import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='main'),
    path('about-us', views.AboutUsView.as_view(), name='about-us'),
    path('contact-us', views.ContactUsView.as_view(), name='contact-us')
]