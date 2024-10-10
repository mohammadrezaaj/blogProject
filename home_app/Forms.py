from django import forms

from home_app.models import ContactUsers


class ContactUsersForm(forms.ModelForm):
    class Meta:
        model = ContactUsers
        exclude = ['done', 'note']

        widgets = {
            'fullname': forms.TextInput(attrs={
                'placeholder':'نام و نام خانوادگی',

            }),
            'phone': forms.TextInput(attrs={
                'placeholder':'شماره موبایل',

            }),
        }
