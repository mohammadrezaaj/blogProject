from django.urls import re_path
from django.views.static import serve
from django.conf import settings


from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounting_web_Bv import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('product/', include('product_app.urls')),
    path('article/', include('article_app.urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
