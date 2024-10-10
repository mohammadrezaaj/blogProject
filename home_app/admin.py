from django.contrib import admin
from home_app import models


class bookLinesAdmin(admin.StackedInline):
    model = models.AccountingBookLines

@admin.register(models.AccountingBook)
class accountingBookAdmin(admin.ModelAdmin):
    list_display = ['title',]
    inlines = (bookLinesAdmin,)

@admin.register(models.Customers)
class customersAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(models.ContactUsers)
class contactUsers(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'done']
    list_editable = ['done',]



