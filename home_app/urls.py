from django.urls import path
from home_app import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='main'),
    path('contact', views.ContactPeopleView.as_view(), name='contactPeople'),
    path('about-us', views.AboutUsView.as_view(), name='about-us'),
    path('contact-us', views.ContactUsView.as_view(), name='contact-us'),
    path('book', views.AccountingBookView.as_view(), name='book'),
    path('footer', views.FooterPartialView.as_view(), name='footer'),

]