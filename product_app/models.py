from django.db import models
from django.utils.text import slugify


class ExelFiles(models.Model):
    title = models.CharField(max_length=128, verbose_name='عنوان')
    status = models.BooleanField(default=False, verbose_name='وضعیت',
                                 help_text='اگر تیک را بزنید کاربران میتوانند این فایل را مشاهده یا دانلود کنند')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/exel-images', verbose_name='تصویر')
    file = models.FileField(upload_to='exel-files', verbose_name='فایل اکسل')
    slug = models.SlugField(max_length=200, unique=True,editable=True,
                            allow_unicode=True)
    click_count = models.PositiveIntegerField(default=0, verbose_name='تعداد دانلود')


    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(ExelFiles, self).save()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'فایل اکسل'
        verbose_name_plural = 'فایل های اکسل'