from django.urls import path, re_path

from product_app import views

app_name="product"
urlpatterns = [
    path('list', views.ProductListView.as_view(), name='filelist'),
    re_path('download/(?P<slug>[-\w]+)/', views.ProductDownloadView.as_view(), name='download'),
]