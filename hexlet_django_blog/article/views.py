from django.shortcuts import render
from django.urls import reverse
from django.views import View
from hexlet_django_blog.article.models import Article


class HomeView(View):
    def get(self, request, *args, **kwargs):
        url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        return redirect(url)
    
    
class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles":articles,
            },
        )