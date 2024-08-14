from django.contrib import admin
from product_app import models

@admin.register(models.ExelFiles)
class ExecAdmin(admin.ModelAdmin):
    list_display = ['__str__','title','status','click_count']
    readonly_fields = ['click_count',]
    list_editable = ['status',]
    search_fields = ['title',]
    prepopulated_fields = {'slug':('title',)}
