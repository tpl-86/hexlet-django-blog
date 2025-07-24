from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        return redirect(url)
    
    
class IndexView(View):
    def get(self, request, tags, article_id, *args, **kwargs):
        return HttpResponse(
            f'Статья номер {article_id}. Тег {tags}')