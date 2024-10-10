from django.db import models


# class JobList(models.Model):
#     title = models.CharField(max_length=64, verbose_name='')
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = ''
#         verbose_name_plural = ''
#
#
# class JobListLines(models.Model):
#     job_title = models.ForeignKey(JobList, on_delete=models.CASCADE, related_name='joblist')
#     body = models.TextField(verbose_name='')
#
#     class Meta:
#         verbose_name = ''
#         verbose_name_plural = ''

class AccountingBook(models.Model):
    title = models.CharField(max_length=64, verbose_name="عنوان")
    image = models.ImageField(upload_to='book/main_image', verbose_name='تصویر')
    published = models.BooleanField(default=False, verbose_name="انتشار")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کتاب قوانبن'
        verbose_name_plural = 'کتاب'


class AccountingBookLines(models.Model):
    book = models.ForeignKey(AccountingBook, on_delete=models.CASCADE, related_name='lines')
    title = models.CharField(max_length=128, verbose_name='عنوان')
    body = models.TextField(verbose_name='بدنه متن')

    class Meta:
        verbose_name = 'سطر'
        verbose_name_plural = 'سطر ها'


class Customers(models.Model):
    title = models.CharField(max_length=128, verbose_name='نام برند')
    image = models.ImageField(upload_to='customers/images', verbose_name='تصویر برند')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند مشتری'
        verbose_name_plural = 'برند مشتریان'


class ContactUsers(models.Model):
    fullname = models.CharField(max_length=256,verbose_name='نام و نام خانوادگی')
    phone = models.PositiveBigIntegerField(verbose_name='شماره موبایل')
    done = models.BooleanField(default=False, verbose_name='در دست انجام')
    note = models.TextField(verbose_name='یادداشت',blank=True,null=True)

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = 'ارتباط با کاربر'
        verbose_name_plural = 'ارتباط با کاربران'
