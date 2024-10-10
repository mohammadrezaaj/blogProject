from django.urls import path, re_path
from article_app import views


app_name="article"
urlpatterns = [
    path('list', views.ArticleListView.as_view(), name='list'),
    path('listq', views.search, name='searchs'),
    path('list/<str:category>', views.CategoryListView.as_view(), name='category-list'),
    path('navbar', views.NavbarPartialView.as_view(), name='navbar'),
    re_path('message/(?P<slug>[-\w]+)/', views.ArticleMessageView.as_view(), name='message'),

    re_path('detail/(?P<slug>[-\w]+)/', views.ArticleDetailView.as_view(), name='detail'),
]