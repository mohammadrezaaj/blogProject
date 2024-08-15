from django import forms

from article_app.models import ArticleMessage


class ArticleMessageForm(forms.ModelForm):
    class Meta:
        model = ArticleMessage
        exclude = ['article',]

        widgets = {
            'fullname': forms.TextInput(attrs={
                'placeholder':'نام کامل را وارد کنید',

            }),
            'phone': forms.TextInput(attrs={
                'placeholder':'شماره موبایل را وارد کنید'
            }),
            'message': forms.Textarea(attrs={
                'placeholder':'دیدگاهتان را بنویسید'
            })
        }
