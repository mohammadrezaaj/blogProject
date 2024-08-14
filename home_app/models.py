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
