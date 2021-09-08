import os
from celery import current_app
from django import forms  
from django.conf import settings  
from django.http import JsonResponse  
from django.shortcuts import render  
from django.views import View
from .tasks import adding_task
from django.core.files.storage import FileSystemStorage
from django.views.generic import CreateView
from .forms import *


class WelderCreate(CreateView):

    model = Welder
    form_class = WelderForm
    extra_context = {'file': Welder.objects.all()}
    template_name = 'welder_create.html'
    success_url = '/welder/'


def home_page(request):
    # POST
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        file_url = fs.url(filename)
        #отправляем файл в task --  celory
        task = adding_task.delay(file_url)
        
        return render(request, 'home_page.html', {
            'file_url': file_url
        })
    return render(request, 'home_page.html')
