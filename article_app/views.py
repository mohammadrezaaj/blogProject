from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.encoding import uri_to_iri
from django.views import View
from django.views.generic import TemplateView

from article_app import models
from article_app.Forms import ArticleMessageForm


class ArticleListView(View):
    def get(self, request):
        articles = models.Article.objects.all().order_by('-created').filter(published=True)
        page_number = request.GET.get('page')
        paginator = Paginator(articles, 8)
        object_list = paginator.get_page(page_number)
        categories = models.Category.objects.all()
        context = {
            'categories': categories,
            'articles': object_list
        }
        return render(request, 'article_app/article-list.html', context)


class CategoryListView(View):
    def get(self, request, category):
        articles = models.Article.objects.all().order_by('-created').filter(category__title=category,
                                                                                published=True)
        page_number = request.GET.get('page')
        paginator = Paginator(articles, 8)
        object_list = paginator.get_page(page_number)
        categories = models.Category.objects.all()
        context = {
            'categories': categories,
            'articles': object_list
        }
        return render(request, 'article_app/article-list.html', context)

class NavbarPartialView(TemplateView):
    template_name = 'includes/header.html'

    def get_context_data(self, **kwargs):
        context = super(NavbarPartialView, self).get_context_data()
        context['categories'] = models.Category.objects.all()
        return context


class ArticleDetailView(View):

    def get(self, request, slug):
        form = ArticleMessageForm()
        articles = models.Article
        article = get_object_or_404(articles, slug=uri_to_iri(slug))
        article.click_count += 1
        article.save()
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'article_app/article-detail.html', context)


def search(request):
    q = request.GET.get('q')
    articles = models.Article.objects.filter(title__contains=q, published=True).order_by('-created')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 8)
    object_list = paginator.get_page(page_number)
    categories = models.Category.objects.all()
    context = {
        'categories': categories,
        'articles': object_list
    }
    return render(request, 'article_app/article-list.html', context)

class ArticleMessageView(View):
    def post(self,request, slug):
        form = ArticleMessageForm(data=request.POST)
        query = form.data
        article = get_object_or_404(models.Article, slug=uri_to_iri(slug))
        fullname = query.get('fullname')
        phone = int(query.get('phone'))
        message = query.get('message')
        if len(str(phone)) == 10:
            models.ArticleMessage.objects.create(fullname=fullname, phone=phone, message=message, article=article)
        form = ArticleMessageForm()
        context = {
            'article': article,
            'form': form,
        }
        return redirect('article:detail',slug=slug)


