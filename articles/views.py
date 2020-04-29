from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def Articles(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})