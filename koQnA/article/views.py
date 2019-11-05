from django.shortcuts import render
from django.views.generic import ListView
from article.models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
