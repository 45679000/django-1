from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'stories': articles})

def full_article(request, pk):
    article_full = Article.objects.get(id= pk)
    f_article = Article.objects.all()
    return render(request, 'articles/full_article.html', context={'f_article': f_article})