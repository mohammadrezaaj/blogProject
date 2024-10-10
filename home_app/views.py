from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from article_app.models import Article
from home_app import models
from home_app.Forms import ContactUsersForm
from home_app.models import ContactUsers


class HomeView(View):
    def get(self, request):
        articles = Article.objects.filter(published=True).order_by('-created')[:6]
        form = ContactUsersForm()
        context = {
            'articles': articles,
            'form': form,
        }
        return render(request, 'home_app/index.html',context)

class ContactPeopleView(View):
    def post(self,request):
        form = ContactUsersForm(data=request.POST)
        query = form.data
        fullname = query.get('fullname')
        phone = int(query.get('phone'))
        if len(str(phone)) == 10:
            ContactUsers.objects.create(fullname=fullname, phone=phone)
        return redirect('home:main')




class AboutUsView(View):
    def get(self, request):
        return render(request, 'home_app/about-us.html',{})


class ContactUsView(View):
    def get(self, request):
        form = ContactUsersForm()
        context = {
            'form': form,
        }
        return render(request, 'home_app/contact-us.html', context)


class AccountingBookView(View):
    def get(self, request):
        book = models.AccountingBook.objects.all().first()
        return render(request, 'home_app/rule-book.html',{'book':book})

class FooterPartialView(TemplateView):
    template_name = 'includes/footer.html'

    def get_context_data(self, **kwargs):
        context = super(FooterPartialView, self).get_context_data()
        context['customers'] = models.Customers.objects.all().order_by('-created')
        return context
