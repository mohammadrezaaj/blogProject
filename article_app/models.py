from django.contrib.auth.models import User
from django.db import models




class Category(models.Model):
    title = models.CharField(max_length=128, verbose_name='عنوان')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               blank=True, null=True, verbose_name='نویسنده')
    title = models.CharField(max_length=128, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/article/main',
                              blank=True, null=True, verbose_name='تصویر اصلی')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 blank=True, null=True, verbose_name='دسته بندی')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False, verbose_name='انتشار')
    slug = models.SlugField(max_length=200, unique=True, editable=True,
                            allow_unicode=True)
    click_count = models.PositiveIntegerField(default=0, verbose_name='بازدید')

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(Article, self).save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class ArticleInline(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='lines', verbose_name='مقاله')
    title = models.CharField(max_length=128, verbose_name='عنوان', blank=True, null=True)
    body = models.TextField(max_length=2048, verbose_name='متن', blank=True, null=True)
    image = models.ImageField(upload_to='images/article/inline', verbose_name='تصویر', blank=True, null=True)

    def __str__(self):
        return f"{self.article} - {self.title}"

    class Meta:
        verbose_name = 'سطر'
        verbose_name_plural= "سطرها"


class ArticleMessage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='message', verbose_name='مقاله')
    fullname = models.CharField(max_length=128, verbose_name="نام و نام خانوادگی")
    phone = models.PositiveBigIntegerField(verbose_name='شماره موبایل',max_length=11)
    message = models.TextField(verbose_name='پیام',)

    def __str__(self):
        return f'{self.fullname} - {self.message[:50]}...'

    class Meta:
        verbose_name = 'نطر'
        verbose_name_plural = "نظرات"
