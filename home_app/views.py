from django.shortcuts import render
from django.views import View
from article_app.models import Article

class HomeView(View):
    def get(self, request):
        articles = Article.objects.filter(published=True).order_by('-created')[:6]
        return render(request, 'home_app/index.html',{'articles':articles})


class AboutUsView(View):
    def get(self, request):
        return render(request, 'home_app/about-us.html',{})


class ContactUsView(View):
    def get(self, request):
        return render(request, 'home_app/contact-us.html', {})

