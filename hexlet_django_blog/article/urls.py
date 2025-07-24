from django.urls import path
from hexlet_django_blog.article.views import IndexView, HomeView


urlpatterns = [
    path('', HomeView.as_view()),
    path("<str:tags>/<int:article_id>/", IndexView.as_view(), name='article'),
]