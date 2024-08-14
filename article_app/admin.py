from django.contrib import admin

from article_app import models

class FilterByTitle(admin.SimpleListFilter):
    title = 'کلید های پر تکرار'
    parameter_name = 'title'

    # def lookups(self, request, model_admin):
    #     return (
    #         ('django', 'DJANGO'),
    #         ('python', 'PYTHON'),
    #     )
    def lookups(self, request, model_admin):

        most_clicked_choices = models.Article.objects.order_by('-click_count').values_list('title', 'title')[:5]

        return tuple(most_clicked_choices)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


class ArticleInLine(admin.StackedInline):
    model = models.ArticleInline

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','created']

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['__str__','title','author','published','click_count']
    list_editable = ['published']
    list_filter = ('published', FilterByTitle)
    search_fields = ('title', 'body', 'auther')
    readonly_fields = ['click_count']
    inlines = (ArticleInLine,)
    prepopulated_fields = {'slug':['title',]}