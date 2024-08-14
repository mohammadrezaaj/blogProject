from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from product_app import models

from django.shortcuts import get_object_or_404, render
from django.utils.encoding import uri_to_iri

class ProductListView(View):
    def get(self, request):
        exel_list = models.ExelFiles.objects.all().order_by('-created').filter(status=True)
        return render(request, 'product_app/product-list.html', {'exel_list':exel_list})


class ProductDownloadView(View):
    def get(self,request, slug):
        exel_files = models.ExelFiles
        exel_file = get_object_or_404(exel_files, slug=uri_to_iri(slug))
        exel_file.click_count += 1
        return FileResponse(exel_file.file, as_attachment=True)
