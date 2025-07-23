from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('articles/', include("hexlet_django_blog.article.urls")),
    path('about/', views.about),
    path('admin/', admin.site.urls),
]
